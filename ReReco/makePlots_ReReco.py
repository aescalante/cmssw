#!/usr/bin/env python3
import ROOT
import argparse
import os
import re
import math

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)  # Turn off statistics box

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Compare histograms from multiple ROOT files')
    
    parser.add_argument('--files', '-f', type=str, nargs='+', required=True,
                       help='List of ROOT files containing histograms')
    
    parser.add_argument('--legends', '-l', type=str, nargs='+', default=None,
                       help='Legend entries for each histogram')
    
    parser.add_argument('--output-dir', '-o', type=str, default='comparison_plots',
                       help='Output directory for plots (default: comparison_plots)')
    
    parser.add_argument('--prefix', '-p', type=str, default='comparison',
                       help='Prefix for output filenames')
    
    parser.add_argument('--histograms', type=str, nargs='+', help='List of histogram names to plot')
    
    parser.add_argument('--file-index', '-i', type=int, nargs='+', default=None,
                       help='File index for each histogram (0-based). If not provided, all histograms are taken from first file')
    
    # Add new ratio plot options
    parser.add_argument('--ratio', '-r', action='store_true',
                       help='Add a ratio plot in the lower pad')
    
    parser.add_argument('--ratio-indices', type=int, nargs=2, default=[1, 0],
                       help='Indices of the histograms to use for ratio (numerator, denominator). Default: [1, 0]')
    
    parser.add_argument('--ratio-label', type=str, default=None,
                       help='Label for the ratio plot y-axis. Default: "Ratio"')
    
    args = parser.parse_args()
    
    # Validate files exist
    for file_path in args.files:
        if not os.path.exists(file_path):
            print(f"Error: Input file '{file_path}' not found.")
            exit(1)
    
    # Auto-generate legend entries if not provided
    if args.legends is None:
        args.legends = []
        for file_path in args.files:
            # Try to extract chi2 value from filename
            match = re.search(r'chi2_(\d+\.?\d*)_', file_path)
            if match:
                args.legends.append(f"Chi2 = {match.group(1)}")
            else:
                # Use basename as fallback
                basename = os.path.basename(file_path).split('_histograms.root')[0]
                args.legends.append(basename)
    
    # Choose which validation to apply based on whether --histograms is used
    if args.histograms:
        # When using --histograms, legends should match histograms
        if args.legends and len(args.legends) != len(args.histograms):
            print(f"Error: Number of legend entries ({len(args.legends)}) doesn't match number of histograms ({len(args.histograms)})")
            exit(1)
    else:
        # In standard mode, legends should match files
        if len(args.legends) != len(args.files):
            print(f"Error: Number of legend entries ({len(args.legends)}) doesn't match number of files ({len(args.files)})")
            exit(1)
    
    return args

def make_comparison_plot(hists, title, x_title, y_title, output_path, legends, normalize=False, log_y=False):
    """Create a plot comparing multiple histograms"""
    canvas = ROOT.TCanvas("c", title, 800, 600)
    
    if (log_y):
        canvas.SetLogy()
    
    # Colors for different histograms
    colors = [ROOT.kRed+1, ROOT.kBlue+1, ROOT.kGreen+2, ROOT.kOrange+1, ROOT.kViolet+1, 
              ROOT.kCyan+1, ROOT.kMagenta+1, ROOT.kYellow+2, ROOT.kGray+2, ROOT.kAzure+1]
    
    # Create legend
    legend = ROOT.TLegend(0.55, 0.73, 0.89, 0.89)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.SetTextSize(0.03) 
    
    # Find maximum y-value among all histograms
    y_max = 0
    for hist in hists:
        if normalize and hist.Integral() > 0:
            hist.Scale(1.0 / hist.Integral())
        
        if hist.GetMaximum() > y_max:
            y_max = hist.GetMaximum()
    
    # Draw histograms
    for i, (hist, legend_text) in enumerate(zip(hists, legends)):
        hist.SetLineColor(colors[i % len(colors)])
        hist.SetLineWidth(2)
        hist.SetFillColor(0)
        hist.SetTitle("")
        
        hist.GetXaxis().SetTitle(x_title)
        hist.GetYaxis().SetTitle(y_title)
        
        # Set y-axis range with 20% padding
        if log_y:
            hist.SetMaximum(y_max * 5)
            hist.SetMinimum(0.1)  # Non-zero minimum for log scale
        else:
            hist.SetMaximum(y_max * 1.2)
            hist.SetMinimum(0)  # Always start at zero for linear scale
        
        draw_option = "HIST" if i == 0 else "HIST SAME"
        hist.Draw(draw_option)
        
        # Add entry count to legend text
        entries = int(hist.GetEntries())
        legend_with_entries = f"{legend_text} [{entries}]"
        legend.AddEntry(hist, legend_with_entries, "l")
    
    # Draw legend
    legend.Draw()
    
    # Add CMS label
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextFont(61)
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.12, 0.92, "CMS")
    
    info_text = ROOT.TLatex()
    info_text.SetNDC()
    info_text.SetTextFont(42)
    info_text.SetTextSize(0.04)
    info_text.DrawLatex(0.20, 0.92, "Simulation Private Work")
    info_text.DrawLatex(0.66, 0.92, "Run 3 (13.6 TeV)")
    
    # Save the plot
    canvas.SaveAs(output_path)
    print(f"Saved: {output_path}")

def make_comparison_plot_with_ratio(hists, title, x_title, y_title, output_path, legends, 
                                   ratio_indices, ratio_label=None, normalize=False, log_y=False):
    """Create a plot comparing multiple histograms with a ratio panel"""
    # Create canvas divided into two pads
    canvas = ROOT.TCanvas("c", title, 800, 800)
    
    # Upper pad for histograms
    upper_pad = ROOT.TPad("upper_pad", "upper_pad", 0, 0.3, 1, 1)
    upper_pad.SetBottomMargin(0.02)  # Even smaller bottom margin since no x-axis labels
    upper_pad.SetLeftMargin(0.13)    # Increased left margin for y-axis labels
    upper_pad.SetRightMargin(0.05)   # Proper right margin
    upper_pad.SetTopMargin(0.08)     # Reduced top margin to better position CMS text
    upper_pad.SetGridx(False)
    upper_pad.SetGridy(False)
    if log_y:
        upper_pad.SetLogy()
    upper_pad.Draw()
    
    # Lower pad for ratio
    lower_pad = ROOT.TPad("lower_pad", "lower_pad", 0, 0, 1, 0.3)
    lower_pad.SetTopMargin(0.02)
    lower_pad.SetBottomMargin(0.35)  # Increased bottom margin for x-axis labels
    lower_pad.SetLeftMargin(0.13)    # Match left margin with upper pad
    lower_pad.SetRightMargin(0.05)   # Match right margin with upper pad
    lower_pad.SetGridx(False)
    lower_pad.SetGridy(False)
    lower_pad.Draw()
    
    # Colors for different histograms
    colors = [ROOT.kRed+1, ROOT.kBlue+1, ROOT.kGreen+2, ROOT.kOrange+1, ROOT.kViolet+1, 
              ROOT.kCyan+1, ROOT.kMagenta+1, ROOT.kYellow+2, ROOT.kGray+2, ROOT.kAzure+1]
    
    # Draw main histograms in upper pad
    upper_pad.cd()
    
    # Create legend with adjusted position
    legend = ROOT.TLegend(0.5, 0.65, 0.9, 0.89)  # Adjusted position to ensure it fits
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.SetTextSize(0.04)
    
    # For large number of entries, adjust text size
    if len(legends) > 4:
        legend.SetTextSize(0.035)
    if len(legends) > 6:
        legend.SetTextSize(0.03)
    
    # Find maximum y-value among all histograms
    y_max = 0
    for hist in hists:
        if normalize and hist.Integral() > 0:
            hist.Scale(1.0 / hist.Integral())
        
        if hist.GetMaximum() > y_max:
            y_max = hist.GetMaximum()
    
    # Draw histograms
    for i, (hist, legend_text) in enumerate(zip(hists, legends)):
        hist.SetLineColor(colors[i % len(colors)])
        hist.SetLineWidth(2)
        hist.SetFillColor(0)
        hist.SetTitle("")
        
        # No x-axis title in upper pad
        hist.GetXaxis().SetTitle("")
        hist.GetXaxis().SetLabelSize(0)  # Hide x-axis labels
        hist.GetYaxis().SetTitle(y_title)
        hist.GetYaxis().SetTitleSize(0.05)
        hist.GetYaxis().SetTitleOffset(1.4)  # Increased offset for y-axis title
        hist.GetYaxis().SetLabelSize(0.045)
        
        # Set y-axis range with 20% padding
        if log_y:
            hist.SetMaximum(y_max * 5)
            hist.SetMinimum(0.1)  # Non-zero minimum for log scale
        else:
            hist.SetMaximum(y_max * 1.2)
            hist.SetMinimum(0)  # Always start at zero for linear scale
        
        draw_option = "HIST" if i == 0 else "HIST SAME"
        hist.Draw(draw_option)
        
        # Add entry count to legend text (shorten if too long)
        entries = int(hist.GetEntries())
        if len(legend_text) > 25:  # Truncate long legend entries
            legend_text = legend_text[:22] + "..."
        legend_with_entries = f"{legend_text} [{entries}]"
        legend.AddEntry(hist, legend_with_entries, "l")
    
    # Draw legend
    legend.Draw()
    
    # Add CMS label with improved positioning
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextFont(61)
    cms_text.SetTextSize(0.06)
    cms_text.DrawLatex(0.15, 0.93, "CMS")
    
    info_text = ROOT.TLatex()
    info_text.SetNDC()
    info_text.SetTextFont(42)
    info_text.SetTextSize(0.045)
    info_text.DrawLatex(0.26, 0.93, "Simulation Private Work")  # More space after CMS
    info_text.DrawLatex(0.72, 0.93, "Run 3 (13.6 TeV)")  # Adjusted position
    
    # Lower pad for ratio
    lower_pad.cd()
    
    # Check if ratio indices are valid
    num_idx, denom_idx = ratio_indices
    if num_idx >= len(hists) or denom_idx >= len(hists) or num_idx < 0 or denom_idx < 0:
        print(f"Warning: Invalid ratio indices {num_idx}, {denom_idx}. Skipping ratio plot.")
        canvas.SaveAs(output_path)
        return
    
    # Create ratio histogram with properly propagated errors
    ratio_hist = hists[num_idx].Clone("ratio")
    ratio_hist.SetDirectory(0)
    
    # Get numerator and denominator histograms
    num_hist = hists[num_idx]
    denom_hist = hists[denom_idx]
    
    # Reset error calculation to prevent automatic error propagation
    ratio_hist.Sumw2(False)
    ratio_hist.Sumw2()
    
    # Manually propagate errors for each bin
    for bin in range(1, ratio_hist.GetNbinsX() + 1):
        num_val = num_hist.GetBinContent(bin)
        denom_val = denom_hist.GetBinContent(bin)
        
        num_err = num_hist.GetBinError(bin)
        denom_err = denom_hist.GetBinError(bin)
        
        # Skip if denominator is zero or too small
        if denom_val <= 0 or num_val <= 0:
            ratio_hist.SetBinContent(bin, 0)
            ratio_hist.SetBinError(bin, 0)
            continue
        
        # Calculate ratio
        ratio = num_val / denom_val
        
        # Properly propagate error for division: error = ratio * sqrt((num_err/num_val)^2 + (denom_err/denom_val)^2)
        # Only if both values are positive and have valid errors
        if num_err >= 0 and denom_err >= 0:
            rel_err_num = num_err / num_val if num_val > 0 else 0
            rel_err_denom = denom_err / denom_val if denom_val > 0 else 0
            
            # Calculate propagated relative error
            rel_err = math.sqrt(rel_err_num**2 + rel_err_denom**2)
            ratio_err = ratio * rel_err
            
            ratio_hist.SetBinContent(bin, ratio)
            ratio_hist.SetBinError(bin, ratio_err)
        else:
            ratio_hist.SetBinContent(bin, ratio)
            ratio_hist.SetBinError(bin, 0)
    
    # Set ratio histogram style
    ratio_hist.SetLineColor(ROOT.kBlack)
    ratio_hist.SetMarkerStyle(20)
    ratio_hist.SetMarkerSize(0.8)
    ratio_hist.SetMarkerColor(ROOT.kBlack)
    ratio_hist.SetTitle("")
    
    # Set axis properties for ratio plot
    ratio_hist.GetXaxis().SetTitle(x_title)  # Only show x-title in ratio plot
    ratio_hist.GetYaxis().SetTitle(ratio_label if ratio_label else "Ratio")
    ratio_hist.GetXaxis().SetTitleSize(0.11)
    ratio_hist.GetYaxis().SetTitleSize(0.11)
    ratio_hist.GetXaxis().SetTitleOffset(1.0)
    ratio_hist.GetYaxis().SetTitleOffset(0.6)  # Adjusted offset
    ratio_hist.GetXaxis().SetLabelSize(0.1)
    ratio_hist.GetYaxis().SetLabelSize(0.1)
    
    # Reduce number of tick marks
    ratio_hist.GetYaxis().SetNdivisions(505)
    ratio_hist.GetXaxis().SetNdivisions(508)
    
    # Calculate proper y-range to include all points
    ratio_min = 0.5
    ratio_max = 1.5
    
    # Find min/max ratio values ignoring zeros and NaNs
    has_valid_points = False
    for bin in range(1, ratio_hist.GetNbinsX() + 1):
        ratio_val = ratio_hist.GetBinContent(bin)
        if ratio_val > 0 and not ROOT.TMath.IsNaN(ratio_val):
            has_valid_points = True
            ratio_min = min(ratio_min, ratio_val * 0.8)
            ratio_max = max(ratio_max, ratio_val * 1.2)
    
    # Use default range if no valid points or all points are around 1
    if not has_valid_points or (abs(ratio_max - 1.0) < 0.1 and abs(ratio_min - 1.0) < 0.1):
        ratio_min = 0.5
        ratio_max = 1.5
    else:
        # Add extra padding for better visibility
        ratio_range = ratio_max - ratio_min
        ratio_min -= ratio_range * 0.1
        ratio_max += ratio_range * 0.1
        
        # Ensure min is always > 0 for ratio plots
        ratio_min = max(0.01, ratio_min)
    
    # Set the computed range
    ratio_hist.SetMinimum(ratio_min)
    ratio_hist.SetMaximum(ratio_max)
    
    # Draw ratio
    ratio_hist.Draw("EP")
    
    # Add line at y=1
    unity_line = ROOT.TLine(ratio_hist.GetXaxis().GetXmin(), 1, ratio_hist.GetXaxis().GetXmax(), 1)
    unity_line.SetLineColor(ROOT.kGray+2)
    unity_line.SetLineStyle(2)
    unity_line.Draw("SAME")
    
    # Add ratio legend - shortened versions of the histogram names
    num_name = legends[num_idx].split(" [")[0][:15]  # Truncate to first 15 chars
    denom_name = legends[denom_idx].split(" [")[0][:15]  # Truncate to first 15 chars
    
    ratio_text = ROOT.TLatex()
    ratio_text.SetNDC()
    ratio_text.SetTextFont(42)
    ratio_text.SetTextSize(0.09)
    ratio_text.DrawLatex(0.15, 0.91, f"{num_name} / {denom_name}")
    
    # Draw canvas with both pads
    canvas.Update()
    canvas.SaveAs(output_path)
    print(f"Saved plot with ratio: {output_path}")

def main():
    args = parse_args()
    
    # Create output directory
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # For custom histogram selection (potentially from different files)
    if args.files and args.histograms:
        histograms = []
        legends = []
        
        # Setup file indices
        file_indices = args.file_index if args.file_index else [0] * len(args.histograms)
        
        # Validate file indices
        if len(file_indices) != len(args.histograms):
            print(f"Error: Number of file indices ({len(file_indices)}) doesn't match number of histograms ({len(args.histograms)})")
            exit(1)
            
        # Check if any index is out of range
        for idx in file_indices:
            if idx < 0 or idx >= len(args.files):
                print(f"Error: File index {idx} is out of range (0 to {len(args.files)-1})")
                exit(1)
        
        # Open all files and keep references
        root_files = []
        for file_path in args.files:
            root_file = ROOT.TFile.Open(file_path)
            if not root_file or root_file.IsZombie():
                print(f"Error opening {file_path}")
                exit(1)
            root_files.append(root_file)
            
        # Extract histograms from files
        x_title = ""
        y_title = ""
        
        print(f"Debug: Looking for {len(args.histograms)} histograms from {len(args.files)} files")
        for i, hist_name in enumerate(args.histograms):
            file_idx = file_indices[i]
            print(f"Debug: Getting histogram '{hist_name}' from file index {file_idx}")
            
            hist = root_files[file_idx].Get(hist_name)
            if not hist:
                print(f"Error: Histogram '{hist_name}' not found in {args.files[file_idx]}")
                continue
                
            # Clone histogram to keep it after files close
            hist_clone = hist.Clone(f"{hist_name}_{i}")
            hist_clone.SetDirectory(0)
            histograms.append(hist_clone)
            
            # Get axis titles from first histogram
            if len(histograms) == 1:
                x_title = hist_clone.GetXaxis().GetTitle() if hist_clone.GetXaxis().GetTitle() else "X-axis"
                y_title = hist_clone.GetYaxis().GetTitle() if hist_clone.GetYaxis().GetTitle() else "Y-axis"
                
            # Use provided legends or fallback to histogram name
            if args.legends and i < len(args.legends):
                legends.append(args.legends[i])
            else:
                legends.append(hist_name)
                
        # Close files
        for root_file in root_files:
            root_file.Close()
            
        if not histograms:
            print("Error: No valid histograms found")
            exit(1)
            
        # Debug histogram information
        print(f"Debug: Successfully loaded {len(histograms)} histograms")
        for i, (hist, legend) in enumerate(zip(histograms, legends)):
            print(f"  [{i}] {legend}: {hist.GetName()}")
            
        # Generate output filename
        output_filename = f"{args.prefix}.png"
        output_path = os.path.join(args.output_dir, output_filename)
        
        # Check if ratio plot is requested
        if args.ratio:
            # Make sure ratio indices are valid
            num_idx, denom_idx = args.ratio_indices
            
            print(f"Debug: Ratio indices requested: {num_idx}, {denom_idx}")
            print(f"Debug: Number of available histograms: {len(histograms)}")
            
            if num_idx < 0 or num_idx >= len(histograms) or denom_idx < 0 or denom_idx >= len(histograms):
                print(f"Error: Invalid ratio indices {num_idx}, {denom_idx}. Valid range is 0 to {len(histograms)-1}")
                exit(1)
                
            # Create plot with ratio panel
            make_comparison_plot_with_ratio(
                histograms, 
                "Comparison", 
                x_title, 
                y_title, 
                output_path, 
                legends, 
                args.ratio_indices, 
                args.ratio_label, 
                False, 
                False
            )
        else:
            # Create standard comparison plot
            make_comparison_plot(
                histograms, 
                "Comparison", 
                x_title, 
                y_title, 
                output_path, 
                legends, 
                False, 
                False
            )
    
    # Handle other modes
    # For multiple files comparison (standard comparison of same histogram across files)
    elif args.files and len(args.files) > 1 and not args.histograms:
        # Histogram configurations: (name, title, x_title, y_title, normalize, log_y)
        hist_configs = [
            ("h_genpt_all", "Gen  p_{T}", "p_{T} [GeV]", "Number of Gen muons", False, False),
            ("h_genpt", "Gen  p_{T}", "p_{T} [GeV]", "Number of Gen muons", False, False),
            ("h_geneta", "Gen #eta", "#eta", "Number of Gen muons", False, False),
            ("h_genlxy", "Gen $L_{xy}$", "$L_{xy}$", "Number of Gen muons", False, False),
            ("h_genpt_dsa", "Gen  p_{T}", "p_{T} [GeV]", "Number of Gen muons matched to dsa", False, False),
            ("h_geneta_dsa", "Gen #eta", "#eta", "Number of Gen muons matched to dsa", False, False),
            ("h_genpt_dgb", "Gen  p_{T}", "p_{T} [GeV]", "Number of Gen muons matched to dgm", False, False),        
            ("h_geneta_dgb", "Gen #eta", "#eta", "Number of Gen muons matched to dgm", False, False),
            ("h_multiplicity_all", "Displaced Global Muon Multiplicity", "Number of Displaced Global Muons (before matching)", "Events", False, False),
            ("h_multiplicity", "Displaced Global Muon Multiplicity", "Number of Displaced Global Muons", "Events", False, False),
            ("h_pt", "Displaced Global Muon p_{T}", "p_{T} [GeV]", "Number of Displaced Global Muons", False, False),
            ("h_eta", "Displaced Global Muon #eta", "#eta", "Number of Displaced Global Muons", False, False),
            ("h_d0", "Displaced Global Muon d0", "d0 [cm]", "Number of Displaced Global Muons", False, True),
            ("h_pt_dtk", "Displaced Track p_{T}", "p_{T} [GeV]", "Number of Displaced Tracks", False, False),
            ("h_dr_dtk", "Displaced Track #Delta R(dgb, dtk)", "#Delta R(dgb, dtk)", "Number of Displaced Tracks", False, False),
            ("h_algo_dtk", "Displaced Track algo", "algo", "Number of Displaced Global Muons", False, False),
            ("h_originalAlgo_dtk", "Displaced Track original Algo", "original Algo", "Number of Displaced Global Muons", False, False),
            ("h_pt_dsa", "Displaced StandAlone p_{T}", "p_{T} [GeV]", "Number of Displaced StandAlone Muons", False, False),
            ("h_dr_dsa", "Displaced StandAlone #Delta R(dgb, dsa)", "#Delta R(dgb, dsa)", "Number of Displaced StandAlone Muons", False, False),
            ("h_pt_earlyOuter", "Early Outer p_{T}", "p_{T} [GeV]", "Number of Early Outer Muons", False, False),
            ("h_dr_earlyOuter", "Early Outer #Delta R(dgb, earlyOuter)", "#Delta R(dgb, earlyOuter)", "Number of EarlyOuter Muons", False, False),
            ("h_pt_early", "Early p_{T}", "p_{T} [GeV]", "Number of Early Muons", False, False),
            ("h_dr_earlyOuter", "Early #Delta R(dgb, early)", "#Delta R(dgb, early)", "Number of Early Muons", False, False),
            ("h_nSeeds", "Number of Seeds", "Number of Seeds", "Entries", False, False)
        ]
        
        # Process each histogram type
        for hist_name, title, x_title, y_title, normalize, log_y in hist_configs:
            print(f"Processing histogram: {hist_name}")
            
            # Load histograms from all files
            hists = []
            for file_path in args.files:
                root_file = ROOT.TFile(file_path)
                if not root_file or root_file.IsZombie():
                    print(f"  Error opening {file_path}")
                    continue
                
                hist = root_file.Get(hist_name)
                if not hist:
                    print(f"  Histogram {hist_name} not found in {file_path}")
                    continue
                
                # Clone the histogram so it persists after file is closed
                hist_clone = hist.Clone(hist_name + "_" + str(len(hists)))
                hist_clone.SetDirectory(0)
                hists.append(hist_clone)
                root_file.Close()
            
            if not hists:
                print(f"  No valid histograms found for {hist_name}, skipping")
                continue
                
            # Generate output filename
            output_filename = f"{args.prefix}_{hist_name}.png"
            output_path = os.path.join(args.output_dir, output_filename)
            
            # Create and save comparison plot
            if args.ratio:
                make_comparison_plot_with_ratio(hists, title, x_title, y_title, output_path, args.legends, args.ratio_indices, args.ratio_label, normalize, log_y)
            else:
                make_comparison_plot(hists, title, x_title, y_title, output_path, args.legends, normalize, log_y)
    
    else:
        print("Invalid combination of arguments")
        exit(1)

if __name__ == "__main__":
    main()
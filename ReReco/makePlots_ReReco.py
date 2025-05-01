#!/usr/bin/env python3
import ROOT
import argparse
import os
import re

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)  # Turn off statistics box

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Compare histograms from multiple ROOT files')
    
    parser.add_argument('--files', '-f', type=str, nargs='+', required=True,
                       help='List of ROOT files containing histograms')
    
    parser.add_argument('--legends', '-l', type=str, nargs='+', default=None,
                       help='Legend entries for each file (same order as files)')
    
    parser.add_argument('--output-dir', '-o', type=str, default='comparison_plots',
                       help='Output directory for plots (default: comparison_plots)')
    
    parser.add_argument('--prefix', '-p', type=str, default='comparison',
                       help='Prefix for output filenames')
    
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
    
    # Ensure legends match number of files
    if len(args.legends) != len(args.files):
        print(f"Error: Number of legend entries ({len(args.legends)}) doesn't match number of files ({len(args.files)})")
        exit(1)
    
    return args

def make_comparison_plot(hists, title, x_title, y_title, output_path, legends, normalize=False, log_y=False):
    """Create a plot comparing multiple histograms"""
    canvas = ROOT.TCanvas("c", title, 800, 600)
    
    if log_y:
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
        
        draw_option = "HIST" if i == 0 else "HIST SAME"
        hist.Draw(draw_option)
        
        #legend.AddEntry(hist, legend_text, "l")
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

def main():
    args = parse_args()
    
    # Create output directory
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Histogram configurations: (name, title, x_title, y_title, normalize, log_y)
    hist_configs = [
        ("h_multiplicity_preselection", "Displaced Global Muon Multiplicity", "Number of Displaced Global Muons (before matching)", "Events", False, False),
        ("h_multiplicity", "Displaced Global Muon Multiplicity", "Number of Displaced Global Muons", "Events", False, False),
        ("h_pt", "Displaced Global Muon p_{T}", "p_{T} [GeV]", "Number of Displaced Global Muons", False, False),
        ("h_eta", "Displaced Global Muon #eta", "#eta", "Number of Displaced Global Muons", False, False),
        ("h_d0", "Displaced Global Muon d0", "d0 [cm]", "Number of Displaced Global Muons", False, True),
        ("h_algo", "Displaced Track algo", "algo", "Number of Displaced Global Muons", False, False)
        ("h_originalAlgo", "Displaced Track original Algo", "original Algo", "Number of Displaced Global Muons", False, False)
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
        make_comparison_plot(hists, title, x_title, y_title, output_path, args.legends, normalize, log_y)

if __name__ == "__main__":
    main()
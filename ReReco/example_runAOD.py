import ROOT
import argparse
import os

ROOT.gROOT.SetBatch(True)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process RECO file and display particle information')
parser.add_argument('--input', '-i', type=str, default='ReReco_chi2_60.0_disp_0.5_sag_2.0_sig_3.root', help='Input ROOT file path')
parser.add_argument('-o', '--output', type=str, default=None, help='Output ROOT file for histograms (default: derived from input)')
args = parser.parse_args()

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.gSystem.Load("libDataFormatsFWLite.so")
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

# Gen sim collections
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")

# Displaced global muons collection
handleDisplacedMuons = Handle("std::vector<reco::Track>")
labelDisplacedMuons = ("displacedGlobalMuons", "", "RECO")

# Check if input file exists
if not os.path.exists(args.input):
    print(f"Error: Input file '{args.input}' not found.")
    exit(1)

print(f"Opening file: {args.input}")
events = Events(args.input)
total_events = events.size()
total_muons = 0
print(f"Total events in file: {total_events}")

# Prepare output filenames
base_filename = os.path.splitext(os.path.basename(args.input))[0]
if args.output is None:
    args.output = f"plots/{base_filename}_histograms.root"

# Create output directory for plots (if it does not exist)
plots_dir = f"plots/{base_filename}"
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Create histograms for basic checks
h_multiplicity = ROOT.TH1F("h_multiplicity", "Displaced Global Muon Multiplicity", 8, 0, 8)
h_multiplicity.GetXaxis().SetTitle("Number of Displaced Global Muons")
h_multiplicity.GetYaxis().SetTitle("Events")

h_pt = ROOT.TH1F("h_pt", "Displaced Global Muon p_{T}", 100, 0, 100)
h_pt.GetXaxis().SetTitle("p_{T} [GeV]")
h_pt.GetYaxis().SetTitle("Entries")

h_eta = ROOT.TH1F("h_pt", "Displaced Global Muon #eta", 30, -2.5, 2.5)
h_eta.GetXaxis().SetTitle("#eta ")
h_eta.GetYaxis().SetTitle("Entries")

for i,event in enumerate(events):
    
    # print the event number
    print("=="*80)
    print("event number: ", i)

    # get the pruned gen particles
    event.getByLabel(labelPruned, handlePruned)
    genParticles = handlePruned.product()

    # loop over the pruned gen particles
    for i, genParticle in enumerate(genParticles):
        # print the interesting particles
        if abs(genParticle.pdgId()) == 13 or abs(genParticle.pdgId()) == 1000013 or abs(genParticle.pdgId()) == 2000013:
            if genParticle.isLastCopy() == True:
                # print the interesting particles
                print("Gen Particle: ", i)
                print("  pdgId: ", genParticle.pdgId())
                print("  status: ", genParticle.status())
                print("  pt: ", genParticle.pt())
                print("  eta: ", genParticle.eta())
                print("  phi: ", genParticle.phi())
                print("  mass: ", genParticle.mass())
                print("  charge: ", genParticle.charge())
                print("  number of daughters: ", genParticle.numberOfDaughters())

    print("=="*80)

    # try to get the displaced global muons (and count them)
    muon_count = 0
    try:
        event.getByLabel(labelDisplacedMuons, handleDisplacedMuons)
        displacedMuons = handleDisplacedMuons.product()

        # dGB multiplicity
        print(f"\nDisplaced Global Muons: {displacedMuons.size()}")
        h_multiplicity.Fill(displacedMuons.size())

        # Loop over the displaced global muon tracks
        for j, track in enumerate(displacedMuons):
            print(f"  Track {j}:")
            print(f"    pT: {track.pt():.2f} GeV")
            print(f"    eta: {track.eta():.2f}")
            print(f"    phi: {track.phi():.2f}")
            print(f"    chi2/ndof: {track.normalizedChi2():.2f}")
            print(f"    hits: {track.numberOfValidHits()}")

            # Fill displaced global muon pT histogram
            h_pt.Fill(track.pt())
            h_eta.Fill(track.eta())

            # Counters
            muon_count += 1
            total_muons += 1

    except Exception as e:
        print(f"Error accessing displaced global muons: {e2}")

# Print summary
print(f"Processed {i+1} events, found {muon_count} displaced global muons")
print(f"Average muons per event: {muon_count/(i+1):.2f}")

# Save histograms to ROOT file
output_root = ROOT.TFile(args.output, "RECREATE")
h_multiplicity.Write()
h_pt.Write()
h_eta.Write()
output_root.Close()
print(f"Histograms saved to {args.output}")

# Create and save multiplicity plot
c_mult = ROOT.TCanvas("c_mult", "Displaced Global Muon Multiplicity", 800, 600)
h_multiplicity.SetFillColor(ROOT.kBlue-7)
h_multiplicity.SetLineColor(ROOT.kBlue+2)
h_multiplicity.Draw("hist")
c_mult.SaveAs(f"{plots_dir}/muon_multiplicity.png")
c_mult.SaveAs(f"{plots_dir}/muon_multiplicity.pdf")

# Create and save pT plot
c_pt = ROOT.TCanvas("c_pt", "Displaced Global Muon $p_{T}$", 800, 600)
h_pt.SetFillColor(ROOT.kRed-7)
h_pt.SetLineColor(ROOT.kRed+2)
h_pt.Draw("hist")
c_pt.SaveAs(f"{plots_dir}/muon_pT.png")
c_pt.SaveAs(f"{plots_dir}/muon_pT.pdf")

# Create and save pT plot
c_eta = ROOT.TCanvas("c_eta", "Displaced Global Muon #eta", 800, 600)
h_eta.SetFillColor(ROOT.kRed-7)
h_eta.SetLineColor(ROOT.kRed+2)
h_eta.Draw("hist")
c_eta.SaveAs(f"{plots_dir}/muon_eta.png")
c_eta.SaveAs(f"{plots_dir}/muon_eta.pdf")

import ROOT
import argparse
import os
import math
import genUtils as gu

ROOT.gROOT.SetBatch(True)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process RECO file and display particle information')
parser.add_argument('--input', '-i', type=str, default='', help='Input ROOT file path')
parser.add_argument('--samples', '-s', type=str, default='/pnfs/ciemat.es/data/cms/store/user/escalant/displacedGlobalMuon_ReReco', help='Directory where ReReco samples are stored')
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

# Displaced tracks collection
handleDisplacedTracks = Handle("std::vector<reco::Track>")
labelDisplacedTracks = ("displacedTracks", "", "RECO")

# Check if input file exists
inputFile = os.path.join(args.samples, args.input)
if not os.path.exists(inputFile):
    print(f"Error: Input file '{inputFile}' not found.")
    exit(1)

print(f"Opening file: {inputFile}")
events = Events(inputFile)
total_events = events.size()
print(f"Total events in file: {total_events}")

# counters to check that what I process in the event loop
event_count = 0 
total_muons = 0

# Prepare output filenames
base_filename = os.path.splitext(os.path.basename(args.input))[0]
if args.output is None:
    args.output = f"plots/{base_filename}_histograms.root"

# Create output directory for plots (if it does not exist)
plots_dir = f"plots/{base_filename}"
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# wrapper to create the histograms
def create_histogram(name, title, nbins, xmin, xmax, x_title, y_title):
    """
    Create a histogram with consistent styling
    
    Parameters:
    - name: Name of the histogram
    - title: Title of the histogram
    - nbins: Number of bins
    - xmin: Minimum x-axis value
    - xmax: Maximum x-axis value
    - x_title: X-axis title
    - y_title: Y-axis title
    
    Returns:
    - ROOT.TH1F: Configured histogram
    """
    hist = ROOT.TH1F(name, title, nbins, xmin, xmax)
    hist.GetXaxis().SetTitle(x_title)
    hist.GetYaxis().SetTitle(y_title)
    return hist

# Create histograms for basic checks
h_multiplicity_preselection = create_histogram("h_multiplicity_preselection", "Displaced Global Muon Multiplicity", 8, 0, 8, "Number of Displaced Global Muons (before matching)", "Events")
h_multiplicity = create_histogram("h_multiplicity", "Displaced Global Muon Multiplicity", 8, 0, 8, "Number of Displaced Global Muons", "Events")
h_pt = create_histogram("h_pt", "Displaced Global Muon p_{T}", 50, 0, 200, "p_{T} [GeV]", "Entries")
h_eta = create_histogram("h_eta", "Displaced Global Muon #eta", 15, -2.5, 2.5, "#eta", "Entries")
h_d0 = create_histogram("h_d0", "Displaced Global Muon d0", 65, 0, 65, "d0 [cm]", "Entries")  
h_algo = create_histogram("h_algo", "Displaced Track algo", 20, 0, 20, "algo", "Entries")
h_originalAlgo = create_histogram("h_originalAlgo", "Displaced Track algo", 20, 0, 20, "originalAlgo", "Entries")
h_genlxy = create_histogram("h_genlxy", "Generated Lxy", 250, 0, 500, "L_{xy} [cm]", "Entries")
h_genlxy_filter = create_histogram("h_genlxy_filter", "Generated Lxy", 100, 0, 100, "L_{xy} [cm]", "Entries")

# loop over the events and fill the histograms
for j,event in enumerate(events):
    print("=="*80)

    # print the event number
    event_count += 1
    print("event number: ", j)

    # get the pruned gen particles
    event.getByLabel(labelPruned, handlePruned)
    genParticles = handlePruned.product()

    # store the generated level muons
    genMuonsList = []

    # loop over the pruned gen particles
    for i, genParticle in enumerate(genParticles):
        # print the interesting particles
        goodSMuon = False
        goodMuon = False
        if (abs(genParticle.pdgId()) == 1000013 or abs(genParticle.pdgId()) == 2000013) and genParticle.isLastCopy() == True: goodSMuon = True
        if (abs(genParticle.pdgId()) == 13) and genParticle.fromHardProcessFinalState() == True: goodMuon = True
        
        if goodSMuon == True or goodMuon == True:
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
            print("  vx: ", genParticle.vx())
            print("  vy: ", genParticle.vy())
            print("  Lxy: ", math.hypot(genParticle.vx(), genParticle.vy()))

            # save the muons
            if abs(genParticle.pdgId()) == 13:
                genMuonsList.append(genParticle)
                gen_lxy = math.hypot(genParticle.vx(), genParticle.vy())
                print("  Lxy: ", gen_lxy)
                h_genlxy.Fill(gen_lxy)

    if len(genMuonsList) != 2:
        print("Skipping event, not 2 muons; Why?")
        import pdb
        pdb.set_trace()
    
    print("=="*80)

    # get the reconstructed muons    
    event.getByLabel(labelDisplacedMuons, handleDisplacedMuons)
    event.getByLabel(labelDisplacedTracks, handleDisplacedTracks)

    displacedMuons = handleDisplacedMuons.product()
    displacedTracks = handleDisplacedTracks.product()

    # try to get the displaced global muons (and count them)
    muon_count = 0

    # dGB multiplicity
    print(f"\nDisplaced Global Muons: {displacedMuons.size()}")
    h_multiplicity_preselection.Fill(displacedMuons.size())

    # Loop over the displaced global muon tracks
    for j, dgmu in enumerate(displacedMuons):

        # is interesting muon?
        if gu.isInterestingMuon(dgmu, genMuonsList) == False: continue # skip the reco if its not matched to a gen-muon

        # displaced global muon info
        print(f"  DisplacedGlobalMuon {j}:")
        print(f"    pT: {dgmu.pt():.3f} GeV")
        print(f"    eta: {dgmu.eta():.3f}")
        print(f"    phi: {dgmu.phi():.3f}")
        print(f"    d0 (cm): {dgmu.d0():.4f} ")
        print(f"    dxy (cm): {dgmu.dxy():.4f} ")
        print(f"    chi2/ndof: {dgmu.normalizedChi2():.2f}")
        print(f"    hits: {dgmu.numberOfValidHits()}")
        print(f"    algo: {dgmu.algo()}") # the algos are not available for diplaced global muons. Why?
        print(f"    originalAlgo: {dgmu.originalAlgo()}") 
        print(f"    algoName: {dgmu.algoName()}") 

        # Fill displaced global muon pT histogram
        h_pt.Fill(dgmu.pt())
        h_eta.Fill(dgmu.eta())
        h_d0.Fill(abs(dgmu.d0()))

        # Fill the generated Lxy histogram for the actual muons used in the analysis
        for genMuon in genMuonsList:
            h_genlxy_filter.Fill(math.hypot(genMuon.vx(), genMuon.vy()))

        # is matched to a good displaced track?
        for k, dtrack in enumerate(displacedTracks):
            if gu.deltaR(dgmu, dtrack) < 0.2:
                print(f"  DisplacedTrack {k}:")
                print(f"    pT: {dtrack.pt():.3f} GeV")
                print(f"    eta: {dtrack.eta():.3f}")
                print(f"    phi: {dtrack.phi():.3f}")
                print(f"    d0 (cm): {dtrack.d0():.4f} ")
                print(f"    dxy (cm): {dtrack.dxy():.4f} ")
                print(f"    chi2/ndof: {dtrack.normalizedChi2():.2f}")
                print(f"    hits: {dtrack.numberOfValidHits()}")
                print(f"    algo: {dtrack.algo()}")
                print(f"    originalAlgo: {dtrack.originalAlgo()}")
                print(f"    algoName: {dtrack.algoName()}")
                h_algo.Fill(dtrack.algo()) 
                h_originalAlgo.Fill(dtrack.originalAlgo()) 
                
        # Counters
        muon_count += 1
        total_muons += 1

    # actual muon multiplicity/event used in the analysis
    h_multiplicity.Fill(muon_count)

# Print summary
print(f"Processed {event_count}/{total_events} events, found {total_muons} displaced global muons")

# output ROOT file
output_root = ROOT.TFile(args.output, "RECREATE")

# make the plots 
def create_and_save_plot(histogram, output_root, output_dir, color=ROOT.kRed):
    """
    Create and save a plot for a histogram
    
    Parameters:
    - histogram: The histogram to plot
    - output_dir: Directory to save the plot
    - color: ROOT color for the histogram (default: kRed)
    """
    # get the histogram name and use it as output filename
    histogram_name = histogram.GetName()
    filename_base = histogram_name.replace("h_", "")

    # Create canvas and set histogram style
    canvas = ROOT.TCanvas(f"c_{filename_base}", histogram.GetTitle(), 800, 600)
    histogram.SetFillColor(color-7)
    histogram.SetLineColor(color+2)
    histogram.Draw("hist")

    # Save the plot in different formats
    canvas.SaveAs(f"{output_dir}/{filename_base}.png")
    canvas.SaveAs(f"{output_dir}/{filename_base}.pdf")
    print(f"Saved plot: {output_dir}/{filename_base}.png")

    # Save the histograms to the ROOT file
    histogram.Write()

# Create and save all plots
create_and_save_plot(h_multiplicity_preselection, output_root, plots_dir, ROOT.kBlue)
create_and_save_plot(h_multiplicity, output_root, plots_dir, ROOT.kBlue)
create_and_save_plot(h_pt, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_eta, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_d0, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_algo, output_root, plots_dir, ROOT.kGreen)
create_and_save_plot(h_originalAlgo, output_root, plots_dir, ROOT.kGreen)
create_and_save_plot(h_genlxy, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_genlxy_filter, output_root, plots_dir, ROOT.kOrange)

# Close the output ROOT file
output_root.Close()
print(f"Histograms saved in {args.output} file")
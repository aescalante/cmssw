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

# Early displaced muons collection 
handleEarlyDisplacedMuons = Handle("vector<reco::Muon>")
labelEarlyDisplacedMuons = ("earlyDisplacedMuons", "", "RECO")

# Displaced stand alone muons collection 
handleDisplacedStandAloneMuons = Handle("vector<reco::Track>")
labelDisplacedStandAloneMuons = ("displacedStandAloneMuons", "", "RECO")

# Seeds
handleSeeds = Handle("vector<TrajectorySeed>")
labelSeeeds = ("muonSeededSeedsOutInDisplaced", "", "RECO")

# Displaced tracks collection
handleDisplacedTracks = Handle("std::vector<reco::Track>")
labelDisplacedTracks = ("displacedTracks", "", "RECO")

# OutInTracks
handleOutInTracks = Handle("vector<reco::Track>")
labelOutInTracks = ("muonSeededTracksOutInDisplaced", "", "RECO")

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

# gen level
h_genlxy_all= create_histogram("h_genlxy_all", "Generated Lxy", 250, 0, 500, "L_{xy} [cm]", "Entries")
h_genpt_all= create_histogram("h_genpt_all", "Generated muon pT ", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_geneta_all= create_histogram("h_geneta_all", "Generated muon #eta ", 15, -2.5, 2.5, "#eta", "Entries")
h_genlxy = create_histogram("h_genlxy", "Generated Lxy", 100, 0, 100, "L_{xy} [cm]", "Entries")
h_genpt = create_histogram("h_genpt", "Generated muon pT ", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_geneta = create_histogram("h_geneta", "Generated muon #eta", 15, -2.5, 2.5, "#eta", "Entries")
h_genpt_dsa = create_histogram("h_genpt_dsa", "Generated muon pT (matched to dsa)", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_geneta_dsa = create_histogram("h_geneta_dsa", "Generated muon #eta (matched to dsa)", 15, -2.5, 2.5, "#eta", "Entries")
h_genpt_dgb = create_histogram("h_genpt_dgb", "Generated muon pT (matched to dgm)", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_geneta_dgb = create_histogram("h_geneta_dgb", "Generated muon #eta (matched to dgm)", 15, -2.5, 2.5, "#eta", "Entries")

# reco level
h_multiplicity_all = create_histogram("h_multiplicity_all", "Displaced Global Muon Multiplicity", 8, 0, 8, "Number of Displaced Global Muons (before matching)", "Events")
h_multiplicity = create_histogram("h_multiplicity", "Displaced Global Muon Multiplicity", 8, 0, 8, "Number of Displaced Global Muons", "Events")
h_pt = create_histogram("h_pt", "Displaced Global Muon p_{T}", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_eta = create_histogram("h_eta", "Displaced Global Muon #eta", 15, -2.5, 2.5, "#eta", "Entries")
h_d0 = create_histogram("h_d0", "Displaced Global Muon d0", 65, 0, 65, "d0 [cm]", "Entries")  
h_algo_dtk = create_histogram("h_algo_dtk", "Displaced Track algo", 20, 0, 20, "algo", "Entries")
h_originalAlgo_dtk = create_histogram("h_originalAlgo_dtk", "Displaced Track algo", 20, 0, 20, "originalAlgo", "Entries")
h_pt_dtk = create_histogram("h_pt_dtk", "Displaced Track p_{T}", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_dr_dtk = create_histogram("h_dr_dtk", "dR(dgb, dtk)", 40, 0, 0.5, "#Delta R", "Entries")
h_pt_dsa = create_histogram("h_pt_dsa", "Displaced StandAlone ", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_dr_dsa = create_histogram("h_dr_dsa", "dR(dgb, dsa)", 40, 0, 0.5, "#Delta R", "Entries")
h_pt_earlyOuter = create_histogram("h_pt_earlyOuter", "Early Outer ", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_dr_earlyOuter = create_histogram("h_dr_earlyOuter", "dR(dgb, earlyOuter)", 40, 0, 0.5, "#Delta R", "Entries")
h_pt_early = create_histogram("h_pt_early", "Early ", 40, 0, 200, "p_{T} [GeV]", "Entries")
h_dr_early = create_histogram("h_dr_early", "dR(dgb, early)", 40, 0, 0.5, "#Delta R", "Entries")
h_nSeeds = create_histogram("h_nSeeds", "Number of Seeds", 30, 0, 30, "Number of Seeds", "Entries")

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
                h_genlxy_all.Fill(gen_lxy)
                h_genpt_all.Fill(genParticle.pt())
                h_geneta_all.Fill(genParticle.eta())

    if len(genMuonsList) != 2:
        print("Skipping event, not 2 muons; Why?")
        import pdb
        pdb.set_trace()
    
    print("=="*80)

    # get the reconstructed muons (dgb, early, dsa), seeds and tracks (outin, displacedTracks)
    event.getByLabel(labelDisplacedMuons, handleDisplacedMuons)
    event.getByLabel(labelEarlyDisplacedMuons, handleEarlyDisplacedMuons)
    event.getByLabel(labelDisplacedStandAloneMuons, handleDisplacedStandAloneMuons)
    event.getByLabel(labelSeeeds, handleSeeds)
    event.getByLabel(labelOutInTracks, handleOutInTracks)
    event.getByLabel(labelDisplacedTracks, handleDisplacedTracks)

    displacedMuons = handleDisplacedMuons.product()
    displacedTracks = handleDisplacedTracks.product()
    earlyDisplacedMuons = handleEarlyDisplacedMuons.product()
    displacedStandAloneMuons = handleDisplacedStandAloneMuons.product()
    seeds = handleSeeds.product()
    outInTracks = handleOutInTracks.product()
    displacedTracks = handleDisplacedTracks.product()
    
    # try to get the displaced global muons (and count them)
    muon_count = 0

    # dGB multiplicity
    print(f"\nDisplaced Global Muon multiplicity: {displacedMuons.size()}")
    h_multiplicity_all.Fill(displacedMuons.size())

    # get interesting gen muons for further analysis
    genMuonsAnalysis = gu.getInterestingGenMuons(genMuonsList)
    if len(genMuonsAnalysis) == 0: continue # skip the event if there are no interesting gen muons

    # Fill the generated Lxy histogram for the actual muons used in the analysis
    for genMuon in genMuonsAnalysis:
        h_genlxy.Fill(math.hypot(genMuon.vx(), genMuon.vy()))
        h_genpt.Fill(genMuon.pt())
        h_geneta.Fill(genMuon.eta())

    # Loop over displaced stand alone muons
    for j, dsa in enumerate(displacedStandAloneMuons):
        # check if the dsa is matched to a gen
        gen_dsa_index = gu.getGenMuonIndex(dsa, genMuonsAnalysis)
        if gen_dsa_index > -1:
            genMuon_dsa = genMuonsAnalysis[gen_dsa_index]
            h_genpt_dsa.Fill(genMuon_dsa.pt())
            h_geneta_dsa.Fill(genMuon_dsa.eta())

    # Loop over the displaced global muon tracks
    for j, dgmu in enumerate(displacedMuons):
        # check if the dgb is matched to a gen
        gen_dgm_index = gu.getGenMuonIndex(dgmu, genMuonsAnalysis)
        if gen_dgm_index > -1:
            genMuon_dgm = genMuonsAnalysis[gen_dgm_index]
            h_genpt_dgb.Fill(genMuon_dgm.pt())
            h_geneta_dgb.Fill(genMuon_dgm.eta())

        # displaced global muon block
        print(f"  DisplacedGlobalMuon {j}/{len(displacedMuons)}:")
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

        # Fill displaced global muon histograms
        h_pt.Fill(dgmu.pt())
        h_eta.Fill(dgmu.eta())
        h_d0.Fill(abs(dgmu.d0()))

        # is it matched to a good displaced track?
        for k, dtrack in enumerate(displacedTracks):
            if gu.deltaR(dgmu, dtrack) < 0.015: # tight matching
                print(f"  DisplacedTrack {k}/{len(displacedTracks)}:")
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
                h_algo_dtk.Fill(dtrack.algo()) 
                h_originalAlgo_dtk.Fill(dtrack.originalAlgo()) 
                h_pt_dtk.Fill(dtrack.pt())
                h_dr_dtk.Fill(gu.deltaR(dgmu, dtrack))
        
        # is matched to a dsa?
        for k, dsa in enumerate(displacedStandAloneMuons):
            if gu.deltaR(dgmu, dsa) < 0.3:
                print(f"  DisplacedStandAloneMuon {k}/{len(displacedStandAloneMuons)}:")
                print(f"    pT: {dsa.pt():.3f} GeV")
                print(f"    eta: {dsa.eta():.3f}")
                print(f"    phi: {dsa.phi():.3f}")
                print(f"    d0 (cm): {dsa.d0():.4f} ")
                print(f"    dxy (cm): {dsa.dxy():.4f} ")
                print(f"    chi2/ndof: {dsa.normalizedChi2():.2f}")
                print(f"    hits: {dsa.numberOfValidHits()}")
                print(f"    algo: {dsa.algo()}")
                print(f"    originalAlgo: {dsa.originalAlgo()}")
                print(f"    algoName: {dsa.algoName()}")
                h_pt_dsa.Fill(dsa.pt())
                h_dr_dsa.Fill(gu.deltaR(dgmu, dsa))
        
        # is it matched to an early muon?
        for k, early in enumerate(earlyDisplacedMuons):
            earlyOuter = early.outerTrack()
            earlyInner = early.innerTrack() # Somehow inner track is not working (not used below)
            if earlyOuter.isNull() == True: continue
            # Outer track needs to be available 
            if gu.deltaR(dgmu, earlyOuter) < 0.3:
                print(f"  EarlyDisplacedMuon {k}:{len(earlyDisplacedMuons)}:")
                print(f"    pT : {early.pt():.3f} GeV")
                print(f"    eta : {early.eta():.3f}")
                print(f"    phi : {early.phi():.3f}")
                print(f"    pT (outer): {earlyOuter.pt():.3f} GeV")
                print(f"    eta (outer): {earlyOuter.eta():.3f}")
                print(f"    phi (outer): {earlyOuter.phi():.3f}")
                #print(f"    pT (inner): {earlyInner.pt():.3f} GeV")
                #print(f"    eta (inner): {earlyInner.eta():.3f}")
                #print(f"    phi (inner): {earlyInner.phi():.3f}")
                h_pt_early.Fill(early.pt())
                h_dr_early.Fill(gu.deltaR(dgmu, early))
                h_pt_earlyOuter.Fill(earlyOuter.pt())
                h_dr_earlyOuter.Fill(gu.deltaR(dgmu, earlyOuter))

        # Counters
        muon_count += 1
        total_muons += 1

        # debug seeds    
        for i, seed in enumerate(seeds):
            print(f"debug seed:{i}/{len(seeds)}")
            recHitIt = seed.recHits().begin()
            recHitEnd = seed.recHits().end()
            hitCounter = 0
            if recHitIt != recHitEnd:
                if recHitIt.isValid() == True:
                    print(f"  recHitIt.isValid(): {recHitIt.isValid()}")
                    print(f"  recHitIt.getType(): {recHitIt.getType()}")
                    print(f"  recHitIt.localPosition(): {recHitIt.geographicalId().det()}")
                    print(f"  recHitIt.localPosition().x(): {recHitIt.localPosition().x()}")
                    print(f"  recHitIt.localPosition().y(): {recHitIt.localPosition().y()}")
                    print(f"  recHitIt.localPosition().z(): {recHitIt.localPosition().z()}")
                recHitIt += 1
                hitCounter += 1
            print("nHits: ", hitCounter)
        h_nSeeds.Fill(len(seeds))
        
        print("debug outInTracks")
        for i, outInTrack in enumerate(outInTracks):
            print(f"  outInTrack: {i}/{len(outInTracks)}:")
            print(f"    pT: {outInTrack.pt()}")
            print(f"    eta: {outInTrack.eta()}")
            print(f"    phi: {outInTrack.phi()}")

    # actual muon multiplicity/event used in the analysis
    h_multiplicity.Fill(muon_count)

    # end of the event
    #import pdb
    #pdb.set_trace()

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
create_and_save_plot(h_genlxy_all, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_genpt_all, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_geneta_all, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_genlxy, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_genpt, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_geneta, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_genpt_dsa, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_geneta_dsa, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_genpt_dgb, output_root, plots_dir, ROOT.kOrange)
create_and_save_plot(h_geneta_dgb, output_root, plots_dir, ROOT.kOrange)

create_and_save_plot(h_multiplicity_all, output_root, plots_dir, ROOT.kBlue)
create_and_save_plot(h_multiplicity, output_root, plots_dir, ROOT.kBlue)
create_and_save_plot(h_pt, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_eta, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_d0, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_algo_dtk, output_root, plots_dir, ROOT.kGreen)
create_and_save_plot(h_originalAlgo_dtk, output_root, plots_dir, ROOT.kGreen)
create_and_save_plot(h_pt_dtk, output_root, plots_dir, ROOT.kGreen)
create_and_save_plot(h_dr_dtk, output_root, plots_dir, ROOT.kGreen)
create_and_save_plot(h_pt_dsa, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_dr_dsa, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_pt_earlyOuter, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_dr_earlyOuter, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_pt_early, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_dr_early, output_root, plots_dir, ROOT.kRed)
create_and_save_plot(h_nSeeds, output_root, plots_dir, ROOT.kRed)

# Close the output ROOT file
output_root.Close()
print(f"Histograms saved in {args.output} file")
import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description='Configure a ReReco in the context of displaced muons')
parser.add_argument('--input', '-i', type=str, help='Input configuration file to modify the ReReco', required=True)
parser.add_argument('--MaxChi2', type=float, default=30., help='Max chi-squared value (default: 30)')
parser.add_argument('--MaxDisplacement', type=float, default=0.5, help='Max displacement value (default: 0.5)')
parser.add_argument('--MaxSagitta', type=float, default=2.0, help='Max sagitta value (default: 2)')
parser.add_argument('--nSigma', type=float, default=3, help='nSigma value (default: 5)')
parser.add_argument('--fromVertex', action='store_true', help='Impose a fromVertex requirement in muon seeding (default: True)')
parser.add_argument('--selection', type=str, help='change the seleciton on early displaced muons for seeding (default: pt > 10 && muonStationsWithValidHits >= 2)')
parser.add_argument('--run', action='store_true', help='Run cmsRun with the generated config file immediately')
parser.add_argument('--MaxEvents', '-n', type=int, default=-1, help='number of events to be processed (default: all events)')
parser.add_argument('--output', '-o', type=str, default='/pnfs/ciemat.es/data/cms/store/user/escalant/displacedGlobalMuon_ReReco', help='Output folder')
parser.add_argument('--postfix', '-p', type=str, default='', help='Add a postfix to the output file name (default: empty)')
parser.add_argument('--debug', action='store_true', help='Enable debugging mode (default: False)')

# Parse arguments
args = parser.parse_args()

# Generate a parameter suffix string to use in filenames
sampleID = args.input.replace('_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py', '')
param_suffix = f"{sampleID}_chi2_{args.MaxChi2}_disp_{args.MaxDisplacement}_sag_{args.MaxSagitta}_sig_{args.nSigma}"
if args.postfix:
    param_suffix += f"_{args.postfix}"
    
# output filenames
output_cfg = f"ReReco_{param_suffix}_cfg.py"
output_root = f"{args.output}/ReReco_{param_suffix}.root"

# load default configuration file
if args.input == "SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py":
    from SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff import *
if args.input == "SMuonToMuGravitino_M_900_ctau_500mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py":
    from SMuonToMuGravitino_M_900_ctau_500mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff import *

# modify the output file name
for module_name in process.outputModules_().keys():
    output_module = getattr(process, module_name)
    if hasattr(output_module, 'fileName'):
        original_name = output_module.fileName.value()
        output_type = ""
        
        # Extract the output type (like _AODSIM, _RECO, etc.)
        if "_" in os.path.basename(original_name):
            output_type = "_" + original_name.split("_")[-1].split(".")[0]
            
        output_module.fileName = cms.untracked.string(output_root)
        print(f"Updated output file:'{module_name}' to: {output_root}")
    else:
        print(f"Warning: Output module '{module_name}' does not have a 'fileName' attribute")

# configure the number of events to process
if args.MaxEvents > 0:
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(args.MaxEvents)
    )
    print(f"Configured to process {args.MaxEvents} events")

processes_to_check = []
# muon seeds for outside in algorithm (used for displaced muons)
processes_to_check.append('muonSeededSeedsOutInDisplaced')
# defining the search window for patter recognition
processes_to_check.append('muonSeededMeasurementEstimatorForOutInDisplaced')
# selections on the trajectories while building them
processes_to_check.append('muonSeededTrajectoryFilterForOutInDisplaced')
# Trajectory builder (using as input the previous steps)
processes_to_check.append('muonSeededTrajectoryBuilderForOutInDisplaced')
# Track candidate maker 
processes_to_check.append('muonSeededTrackCandidatesOutInDisplaced')

# test if the processes has the attributes that I wish to modify
for process_name in processes_to_check:
    if hasattr(process, process_name):
        print(f"✓ Found {process_name} as a process attribute")
        print(getattr(process, process_name))
    else:
        print(f"✗ Not found {process_name} as a process attribute")
        print(" Available attributes:")
        print(dir(process))
    
        # Check if it's included in any path or sequence
        print("\n Debugging Path definitions:")
        found_in_path = False
        for path_name, path in process.paths_().items():
            print(path_name)
            if process_name in str(path):
                print(f"✓ Found in path: {path_name}")
                found_in_path = True

        if not found_in_path:
            print("✗ Not found in any path")
            
            # start debugging
            import pdb
            pdb.set_trace()

# apply fromVertex in the muon seeding?
if args.fromVertex == True:
    process.muonSeededSeedsOutInDisplaced.fromVertex = True 
else:
    process.muonSeededSeedsOutInDisplaced.fromVertex = False

# change the selection on early displaced muons for seeding
if args.selection:
    process.muonSeededSeedsOutInDisplaced.cut = cms.string(args.selection)
    print("  changed muonSeededSeedsOutInDisplaced.cut to :", process.muonSeededSeedsOutInDisplaced.cut)

if args.debug == True:
    process.muonSeededSeedsOutInDisplaced.debug = True

print("use fromVertex in  constraint in muon seeding?")
print(process.muonSeededSeedsOutInDisplaced.fromVertex)

# Print the updated parameters
print("Updated parameters:")
if process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2 !=  args.MaxChi2:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2 = args.MaxChi2
    print("  changed MaxChi2 :", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2)

if process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement != args.MaxDisplacement:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement = args.MaxDisplacement
    print("  changed MaxDisplacement :", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement)

if process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta != args.MaxSagitta:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta = args.MaxSagitta
    print("  changed MaxSagitta :", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta)

if process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma != args.nSigma:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma = args.nSigma
    print("  changed nSigma :", process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma)

# add all the Displaced collections to the AOD output file, such that I can study them later (if neede)
collections_to_add = ["keep *_*Displaced*_*_*",]
for collection in collections_to_add:
    process.AODEventContent.outputCommands.append(collection)
    process.AODSIMEventContent.outputCommands.append(collection)
    process.AODSIMoutput.outputCommands.append(collection)

# Dump the full configuration to a file that can be used with cmsRun
print(f"\nDumping configuration to: {output_cfg}")
with open(output_cfg, 'w') as f:
    f.write(process.dumpPython())

# Instructions to run the code
print(f"You can run it (with --run option) to produce the output file {output_root}")

# Print the input files being used
print("\n The code will ReReco the following files (you might need a certificate to access them):")
if hasattr(process, 'source') and hasattr(process.source, 'fileNames'):
    for i, filename in enumerate(process.source.fileNames):
        print(f"  [{i}] {filename}")
else:
    print("  No input files found in the process source")

# Run cmsRun if requested as argument
if args.run:
    print(f"\nRunning: cmsRun {output_cfg}")
    print("=" * 80)
    
    # Use os.system to run cmsRun with the generated config file
    cmd = f"cmsRun {output_cfg}"
    exit_code = os.system(cmd)
    
    print("=" * 80)
    if exit_code == 0:
        print(f"✓ cmsRun completed successfully. Output saved to: {output_root}")
        
        # Check if the output file was actually created
        if os.path.exists(output_root):
            print(f"   Output file size: {os.path.getsize(output_root)/1024/1024:.2f} MB")
        else:
            print(f"   !! Warning !!: Output file {output_root} was not created!")
    else:
        # os.system returns the exit status code in a different format than subprocess
        # The actual exit code is in the high byte (exit_code >> 8)
        actual_code = exit_code >> 8
        print(f"✗ cmsRun failed with exit code {actual_code}")
else:
    print(f"\nTo run the job: cmsRun {output_cfg}")
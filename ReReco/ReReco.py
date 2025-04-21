import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Configure muonSeededMeasurementEstimatorForOutInDisplaced parameters')
parser.add_argument('--MaxChi2', type=float, default=30., help='Max chi-squared value (default: 30)')
parser.add_argument('--MaxDisplacement', type=float, default=0.5, help='Max displacement value (default: 0.5)')
parser.add_argument('--MaxSagitta', type=float, default=2.0, help='Max sagitta value (default: 2)')
parser.add_argument('--nSigma', type=float, default=3, help='nSigma value (default: 5)')

# Parse arguments
args = parser.parse_args()

# Generate a parameter suffix string to use in filenames
param_suffix = f"chi2_{args.MaxChi2}_disp_{args.MaxDisplacement}_sag_{args.MaxSagitta}_sig_{args.nSigma}"

# output filenames
output_cfg = f"ReReco_{param_suffix}_cfg.py"
output_root = f"ReReco_{param_suffix}.root"

# load default configuration file
from SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff import *

# Apply the ROOT output filename to the process
if hasattr(process, 'TFileService'):
    # If TFileService already exists, update its fileName parameter
    process.TFileService.fileName = cms.string(output_root)
else:
    # Create a new TFileService if it doesn't exist
    process.TFileService = cms.Service("TFileService", 
        fileName = cms.string(output_root)
    )

# test if the processes has the attributes that I wish to modify
print("Checking if muonSeededMeasurementEstimatorForOutInDisplaced is in the process:")
if hasattr(process, 'muonSeededMeasurementEstimatorForOutInDisplaced'):
    print("✓ Found as a process attribute")
    print(process.muonSeededMeasurementEstimatorForOutInDisplaced)

else:
    print("✗ Not found as a process attribute")
    print(" Available attributes:")
    print(dir(process))
    
    # Check if it's included in any path or sequence
    print("\n Debugging Path definitions:")
    found_in_path = False
    for path_name, path in process.paths_().items():
        print(path_name)
        if 'muonSeededMeasurementEstimatorForOutInDisplaced' in str(path):
            print(f"✓ Found in path: {path_name}")
            found_in_path = True

    if not found_in_path:
        print("✗ Not found in any path")
        
        # start debugging
        import pdb
        pdb.set_trace()

# Changing one configuration for testing
print("default: ")
print("  MaxChi2", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2)
print("  MaxDisplacement: ", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement)
print("  MaxSaggita: ", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta)
print("  nSigma:", process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma)

# Print the updated parameters
print("\n Updated parameters:")
if process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2 !=  args.MaxChi2:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2 = args.MaxChi2
    print("changed: MaxChi2 :", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2)

if process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement != args.MaxDisplacement:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement = args.MaxDisplacement
    print("changed: MaxDisplacement :", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement)

if process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta != args.MaxSagitta:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta = args.MaxSagitta
    print("changed: MaxSagitta :", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta)

if process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma != args.nSigma:
    process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma = args.nSigma
    print("changed: nSigma :", process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma)

# Dump the full configuration to a file that can be used with cmsRun
print(f"\nDumping configuration to: {output_cfg}")
with open(output_cfg, 'w') as f:
    f.write(process.dumpPython())

# instructions
print(f"You can now run: cmsRun {output_cfg} to produce the output file {output_root}")

print("\n The code will ReReco the following files (you might need a certificate to access them):")
# Print the input files being used
if hasattr(process, 'source') and hasattr(process.source, 'fileNames'):
    for i, filename in enumerate(process.source.fileNames):
        print(f"  [{i}] {filename}")
else:
    print("  No input files found in the process source")


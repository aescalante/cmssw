import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description='Configure muonSeededMeasurementEstimatorForOutInDisplaced parameters')
parser.add_argument('--MaxChi2', type=float, default=30., help='Max chi-squared value (default: 30)')
parser.add_argument('--MaxDisplacement', type=float, default=0.5, help='Max displacement value (default: 0.5)')
parser.add_argument('--MaxSagitta', type=float, default=2.0, help='Max sagitta value (default: 2)')
parser.add_argument('--nSigma', type=float, default=3, help='nSigma value (default: 5)')
parser.add_argument('--run', action='store_true', help='Run cmsRun with the generated config file immediately')

# Parse arguments
args = parser.parse_args()

# Generate a parameter suffix string to use in filenames
param_suffix = f"chi2_{args.MaxChi2}_disp_{args.MaxDisplacement}_sag_{args.MaxSagitta}_sig_{args.nSigma}"

# output filenames
output_cfg = f"ReReco_{param_suffix}_cfg.py"
output_root = f"ReReco_{param_suffix}.root"

# load default configuration file
from SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff import *

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

# test if the processes has the attributes that I wish to modify
print("Check if muonSeededMeasurementEstimatorForOutInDisplaced is in the process:")
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
print("Default: ")
print("  MaxChi2", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxChi2)
print("  MaxDisplacement: ", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxDisplacement)
print("  MaxSaggita: ", process.muonSeededMeasurementEstimatorForOutInDisplaced.MaxSagitta)
print("  nSigma:", process.muonSeededMeasurementEstimatorForOutInDisplaced.nSigma)

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

# Dump the full configuration to a file that can be used with cmsRun
print(f"\nDumping configuration to: {output_cfg}")
with open(output_cfg, 'w') as f:
    f.write(process.dumpPython())

# Instructions to run the code
print(f"You can now run: cmsRun {output_cfg} to produce the output file {output_root} (or use the --run option)")


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
# Rerun files for Jorge's study

First you need to setup (tested in `gaeui05`): `cmsset; cmssw-el7; exec bash`

__Setup intruction__

```bash
# source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel cmsrel CMSSW_12_4_21
cd CMSSW_12_4_21/src
git-cms-init
```

```bash
# needed to configure the muon reconstruction sequence
git cms-addpkg RecoMuon/Configuration 

# needed to touch the tracking
git cms-addpkg RecoTracker/IterativeTracking

# and commpile
scram b -j 8
```

```bash
# do the needed changes to the rereco (e.g change RecoMuon/Configuration/python/DisplacedMuonSeededStep_cff.py)
```

```bash
# setup the cmsDriver command to ReReco an AOD file
cmsDriver.py --python_filename SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:output_AODSIM.root --conditions 124X_mcRun3_2022_realistic_v12 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --geometry DB:Extended --filein root://cmsxrootd.fnal.gov///store/user/rlopezru/SMuonToMuGravitino_M_100_2000mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_105457/0000/output_PREMIXRAW_100.root --era Run3 --no_exec --mc -n 8 --nThreads 8

# then run it
# cmsRun SMuonToMuGravitino-M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py

# then run the ReReco command
python3 ReReco.py

# or changing one of the parameters
python3 ReReco.py --MaxChi2 60

# or changing one of the parameters and run the file
python3 ReReco.py --MaxChi2 60 --run

# run over one of the rerecoed files and make a plot of the dGB pT and multiplicity
python3 example_runAOD.py -i ReReco_chi2_60.0_disp_0.5_sag_2.0_sig_3.root
python3 example_runAOD.py -i ReReco_chi2_30.0_disp_0.5_sag_2.0_sig_3.root
python3 example_runAOD.py -i ReReco_chi2_2.0_disp_0.5_sag_2.0_sig_3.root
```
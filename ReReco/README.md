# Rerun files for Jorge's study

First you need to setup (tested in `gaeui05`): `cmsset; cmssw-el7; exec bash; cmsenv`

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
```

```bash
# do the needed changes to the rereco (e.g change RecoMuon/Configuration/python/DisplacedMuonSeededStep_cff.py)... So far nothing is needed and compile.
scram b -j 8
```

```bash
# idetify the relevant signal datasets with dasgoclient
# low mass sample
dasgoclient --query="dataset=/SMuonToMuGravitino_M_100_2000mm_13p6TeV_GENSIM_2022MC_v01/rlopezru-PREMIXRAW_v02-b722d1cf11a99a4476f09a94f34c768e/USER instance=prod/phys03"
# high mass sample
dasgoclient --query="dataset=/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/rlopezru-PREMIXRAW_v02-b722d1cf11a99a4476f09a94f34c768e/USER instance=prod/phys03"
# dump the files for the identified dataset into a .txt file
dasgoclient --query="file dataset=/SMuonToMuGravitino_M_100_2000mm_13p6TeV_GENSIM_2022MC_v01/rlopezru-PREMIXRAW_v02-b722d1cf11a99a4476f09a94f34c768e/USER instance=prod/phys03" >>  
SMuonToMuGravitino_M_100_2000mm_13p6TeV.txt
dasgoclient --query="file dataset=/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/rlopezru-PREMIXRAW_v02-b722d1cf11a99a4476f09a94f34c768e/USER instance=prod/phys03" >>  SMuonToMuGravitino_M_900_500mm_13p6TeV.txt
```

```bash
# setup the cmsDriver command to ReReco an AOD file 
cmsDriver.py --python_filename SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:output_AODSIM.root --conditions 124X_mcRun3_2022_realistic_v12 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --geometry DB:Extended --filein filelist:SMuonToMuGravitino_M_100_2000mm_13p6TeV.txt --era Run3 --no_exec --mc -n -1 --nThreads 8

cmsDriver.py --python_filename SMuonToMuGravitino_M_900_ctau_500mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:output_AODSIM.root --conditions 124X_mcRun3_2022_realistic_v12 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --geometry DB:Extended --filein filelist:SMuonToMuGravitino_M_900_500mm_13p6TeV.txt --era Run3 --no_exec --mc -n -1 --nThreads 8

# then run the ReReco command over 1000 events
python3 ReReco.py -i SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py -n 1000 

# or changing one of the parameters
python3 ReReco.py -i SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py --MaxChi2 60 -n 1000

# or changing one of the parameters and run the file
python3 ReReco.py -i SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py --MaxChi2 60 -n 1000 --run 

# run over one of the rerecoed files and make a plot of the dGB pT and multiplicity (it assumes aod samples are in /pnfs/ciemat.es/data/cms/store/user/escalant/displacedGlobalMuon_ReReco)
python3 makeHistograms_ReReco.py -i ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_0.01_disp_0.5_sag_2.0_sig_3.root # debug
python3 makeHistograms_ReReco.py -i ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.01_sag_2.0_sig_3.root # debug

python3 makeHistograms_ReReco.py -i ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_15.0_disp_0.5_sag_2.0_sig_3.root
python3 makeHistograms_ReReco.py -i ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3.root
python3 makeHistograms_ReReco.py -i ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_120.0_disp_0.5_sag_2.0_sig_3.root

# run over a .sh script with all configurations (might be worth using the batch system)
source submit_ReReco.sh
```
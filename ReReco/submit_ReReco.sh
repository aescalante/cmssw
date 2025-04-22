#!/bin/bash
# This script is used to run the ReReco.py script with different parameters
# and then create histograms using the makeHistograms_ReReco.py script.
# The script takes the following parameters:
NEVENTS=100
INPUTDIR=/pnfs/ciemat.es/data/cms/store/user/escalant/displacedGlobalMuon_ReReco/
SAMPLE=SMuonToMuGravitino_M_100_ctau_2000mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py
#SAMPLE = SMuonToMuGravitino_M_900_ctau_500mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py
SAMPLE_RERECO="ReReco_${SAMPLE/_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py/}"

DO_REREC=false
if [ "$DO_RERECO" = true ]; then
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxChi2 0.01 -n $NEVENTS --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxChi2 15 -n $NEVENTS --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxChi2 30 -n $NEVENTS --run # default
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxChi2 120 -n $NEVENTS --run 
    
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxDisplacement 0.01 -n $NEVENTS  --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxDisplacement 0.25 -n $NEVENTS  --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxDisplacement 0.5 -n $NEVENTS  --run # default
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxDisplacement 100 -n $NEVENTS  --run 
    
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxSagitta 0.01 -n $NEVENTS --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxSagitta 1.0 -n $NEVENTS --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxSagitta 2.0 -n $NEVENTS --run # default
    python3 ReReco.py -i $INPUTDIR$SAMPLE --MaxSagitta 100 -n $NEVENTS --run 

    python3 ReReco.py -i $INPUTDIR$SAMPLE --nSigma 0.1 -n $NEVENTS --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --nSigma 2.0 -n $NEVENTS --run 
    python3 ReReco.py -i $INPUTDIR$SAMPLE --nSigma 3.0 -n $NEVENTS --run # default
    python3 ReReco.py -i $INPUTDIR$SAMPLE --nSigma 10 -n $NEVENTS --run
fi

DO_HISTO=true
if [ "$DO_HISTO" = true ]; then
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_0.01_disp_0.5_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_15.0_disp_0.5_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_120.0_disp_0.5_sag_2.0_sig_3.root

    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.01_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.25_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_100.0_sag_2.0_sig_3.root

    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_0.01_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_1.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_100.0_sig_3.root

    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_2.0_sig_0.1.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_2.0_sig_2.0.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_2.0_sig_3.root
    python3 makeHistograms_ReReco.py -i ${SAMPLE_RERECO}_chi2_30.0_disp_0.5_sag_2.0_sig_10.0.root
fi
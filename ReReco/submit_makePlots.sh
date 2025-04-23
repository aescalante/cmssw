python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_120.0_disp_0.5_sag_2.0_sig_3_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_15.0_disp_0.5_sag_2.0_sig_3_histograms.root \
-l "Chi2 = 120" "Chi2 = 30 (default)" "Chi2 = 15" \
-p "Chi2"

#python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_100.0_sag_2.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.25_sag_2.0_sig_3_histograms.root \
#-l "Disp = 100" "Disp = 0.5 (default)" "Disp = 0.25" \
#-p "Disp"

#python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_100.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_1.0_sig_3_histograms.root \
#-l "sag = 100" "sag = 2 (default)" "sag = 1" \
#-p "Sag"

#python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_10.0_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_2.0_histograms.root \
#-l "nSig = 10" "nSig = 3 (default)" "nSig = 2" \
#-p "nSig" 

python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
-l "vtx = True" "vtx = False (default)" \
-p "vtx" 
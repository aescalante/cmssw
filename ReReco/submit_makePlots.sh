#python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_120.0_disp_0.5_sag_2.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_15.0_disp_0.5_sag_2.0_sig_3_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_0.01_disp_0.5_sag_2.0_sig_3_histograms.root \
#-l "Chi2 = 120" "Chi2 = 30 (default)" "Chi2 = 15" "Chi2 = 0.01" \
#-p "Chi2"

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

#python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_histograms.root \
#plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
#-l "vtx = True" "vtx = False (default)" \
#-p "vtx" 

# multiply histograms from miltiple files
python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_quality_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_noselection_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
-l "cut = default" "cut = quality" "cut = nocut" "cut = nocut + vtx" \
-p "selection" 

# plot with different histograms from different files
python3 makePlots_ReReco.py \
-f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
   plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_genpt" "h_genpt_dsa" "h_genpt_dgb" "h_genpt_dgb" \
--file-index 0 0 0 1 \
-l "Gen muons" "DSA matched" "DGB matched" "DGB (new)" \
-p "genpt_comparison"

python3 makePlots_ReReco.py \
-f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
   plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_geneta" "h_geneta_dsa" "h_geneta_dgb" "h_geneta_dgb" \
--file-index 0 0 0 1 \
-l "Gen muons" "DSA matched" "DGB matched" "DGB (new)" \
-p "geneta_comparison"

# Example showing how to plot histograms with ratio panel - basic version to test
python3 makePlots_ReReco.py \
-f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
   plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_genpt" "h_genpt_dsa" "h_genpt_dgb" "h_genpt_dgb" \
--file-index 0 0 0 1 \
-l "Gen muons" "DSA matched" "DGB matched" "DGB (new)" \
-p "genpt_comparison_with_ratio" \
--ratio \
--ratio-indices 3 2

# Example showing how to plot histograms with ratio panel - basic version to test
python3 makePlots_ReReco.py \
-f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
   plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_geneta" "h_geneta_dsa" "h_geneta_dgb" "h_geneta_dgb" \
--file-index 0 0 0 1 \
-l "Gen muons" "DSA matched" "DGB matched" "DGB (new)" \
-p "geneta_comparison_with_ratio" \
--ratio \
--ratio-indices 3 2

python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_quality_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_noselection_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_pt" "h_pt" "h_pt" "h_pt" \
--file-index 0 1 2 3 \
-l "cut = default" "cut = quality" "cut = nocut" "cut = nocut + vtx" \
-p "pt_comparison_with_ratio" \
--ratio \
--ratio-indices 3 0 \
--log-y


python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_quality_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_noselection_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_pt_dsa" "h_pt_dsa" "h_pt_dsa" "h_pt_dsa" \
--file-index 0 1 2 3 \
-l "cut = default" "cut = quality" "cut = nocut" "cut = nocut + vtx" \
-p "ptdsa_comparison_with_ratio" \
--ratio \
--ratio-indices 1 0 \
--log-y


python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_quality_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_noselection_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_pt_early" "h_pt_early" "h_pt_early" "h_pt_early" \
--file-index 0 1 2 3 \
-l "cut = default" "cut = quality" "cut = nocut" "cut = nocut + vtx" \
-p "ptearly_comparison_with_ratio" \
--ratio \
--ratio-indices 1 0 \
--log-y

python3 makePlots_ReReco.py -f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_quality_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_noselection_histograms.root \
plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_d0" "h_d0" "h_d0" "h_d0" \
--file-index 0 1 2 3 \
-l "cut = default" "cut = quality" "cut = nocut" "cut = nocut + vtx" \
-p "d0_comparison_with_ratio" \
--ratio \
--ratio-indices 3 0 \
--log-y

# Example of plot for 12 Jun 2025 presentation, where I show the imapct of the vtx requirement
python3 makePlots_ReReco.py \
-f plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root \
   plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_histograms.root \
   plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_120.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root \
--histograms "h_genpt" "h_genpt" "h_genpt" \
--file-index 0 1 2 \
-l "default" "vtx = True" "New" \
-p "Jun12_genpt_comparison_with_ratio" \
--ratio \
--ratio-indices 2 0 \
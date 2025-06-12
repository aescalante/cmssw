# Script to run makePlots_ReReco.py with different histogram parameters in a loop
import os

# study I
histograms_to_plot = [
    "h_genpt", "h_geneta", "h_genpt_dgb", "h_geneta_dgb", "h_genlxy_dgb", "h_pt", "h_eta", "h_d0", "h_nSeeds", 
    "h_r", "h_ptError", "h_chi2", "h_nPxlHits", "h_nTrkHits", "h_nTOBHits", 
    "h_nTrkLayers", "h_nMuonHits", "h_nDTHits", "h_nCSCHits", 
    "h_DTStations", "h_CSCStations", "h_MuonStations"
]

base_files = [
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root",
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_histograms.root",
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root"
]

labels = ["default", "vtx = True", "new"]

# Loop through each histogram and create the plot
for hist in histograms_to_plot:
    
    cmd = "python3 makePlots_ReReco.py \\\n"
    cmd += "-f " + " ".join(base_files) + " \\\n"
    cmd += f"--histograms \"{hist}\" \"{hist}\" \"{hist}\" \\\n"
    
    label_args = " ".join([f"\"{label}\"" for label in labels])
    cmd += f"--file-index 0 1 2 \\\n"
    cmd += f"-l {label_args} \\\n"
    cmd += f"-p \"Jun12_vtx_vs_new_{hist}_comparison\" \\\n"
    cmd += "--ratio \\\n"
    cmd += "--ratio-indices 2 1"
    
    print(f"Processing {hist}...")
    os.system(cmd)

# study II
base_files = [
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root",
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_histograms.root",
]

labels = ["default", "vtx = True"]

# Loop through each histogram and create the plot
for hist in histograms_to_plot:
    
    cmd = "python3 makePlots_ReReco.py \\\n"
    cmd += "-f " + " ".join(base_files) + " \\\n"
    cmd += f"--histograms \"{hist}\" \"{hist}\" \\\n"
    
    label_args = " ".join([f"\"{label}\"" for label in labels])
    cmd += f"--file-index 0 1 \\\n"
    cmd += f"-l {label_args} \\\n"
    cmd += f"-p \"Jun12_default_vs_vtx_{hist}_comparison\" \\\n"
    cmd += "--ratio \\\n"
    cmd += "--ratio-indices 1 0"
    
    print(f"Processing {hist}...")
    os.system(cmd)

# study III
base_files = [
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_histograms.root",
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_histograms.root",
    "plots/ReReco_SMuonToMuGravitino_M_100_ctau_2000mm_chi2_30.0_disp_0.5_sag_2.0_sig_3_vtx_noselection_histograms.root"
]

labels = ["default", "vtx = True", "new"]

# Loop through each histogram and create the plot
for hist in histograms_to_plot:
    
    cmd = "python3 makePlots_ReReco.py \\\n"
    cmd += "-f " + " ".join(base_files) + " \\\n"
    cmd += f"--histograms \"{hist}\" \"{hist}\" \"{hist}\" \\\n"
    
    label_args = " ".join([f"\"{label}\"" for label in labels])
    cmd += f"--file-index 0 1 2 \\\n"
    cmd += f"-l {label_args} \\\n"
    cmd += f"-p \"Jun12_default_vs_new_{hist}_comparison\" \\\n"
    cmd += "--ratio \\\n"
    cmd += "--ratio-indices 2 0"
    
    print(f"Processing {hist}...")
    os.system(cmd)
# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SMuonToMuGravitino_M_900_ctau_500mm_TuneCP5_13p6TeV_pythia8_AODSIM_cff.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:output_AODSIM.root --conditions 124X_mcRun3_2022_realistic_v12 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --geometry DB:Extended --filein filelist:SMuonToMuGravitino_M_900_500mm_13p6TeV.txt --era Run3 --no_exec --mc -n -1 --nThreads 8
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.ProcessModifiers.siPixelQualityRawToDigi_cff import siPixelQualityRawToDigi

process = cms.Process('RECO',Run3,siPixelQualityRawToDigi)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_10.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_178.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_88.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_170.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_52.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_162.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_192.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_142.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_78.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_141.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_74.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_3.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_70.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_121.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_79.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_98.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_96.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_31.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_50.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_182.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_92.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_176.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_124.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_190.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_67.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_153.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_140.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_87.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_2.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_69.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_137.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_39.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_189.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_155.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_128.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_11.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_139.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_105.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_56.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_86.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_158.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_168.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_161.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_164.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_42.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_199.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_5.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_71.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_180.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_138.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_29.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_45.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_157.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_116.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_55.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_99.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_9.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_148.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_149.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_115.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_13.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_188.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_171.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_41.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_80.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_38.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_196.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_44.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_167.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_89.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_187.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_179.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_62.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_117.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_186.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_130.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_100.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_198.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_17.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_147.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_97.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_174.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_91.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_136.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_165.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_195.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_166.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_64.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_146.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_93.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_200.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_90.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_43.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_156.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_152.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_107.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_76.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_73.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_58.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_181.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_184.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_28.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_49.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_133.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_36.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_85.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_111.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_173.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_118.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_95.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_65.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_46.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_47.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_175.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_193.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_194.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_191.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_112.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_32.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_123.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_122.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_40.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_151.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_104.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_94.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_53.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_126.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_131.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_57.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_1.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_16.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_172.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_63.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_25.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_51.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_101.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_66.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_110.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_33.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_59.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_163.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_24.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_83.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_129.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_143.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_26.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_106.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_102.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_8.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_18.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_77.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_6.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_23.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_22.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_20.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_159.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_72.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_132.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_103.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_7.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_82.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_48.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_12.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_75.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_35.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_84.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_150.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_27.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_15.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_120.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_19.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_14.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_169.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_60.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_113.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_134.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_145.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_185.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_30.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_109.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_114.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_81.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_127.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_34.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_119.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_125.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_61.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_183.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_144.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_108.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_197.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_68.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_177.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_54.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_37.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_154.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_4.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_135.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_160.root',
        '/store/user/rlopezru/SMuonToMuGravitino_M_900_500mm_13p6TeV_GENSIM_2022MC_v01/PREMIXRAW_v02/250206_110144/0000/output_PREMIXRAW_21.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    fileName = cms.untracked.string('file:output_AODSIM.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_mcRun3_2022_realistic_v12', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.recosim_step = cms.Path(process.recosim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.recosim_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 8
process.options.numberOfStreams = 0

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

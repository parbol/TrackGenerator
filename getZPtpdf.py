import ROOT as r
import math

_file = r.TFile("/eos/user/f/fernance/LLP_Analysis/NTuples/2016_v3/DYJetsToLL_M-50/DYJetsToLL_M-50_chunk0.root")
_tree = _file.Get("Events")

hZpt = r.TH1F("Zptpdf", "Zptpdf", 130, 0, 130)
hRecoZpt = r.TH1F("RecoZptpdf", "RecoZptpdf", 130, 0, 130)

for i,_e in enumerate(_tree):

    #if i > 1000000: break
 
    # Find the Z
    Z = []
    for h in range(0, _e.nHardProcessParticle):
        if _e.HardProcessParticle_pdgId[h] == 23: Z.append(h)

    if not len(Z) == 1: continue # Only one Z

    if _e.HardProcessParticle_pt[Z[0]] > 0.00001: hZpt.Fill(_e.HardProcessParticle_pt[Z[0]])

    """
    leptons = []
    for g in range(0, _e.nGenLepton):
        if not _e.GenLeptonSel_fromHardProcessFinalState[g]: continue
        if not _e.GenLeptonSel_motherPdgId[g] == 23: continue
        leptons.append(g)

    if not len(leptons) == 2: continue

    #l1 = r.TVector3()
    #e1 = _e.GenLeptonSel_et[leptons[0]]/math.sin()
    pt0 = math.sqrt(_e.GenLeptonSel_et[leptons[0]]**2 - 0.105**2)
    pt1 = math.sqrt(_e.GenLeptonSel_et[leptons[1]]**2 - 0.105**2)
    l0 = r.TLorentzVector()
    l1 = r.TLorentzVector()
    l0.SetPtEtaPhiM(pt0, _e.GenLeptonSel_eta[leptons[0]], _e.GenLeptonSel_phi[leptons[0]], 0.105)
    l1.SetPtEtaPhiM(pt1, _e.GenLeptonSel_eta[leptons[1]], _e.GenLeptonSel_phi[leptons[1]], 0.105)
    
    print((l0+l1).M())
    print(_e.HardProcessParticle_eta[Z[0]], (l0+l1).Eta())
    print(_e.HardProcessParticle_pt[Z[0]], (l0+l1).Pt())
    print(_e.HardProcessParticle_pdgId[Z[0]])
    """

    leptons = []
    for h in range(0, _e.nHardProcessParticle):
        if not abs(_e.HardProcessParticle_pdgId[h]) == 13: continue
        leptons.append(h)

    if not len(leptons) == 2: continue

    l0 = r.TLorentzVector()
    l1 = r.TLorentzVector()
    l0.SetPtEtaPhiM(_e.HardProcessParticle_pt[leptons[0]], _e.HardProcessParticle_eta[leptons[0]], _e.HardProcessParticle_phi[leptons[0]], 0.105)
    l1.SetPtEtaPhiM(_e.HardProcessParticle_pt[leptons[1]], _e.HardProcessParticle_eta[leptons[1]], _e.HardProcessParticle_phi[leptons[1]], 0.105)
    hRecoZpt.Fill((l0+l1).Pt())


hZpt.Scale(1.0/hZpt.Integral())
hRecoZpt.Scale(1.0/hRecoZpt.Integral())

_fileout = r.TFile("Zpdf.root", "RECREATE")
_fileout.cd()
hZpt.Write()
hRecoZpt.Write()
_fileout.Close()

import math

def deltaPhi(a,b):
    '''
    computes delta phi for two given gen particles
    '''
    dphi = abs(a.phi()-b.phi())
    if dphi > math.pi: dphi = 2*math.pi-dphi
    return dphi

def deltaR(a,b):
    '''
    computes dR for two given gen particles
    '''
    dphi = deltaPhi(a,b)
    return math.hypot(a.eta()-b.eta(),dphi)

def getInterestingGenMuons(gen):
    '''
    returns a list with the interesting gen muons
    '''
    interestingGen = []
    for g in gen:
        # check if the gen level muon originated inside the tracker (and in the acceptance)
        if math.hypot(g.vx(), g.vy()) < 65 and abs(g.eta()) < 2.4:
            if abs(g.pdgId()) == 13 and g.isLastCopy() == True:
                interestingGen.append(g)
    return interestingGen

def getGenMuonIndex(reco, gen):
    '''
    tries a matching between reco and gen muons and returns the gen muon
    '''
    matchedGenIndex = -1
    minDr = 999
    for index, g in enumerate(gen):
        if deltaR(reco,g) < 0.2: 
            if deltaR(reco,g) < minDr:
                matchedGenIndex = index
                minDr = deltaR(reco,g)
    
    return matchedGenIndex
#created by Fasya Khuzaimah on 2020.04.17

import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TLegend, TAxis, TLatex, gStyle
import array as arr

print "Top electron region"

L = 41000.0 #/pb ; integrated luminosity

#---------------------------------#
#         TTtoSemileptonic        #
#---------------------------------#

Top_path = "combined_crab_TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"

xsTop = 300.9498

h_TopMatch = TH1F("h_TopMatch", "", 50, 0.0, 1.0)
h_Wmatch = TH1F("h_Wmatch", "", 50, 0.0, 1.0)
h_unmatch = TH1F("h_unmatch", "", 50, 0.0, 1.0)
h_ttFailed = TH1F("h_ttFailed", "", 50, 0.0, 1.0)
h_ttPassed = TH1F("h_ttPassed", "", 50, 0.0, 1.0)

openTop = TFile(Top_path, "read")
h_total_mcweight_Top = openTop.Get("h_total_mcweight")
totalEventsTop = h_total_mcweight_Top.Integral()
treeTop = openTop.Get("monoHbb_Tope_boosted")
EventsTop = treeTop.GetEntries()

for i in range(EventsTop):
    treeTop.GetEntry(i)
    st_TopMatching = getattr(treeTop, 'st_TopMatching')
    CSV_Top = getattr(treeTop, 'FJetCSV')
    SD_Top = getattr(treeTop, 'FJetMass')
    dPhi_Top = getattr(treeTop, 'min_dPhi')
    if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4):
        h_TopMatch.Fill(CSV_Top)
    if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4):
        h_Wmatch.Fill(CSV_Top)
    if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4):
        h_unmatch.Fill(CSV_Top)
    if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86):
        h_ttFailed.Fill(CSV_Top)
    if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86):
        h_ttPassed.Fill(CSV_Top)

h_TopMatch = h_TopMatch*(L*xsTop/totalEventsTop)
h_Wmatch = h_Wmatch*(L*xsTop/totalEventsTop)
h_unmatch = h_unmatch*(L*xsTop/totalEventsTop)
h_ttFailed = h_ttFailed*(L*xsTop/totalEventsTop)
h_ttPassed = h_ttPassed*(L*xsTop/totalEventsTop)

h_tt = h_ttFailed + h_ttPassed
frac_match = (h_TopMatch.Integral())/(h_tt.Integral())*100
frac_Wmatch = (h_Wmatch.Integral())/(h_tt.Integral())*100
frac_unmatch = (h_unmatch.Integral())/(h_tt.Integral())*100
frac_Passed = (h_ttPassed.Integral())/(h_tt.Integral())*100

print "match fraction :", frac_match, "%"
print "W-match fraction :", frac_Wmatch, "%"
print "unmatch fraction :", frac_unmatch, "%"
print "Mistag fraction :", frac_Passed, "%"



#---------------------------------#
#              W+Jets             #
#---------------------------------#

WJets_files = ["combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root","combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root","combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root","combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root","combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root","combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root"]

xsWJets = [407.9, 57.48, 12.87, 5.366, 1.074, 0.008001]

h_WJets = TH1F("h_WJets", "", 50, 0.0, 1.0)
h_sumWJets = TH1F("h_sumWJets", "", 50, 0.0, 1.0)

for k in range(len(WJets_files)):
    openWJets = TFile(WJets_files[k], "read")
    h_total_mcweight_WJets = openWJets.Get("h_total_mcweight")
    totalEventsWJets = h_total_mcweight_WJets.Integral()
    treeWJets = openWJets.Get("monoHbb_Tope_boosted")
    EventsWJets = treeWJets.GetEntries()

    for i in range(EventsWJets):
        treeWJets.GetEntry(i)
        CSV_WJets = getattr(treeWJets, 'FJetCSV')
        SD_WJets = getattr(treeWJets, 'FJetMass')
        dPhi_WJets = getattr(treeWJets, 'min_dPhi')
        if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4):
            h_WJets.Fill(CSV_WJets)

    h_WJets = h_WJets*(L*xsWJets[k]/totalEventsWJets)

    h_sumWJets += h_WJets



#---------------------------------#
#              Diboson             #
#---------------------------------#

Diboson_files = ["combined_crab_ZZ_TuneCP5_13TeV-pythia8.root","crab_WZ_TuneCP5_13TeV-pythia8.root","crab_WZ_TuneCP5_13TeV-pythia8.root"]

xsDiboson = [12.14, 27.6, 27.6]

h_Diboson = TH1F("h_Diboson", "", 50, 0.0, 1.0)
h_sumDiboson = TH1F("h_sumDiboson", "", 50, 0.0, 1.0)

for k in range(len(Diboson_files)):
    openDiboson = TFile(Diboson_files[k], "read")
    h_total_mcweight_Diboson = openDiboson.Get("h_total_mcweight")
    totalEventsDiboson = h_total_mcweight_Diboson.Integral()
    treeDiboson = openDiboson.Get("monoHbb_Tope_boosted")
    EventsDiboson = treeDiboson.GetEntries()
    
    for i in range(EventsDiboson):
        treeDiboson.GetEntry(i)
        CSV_Diboson = getattr(treeDiboson, 'FJetCSV')
        SD_Diboson = getattr(treeDiboson, 'FJetMass')
        dPhi_Diboson = getattr(treeDiboson, 'min_dPhi')
        if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4):
            h_Diboson.Fill(CSV_Diboson)

    h_Diboson = h_Diboson*(L*xsDiboson[k]/totalEventsDiboson)

    h_sumDiboson += h_Diboson



'''
#---------------------------------#
#               DATA              #
#---------------------------------#
##       Single Electron         ##
#---------------------------------#

SE_path = "combined_data_SE.root"

h_SE = TH1F("h_SE", "", 50, 0.0, 1.0)

openSE = TFile(SE_path, "read")
h_total_mcweight_SE = openSE.Get("h_total_mcweight")
totalEventsSE = h_total_mcweight_SE.Integral()
treeSE = openSE.Get("monoHbb_Tope_boosted")
EventsSE = treeSE.GetEntries()

for i in range(EventsSE):
    treeSE.GetEntry(i)
    CSV_SE = getattr(treeSE, 'FJetCSV')
    SD_SE = getattr(treeSE, 'FJetMass')
    dPhi_SE = getattr(treeSE, 'min_dPhi')
    if (SD_SE > 100.0) and (SD_SE < 150.0) and (dPhi_SE > 0.4):
        h_SE.Fill(CSV_SE)
'''



#------------Overlap histograms-------------#

h_TopMatchFinal = TH1F("h_TopMatchFinal", "", 50, 0.0, 1.0)
h_WmatchFinal = TH1F("h_WmatchFinal", "", 50, 0.0, 1.0)
h_unmatchFinal = TH1F("h_unmatchFinal", "", 50, 0.0, 1.0)
h_sumWJetsFinal = TH1F("h_sumWJetsFinal", "", 50, 0.0, 1.0)
#h_sumDibosonFinal = TH1F("h_sumDibosonFinal", "", 50, 0.0, 1.0)

h_TopMatchFinal = h_TopMatch + h_Wmatch + h_unmatch + h_sumWJets + h_sumDiboson
h_WmatchFinal = h_Wmatch + h_unmatch + h_sumWJets + h_sumDiboson
h_unmatchFinal = h_unmatch + h_sumWJets + h_sumDiboson
h_sumWJetsFinal = h_sumWJets + h_sumDiboson
#h_sumDibosonFinal = h_sumDiboson


c1 = TCanvas("c1","c1",900,700) #width-height
c1.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

leg = TLegend(0.65,0.7,0.85,0.87)
leg.SetBorderSize(0)
leg.SetTextSize(0.027)

#lt1 = TLatex()

h_TopMatchFinal.Rebin(2)
h_TopMatchFinal.SetFillColor(821)
h_TopMatchFinal.SetLineColor(923)
h_TopMatchFinal.GetXaxis().SetTitle("Double b score")
h_TopMatchFinal.GetYaxis().SetTitle("Events/Bin")
leg.AddEntry(h_TopMatchFinal, "Top (mtch.)", "f")

h_WmatchFinal.Rebin(2)
h_WmatchFinal.SetFillColor(822)
h_WmatchFinal.SetLineColor(923)
h_WmatchFinal.GetXaxis().SetTitle("Double b score")
h_WmatchFinal.GetYaxis().SetTitle("Events/Bin")
leg.AddEntry(h_WmatchFinal, "Top (W-mtch.)","f")

h_unmatchFinal.Rebin(2)
h_unmatchFinal.SetFillColor(813)
h_unmatchFinal.SetLineColor(923)
h_unmatchFinal.GetXaxis().SetTitle("Double b score")
h_unmatchFinal.GetYaxis().SetTitle("Events/Bin")
leg.AddEntry(h_unmatchFinal, "Top (unmtch.)","f")

h_sumWJetsFinal.Rebin(2)
h_sumWJetsFinal.SetFillColor(854)
h_sumWJetsFinal.SetLineColor(923)
h_sumWJetsFinal.GetXaxis().SetTitle("Double b score")
h_sumWJetsFinal.GetYaxis().SetTitle("Events/Bin")
leg.AddEntry(h_sumWJetsFinal, "W+Jets","f")

h_sumDiboson.Rebin(2)
h_sumDiboson.SetFillColor(627)
h_sumDiboson.SetLineColor(923)
h_sumDiboson.GetXaxis().SetTitle("Double b score")
h_sumDiboson.GetYaxis().SetTitle("Events/Bin")
leg.AddEntry(h_sumDiboson, "Diboson","f")



#-------Draw Histogram in c1---------#

h_TopMatchFinal.Draw("hist")
h_WmatchFinal.Draw("histsame")
h_unmatchFinal.Draw("histsame")
h_sumWJetsFinal.Draw("histsame")
h_sumDiboson.Draw("histsame")
leg.Draw()

lt = TLatex()
lt.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Preliminary}}}")
lt.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
lt.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.0 fb^{-1} (13 TeV)}}")

c1.cd()
c1.Modified()
c1.Update()
c1.SaveAs("Tope_test.pdf")



#------------Overlap histograms in c2-------------#

c2 = TCanvas("c2","c2",900,700) #width-height
c2.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

leg2 = TLegend(0.4,0.5,0.6,0.6)
leg2.SetBorderSize(0)
leg2.SetTextSize(0.027)

lt2 = TLatex()

h_ttFailed.Rebin(2)
h_ttFailed.SetFillColor(821)
h_ttFailed.SetLineColor(922)
h_ttFailed.GetXaxis().SetTitle("Double b score")
h_ttFailed.GetYaxis().SetTitle("Events/Bin")
h_ttFailed.SetMaximum(350.0)
leg2.AddEntry(h_ttFailed, "t#bar{t}", "f")

h_ttPassed.Rebin(2)
h_ttPassed.SetFillColor(622)
h_ttPassed.SetLineColor(922)
h_ttPassed.GetXaxis().SetTitle("Double b score")
h_ttPassed.GetYaxis().SetTitle("Events/Bin")
h_ttPassed.SetMaximum(350.0)
leg2.AddEntry(h_ttPassed, "t#bar{t} mistag", "f")

#-------Draw Histogram in c2---------#

h_ttFailed.Draw("hist")
h_ttPassed.Draw("histsame")
leg2.Draw()

lt2 = TLatex()
lt2.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Preliminary}}}")
lt2.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
lt2.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.0 fb^{-1} (13 TeV)}}")

c2.cd()
c2.Modified()
c2.Update()
c2.SaveAs("Tope_test2.pdf")

'''
#------------Overlap histograms in c3-------------#

c3 = TCanvas("c3","c3",900,700) #width-height
c3.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

leg3 = TLegend(0.4,0.5,0.6,0.6)
leg3.SetBorderSize(0)
leg3.SetTextSize(0.027)

lt3 = TLatex()

h_tt.Rebin(2)
h_tt.SetFillColor(821)
h_tt.SetLineColor(922)
h_tt.GetXaxis().SetTitle("Double b score")
h_tt.GetYaxis().SetTitle("Events/Bin")
leg3.AddEntry(h_tt, "t#bar{t}", "f")

#-------Draw Histogram in c3---------#

h_tt.Draw("hist")
leg3.Draw()

lt3 = TLatex()
lt3.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Preliminary}}}")
lt3.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
lt3.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.0 fb^{-1} (13 TeV)}}")

c3.cd()
c3.Modified()
c3.Update()
c3.SaveAs("Tope_test3.pdf")
'''

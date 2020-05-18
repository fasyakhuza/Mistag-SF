#created by Fasya Khuzaimah on 2020.04.17

import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TLegend, TAxis, TLatex, TPad, TPaveText, THStack, gStyle, gPad
import array as arr

print "Top Electron Region"
print " "

openfile1 = TFile("TopE.root")

topmatchTopE = openfile1.Get("h_TopMatch")
WmatchTopE = openfile1.Get("h_Wmatch")
unmatchTopE = openfile1.Get("h_unmatch")
wjetsTopE = openfile1.Get("h_sumWJets")
dibosonTopE = openfile1.Get("h_sumDiboson")
unsubtractedDataTopE = openfile1.Get("h_SE")

failMCsubtractTopE = openfile1.Get("h_ttFailed")
passMCsubtractTopE = openfile1.Get("h_ttPassed")
subtractedDataTopE = openfile1.Get("SubtractedData")

pfdataTopE = openfile1.Get("h_pfdata")
pfMCtopE = openfile1.Get("h_pfMC")
datapassTopE = openfile1.Get("Cloned_frac_tt_data_passed")
MCpassTopE = openfile1.Get("Cloned_frac_ttPassed")
#sfTopE = openfile1.Get("mistagSF")


print "Top Muon Region"
print " "

openfile2 = TFile("TopMu.root")

topmatchTopMu = openfile2.Get("h_TopMatch")
WmatchTopMu = openfile2.Get("h_Wmatch")
unmatchTopMu = openfile2.Get("h_unmatch")
wjetsTopMu = openfile2.Get("h_sumWJets")
dibosonTopMu = openfile2.Get("h_sumDiboson")
unsubtractedDataTopMu = openfile2.Get("h_MET")

failMCsubtractTopMu = openfile2.Get("h_ttFailed")
passMCsubtractTopMu = openfile2.Get("h_ttPassed")
subtractedDataTopMu = openfile2.Get("SubtractedData")

pfdataTopMu = openfile2.Get("h_pfdata")
pfMCtopMu = openfile2.Get("h_pfMC")
datapassTopMu = openfile2.Get("Cloned_frac_tt_data_passed")
MCpassTopMu = openfile2.Get("Cloned_frac_ttPassed")
#sfTopMu = openfile2.Get("mistagSF")

print "get histograms from root files: done"
print " "


#merge histogram"
print "merge histograms"
print " "


topmatchMerge = topmatchTopE + topmatchTopMu
WmatchMerge = WmatchTopE + WmatchTopMu
unmatchMerge = unmatchTopE + unmatchTopMu
wjetsMerge = wjetsTopE + wjetsTopMu
dibosonMerge = dibosonTopE + dibosonTopMu
unsubtractedDataMerge = unsubtractedDataTopE + unsubtractedDataTopMu

failMCsubtractMerge = failMCsubtractTopE + failMCsubtractTopMu
passMCsubtractMerge = passMCsubtractTopE + passMCsubtractTopMu
subtractedDataMerge = subtractedDataTopE + subtractedDataTopMu

pfdataMerge = pfdataTopE + pfdataTopMu
pfMCMerge = pfMCtopE + pfMCtopMu
datapassMerge = datapassTopE + datapassTopMu
MCpassMerge = MCpassTopE + MCpassTopMu

sfMerge = datapassMerge.Clone("sfMerge")
sfMerge.Sumw2()
sfMerge.Divide(MCpassMerge)

stacklist = []
stacklist.append(dibosonMerge)
stacklist.append(wjetsMerge)
stacklist.append(unmatchMerge)
stacklist.append(WmatchMerge)
stacklist.append(topmatchMerge)

print "merge histograms: done"
print " "



def myCanvas(c, size = [800, 700]):
    c = TCanvas(c, "", size[0], size[1])
    c.SetTopMargin(0.1)
    c.SetBottomMargin(0.15)
    c.SetRightMargin(0.1)
    c.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)
    return c

def myLegend(coordinate=[0.45,0.6,0.65,0.75], ncol=1):
    co = coordinate
    leg = TLegend(co[0], co[1], co[2], co[3])
    leg.SetNColumns(ncol)
    leg.SetBorderSize(0)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.03)
    return leg

def myStack(colorlist_, backgroundlist_, legendname_):
    hs = THStack("hs", "")
    leg1 = myLegend()
    for j in range(len(colorlist_)):
        h = backgroundlist_[j]
        h.SetFillColor(colorlist_[j])
        h.SetLineColor(colorlist_[j])
        hs.Add(h, "")
        leg1.AddEntry(h,legendname_[j],"f")
    return [hs, leg1]



print "draw histograms"
print " "
#----------------------- canvas 1 -----------------------#

c1 = myCanvas(c = "c1")
gPad.GetUymax()
leg1 = myLegend(coordinate=[0.45,0.57,0.65,0.6])

unsubtractedDataMerge.SetLineColor(1)
unsubtractedDataMerge.SetMarkerStyle(20)
unsubtractedDataMerge.SetMarkerSize(1.5)
unsubtractedDataMerge.GetXaxis().SetTitle("Double b score")
unsubtractedDataMerge.GetYaxis().SetTitle("Events/Bin")
leg1.AddEntry(unsubtractedDataMerge, "Data", "lep")
unsubtractedDataMerge.Draw("e1")

stackhisto = myStack(colorlist_ = [627, 854, 813, 822, 821],  backgroundlist_ = stacklist, legendname_ = ["Diboson", "W+Jets", "Top (unmtch.)", "Top (W-mtch.)", "Top (mtch.)"])
stackhisto[0].Draw("histsame")
unsubtractedDataMerge.Draw("e1same")
stackhisto[1].Draw()
leg1.Draw()

lt = TLatex()
lt.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
lt.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e+#mu)}}")
lt.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")

c1.SaveAs("Merge_all.pdf")


#----------------------- canvas 2 -----------------------#

c2 = myCanvas(c = "c2")
gPad.GetUymax()
leg2 = myLegend()

failMCsubtractMerge.SetFillColor(821)
failMCsubtractMerge.SetLineColor(821)#922
failMCsubtractMerge.GetXaxis().SetTitle("Double b score")
failMCsubtractMerge.GetYaxis().SetTitle("Events/Bin")
leg2.AddEntry(failMCsubtractMerge, "t#bar{t}", "f")

passMCsubtractMerge.SetFillColor(622)
passMCsubtractMerge.SetLineColor(622)
#passMCsubtractMerge.GetXaxis().SetTitle("Double b score")
#passMCsubtractMerge.GetYaxis().SetTitle("Events/Bin")
leg2.AddEntry(passMCsubtractMerge, "t#bar{t} mistag", "f")

subtractedDataMerge.SetLineColor(1)
subtractedDataMerge.SetMarkerStyle(20)
subtractedDataMerge.SetMarkerSize(1.5)
#subtractedDataMerge.GetXaxis().SetTitle("Double b score")
#subtractedDataMerge.GetYaxis().SetTitle("Events/Bin")
leg2.AddEntry(subtractedDataMerge, "Subtracted Data", "lep")

failMCsubtractMerge.Draw("hist")
passMCsubtractMerge.Draw("histsame")
subtractedDataMerge.Draw("e1same")
leg2.Draw()

lt2 = TLatex()
lt2.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
lt2.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e+#mu)}}")
lt2.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")

c2.SaveAs("Merged_subtrac.pdf")


#----------------------- canvas 3 -----------------------#

c3 = myCanvas(c = "c3", size = [700, 900])

pad1 = TPad("pad1", "", 0.01, 0.25, 0.93, 1.0)
pad1.SetTopMargin(0.1)
pad1.SetRightMargin(0.05)
pad1.SetLeftMargin(0.17)
pad1.SetBottomMargin(0.05)

pad2 = TPad("pad2", "", 0.0, 0.0, 0.375, 0.24)
pad2.SetTopMargin(0.0)
pad2.SetRightMargin(0.0)
pad2.SetLeftMargin(0.0)
pad2.SetBottomMargin(0.0)

pad3 = TPad("pad3", "", 0.38, 0.025, 0.94, 0.25)
pad2.SetTopMargin(0.05)
pad2.SetRightMargin(0.0)
pad2.SetLeftMargin(0.45)
pad2.SetBottomMargin(0.2)

pad1.Draw()
pad2.Draw()
pad3.Draw()

#* Pad 1 *#
pad1.cd()
leg3 = myLegend(coordinate=[0.65,0.4,0.75,0.5])

pfdataMerge.SetLineColor(1)
pfdataMerge.SetMarkerStyle(20)
pfdataMerge.SetLineWidth(2)
pfdataMerge.SetMaximum(2.2)
pfdataMerge.GetYaxis().SetTitle("Fraction")
pfdataMerge.GetXaxis().SetTickLength(0.03)
pfdataMerge.GetXaxis().SetNdivisions(104)
pfdataMerge.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Fail")
pfdataMerge.GetXaxis().ChangeLabel(1,-1,0)
pfdataMerge.GetXaxis().ChangeLabel(3,-1,0)
pfdataMerge.GetXaxis().ChangeLabel(-1,-1,0)
pfdataMerge.GetXaxis().ChangeLabel(-2,-1,-1,-1,-1,-1,"Pass")
leg3.AddEntry(pfdataMerge, "Subtracted Data", "lep")

pfMCMerge.SetLineColor(870)
pfMCMerge.SetLineWidth(3)
leg3.AddEntry(pfMCMerge, "tt", "l")

pfdataMerge.Draw("e1")
pfMCMerge.Draw("histsame")
leg3.Draw()

lt3 = TLatex()
lt3.DrawLatexNDC(0.21,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
lt3.DrawLatexNDC(0.21,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e+#mu)}}")
lt3.DrawLatexNDC(0.21,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt3.DrawLatexNDC(0.67,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
lt3.Draw()

#* Pad 2 *#
pad2.cd()
datapassMerge.SetLineColor(1)
datapassMerge.SetLineWidth(2)
datapassMerge.SetMarkerStyle(20)
datapassMerge.GetYaxis().SetTitle("Fraction")
datapassMerge.GetYaxis().SetTitleSize(0.09)
datapassMerge.GetYaxis().SetLabelSize(0.1)
datapassMerge.GetYaxis().SetNdivisions(404)
datapassMerge.SetMaximum(0.45)
datapassMerge.SetMinimum(0.0)
datapassMerge.GetXaxis().SetTitle("Pass")
datapassMerge.GetXaxis().SetTitleSize(0.09)
datapassMerge.GetXaxis().SetTitleOffset(0.4)

MCpassMerge.SetLineColor(870)
MCpassMerge.SetLineWidth(3)
datapassMerge.Draw("e1")
MCpassMerge.Draw("histsame")

'''
lt4 = TLatex()
lt4.DrawLatexNDC(0.4,0.5,"#scale[2.0]{Eff.}")
lt4.Draw()
'''

#* Pad 3 *#
pad3.cd()

SF = sfMerge.Integral()
print "******"
print "mistag SF:", SF

SFfinal = round(SF, 2)
SFtext = "SF = "+str(SFfinal)

sfMerge.SetLineColor(797)
sfMerge.SetLineWidth(3)
sfMerge.SetMaximum(1.2)
sfMerge.SetMinimum(0.6)
sfMerge.GetXaxis().SetTitle(" ")
sfMerge.GetXaxis().SetLabelOffset(999)
sfMerge.GetXaxis().SetLabelSize(0)
sfMerge.GetXaxis().SetTickLength(0)
sfMerge.GetYaxis().SetLabelSize(0.1)
sfMerge.GetYaxis().SetNdivisions(404)

sfMerge.Draw("hist")

pt = TPaveText(0.21, 0.72, 0.31, 0.8, "brNDC")
pt.SetBorderSize(0)
pt.SetTextAlign(12)
pt.SetFillStyle(0)
pt.SetTextFont(42)
pt.SetTextSize(0.1)
pt.AddText(SFtext)
pt.Draw()

c3.SaveAs("Merge_SF.pdf")

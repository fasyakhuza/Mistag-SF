#created by Fasya Khuzaimah on 2020.05.12

import ROOT
from ROOT import TFile, TH1F, TGraph, TGraphAsymmErrors, gPad, gStyle

import PlotTemplates
from PlotTemplates import *


openf = TFile("monoHbb_WS.root")

#Get histogram from root file

topMu = openf.Get("transferfactor/monoHbb2017_B_TOPMU_tt")
topE = openf.Get("transferfactor/monoHbb2017_B_TOPE_tt")
WE = openf.Get("transferfactor/monoHbb2017_B_WE_wjets")
WMu = openf.Get("transferfactor/monoHbb2017_B_WMU_wjets")
ZMumu = openf.Get("transferfactor/monoHbb2017_B_ZMUMU_dyjets")
ZEE = openf.Get("transferfactor/monoHbb2017_B_ZEE_dyjets")

def drawenergy(is2017 = True, text_=" Internal", data = True):
    pt = TPaveText(0.0877181,0.9,0.9580537,0.96,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(52)
    
    cmstextSize = 0.07
    preliminarytextfize = cmstextSize * 0.7
    lumitextsize = cmstextSize *0.7
    pt.SetTextSize(cmstextSize)
    text = pt.AddText(0.01,0.57,"#font[61]{CMS}")
    
    pt1 = TPaveText(0.0877181,0.904,0.9580537,0.96,"brNDC")
    pt1.SetBorderSize(0)
    pt1.SetTextAlign(12)
    pt1.SetFillStyle(0)
    pt1.SetTextFont(52)
    
    pt1.SetTextSize(preliminarytextfize)
    #text1 = pt1.AddText(0.155,0.4,"Preliminary")
    text1 = pt1.AddText(0.125,0.4,text_)
    
    pt2 = TPaveText(0.0877181,0.9,0.7280537,0.96,"brNDC")
    pt2.SetBorderSize(0)
    pt2.SetTextAlign(12)
    pt2.SetFillStyle(0)
    pt2.SetTextFont(52)
    pt2.SetTextFont(42)
    pt2.SetTextSize(lumitextsize)
    
    pavetext = ''
    if is2017 and data: pavetext = "41.5 fb^{-1} (13 TeV)"
    if (not is2017) and data: pavetext = "(13 TeV)"
    
    if is2017 and not data: pavetext = "(13 TeV)"
    if (not is2017) and not data: pavetext = "(13 TeV)"
    
    if data: text3 = pt2.AddText(0.735,0.5,pavetext)
    if not data: text3 = pt2.AddText(0.75,0.5,pavetext)
    
    return [pt,pt1,pt2]

#** Draw TOPMU Histogram **#

c1 = PlotTemplates.myCanvas()

gPad.GetUymax()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

h_topMu = PlotTemplates.Save1DHisto(topMu, c1, "Recoil", "Yield Ratio (TopMu/tt)")
h_topMu.SetLineWidth(2)
h_topMu.SetMarkerStyle(20)
h_topMu.Draw("e1")

E1 = drawenergy()
for i in E1:
    i.Draw()

c1.Update()
c1.SaveAs("transferfactor/TopMu.pdf")

#** Draw TOPE Histogram **#

c2 = PlotTemplates.myCanvas()

gPad.GetUymax()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

h_topE = PlotTemplates.Save1DHisto(topE, c2, "Recoil", "Yield Ratio (TopE/tt)")
h_topE.SetLineWidth(2)
h_topE.SetMarkerStyle(20)
h_topE.Draw("e1")

E2 = drawenergy()
for i in E2:
    i.Draw()

c2.Update()
c2.SaveAs("transferfactor/TopE.pdf")

#** Draw WE Histogram **#

c3 = PlotTemplates.myCanvas()

gPad.GetUymax()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

h_WE = PlotTemplates.Save1DHisto(WE, c3, "Recoil", "Yield Ratio (We/tt)")
h_WE.SetLineWidth(2)
h_WE.SetMarkerStyle(20)
h_WE.Draw("e1")

E3 = drawenergy()
for i in E3:
    i.Draw()

c3.Update()
c3.SaveAs("transferfactor/WE.pdf")

#** Draw WMU Histogram **#

c4 = PlotTemplates.myCanvas()

gPad.GetUymax()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

h_WMu = PlotTemplates.Save1DHisto(WMu, c4, "Recoil", "Yield Ratio (WMu/tt)")
h_WMu.SetLineWidth(2)
h_WMu.SetMarkerStyle(20)
h_WMu.Draw("e1")

E4 = drawenergy()
for i in E4:
    i.Draw()

c4.Update()
c4.SaveAs("transferfactor/WMu.pdf")

#** Draw ZMUMU Histogram **#

c5 = PlotTemplates.myCanvas()

gPad.GetUymax()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

h_ZMumu = PlotTemplates.Save1DHisto(ZMumu, c5, "Recoil", "Yield Ratio (ZMuMu/tt)")
h_ZMumu.SetLineWidth(2)
h_ZMumu.SetMarkerStyle(20)
h_ZMumu.Draw("e1")

E5 = drawenergy()
for i in E5:
    i.Draw()

c5.Update()
c5.SaveAs("transferfactor/ZMuMu.pdf")

#** Draw ZEE Histogram **#

c6 = PlotTemplates.myCanvas()

gPad.GetUymax()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

h_ZEE = PlotTemplates.Save1DHisto(ZEE, c6, "Recoil", "Yield Ratio (Zee/tt)")
h_ZEE.SetLineWidth(2)
h_ZEE.SetMarkerStyle(20)
h_ZEE.Draw("e1")

E6 = drawenergy()
for i in E6:
    i.Draw()

c6.Update()
c6.SaveAs("transferfactor/ZEE.pdf")



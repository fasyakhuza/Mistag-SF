#created by Fasya Khuzaimah on 2020.05.01

import ROOT
from ROOT import TFile, TH1F, TGraph, TGraphAsymmErrors

import PlotTemplates
from PlotTemplates import *


file = TFile("fitDiagnostics.root")


#------------------------TOPE------------------------------#

Tope = "shapes_fit_b/TOPE/"
#getDir = file.cd("shapes_fit_b/TOPE")

#get the histogram inside shapes_fit_b/TOPE
Topedata = file.Get(Tope+"data")
dataTope = TH1F("dataTope","",4,200,1000)
nPointsTope = Topedata.GetN()
for i in range(nPointsTope):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Topedata.GetPoint(i, x, y)
    k = dataTope.FindFixBin(x)
    dataTope.SetBinContent(k, y)
Topediboson = file.Get(Tope+"diboson")
TopeDYjets = file.Get(Tope+"dyjets")
TopeQCD = file.Get(Tope+"qcd")
TopeST = file.Get(Tope+"singlet")
TopeSMH = file.Get(Tope+"smh")
TopeWjets = file.Get(Tope+"wjets")

tt_data_in_topE = dataTope - (Topediboson + TopeDYjets + TopeQCD + TopeST + TopeSMH + TopeWjets)


#-----------------------TOPMU-----------------------------#

Topmu = "shapes_fit_b/TOPMU/"

#get the histogram inside shapes_fit_b/TOPMU
Topmudata = file.Get(Topmu+"data")
dataTopmu = TH1F("dataTopmu","",4,200,1000)
nPointsTopmu = Topmudata.GetN()
for i in range(nPointsTopmu):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Topmudata.GetPoint(i, x, y)
    k = dataTopmu.FindFixBin(x)
    dataTopmu.SetBinContent(k,y)
Topmudiboson = file.Get(Topmu+"diboson")
TopmuDYjets = file.Get(Topmu+"dyjets")
TopmuQCD = file.Get(Topmu+"qcd")
TopmuST = file.Get(Topmu+"singlet")
TopmuSMH = file.Get(Topmu+"smh")
TopmuWjets = file.Get(Topmu+"wjets")

tt_data_in_topMU = dataTopmu - (Topmudiboson + TopmuDYjets + TopmuQCD + TopmuST + TopmuSMH + TopmuWjets)


#----------------------SR-----------------------------------#

SR = "shapes_fit_b/SR/"

#get the histogram inside shapes_fit_b/SR
SRdata = file.Get(SR+"data")
dataSR = TH1F("dataSR","",4,200,1000)
nPointsSR = SRdata.GetN()
for i in range(nPointsSR):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    SRdata.GetPoint(i, x, y)
    k = dataSR.FindFixBin(x)
    dataSR.SetBinContent(k,y)
SRdiboson = file.Get(SR+"diboson")
SRqcd = file.Get(SR+"qcd")
SRst = file.Get(SR+"singlet")
SRsmh = file.Get(SR+"smh")
SRwjets = file.Get(SR+"wjets")
SRzjets = file.Get(SR+"zjets")

tt_data_in_SR = dataSR - (SRdiboson + SRqcd + SRst + SRsmh + SRwjets + SRzjets)


#----------------------yield ratio--------------------------#

yieldratioTope = tt_data_in_topE.Clone("yieldratioTope")
yieldratioTopmu = tt_data_in_topMU.Clone("yieldratioTopmu")
yieldratioTope.Divide(tt_data_in_SR)
yieldratioTopmu.Divide(tt_data_in_SR)


#-----------------Plot the Top e yield ratio----------------#

c1 = PlotTemplates.myCanvas()
h_yieldratioTope = PlotTemplates.Save1DHisto(yieldratioTope, c1, "Recoil", "Yield Ratio (TopE/tt)")
leg1 = PlotTemplates.SetLegend()
leg1.AddEntry(yieldratioTope, "Data")
leg1.Draw()
E1 = PlotTemplates.drawenergy(is2017 = True, data=True)
for i in E1:
    i.Draw()

c1.cd()
c1.Modified()
c1.Update()
c1.SaveAs("Tope_test.pdf")
c1.SaveAs("Tope_test.png")


#----------------Plot the Top Mu yield ratio----------------#

c2 = PlotTemplates.myCanvas()
h_yieldratioTopmu = PlotTemplates.Save1DHisto(yieldratioTopmu, c2, "Recoil", "Yield Ratio (TopMu/tt)")
leg2 = PlotTemplates.SetLegend()
leg2.AddEntry(yieldratioTopmu, "Data")
leg2.Draw()
E2 = PlotTemplates.drawenergy(is2017 = True, data=True)
for i in E2:
    i.Draw()

c2.cd()
c2.Modified()
c2.Update()
c2.SaveAs("Topmu_test.pdf")
c2.SaveAs("Topmu_test.png")

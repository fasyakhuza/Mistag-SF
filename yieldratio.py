#created by Fasya Khuzaimah on 2020.05.01

import ROOT
from ROOT import TFile, TH1F, TGraph, TGraphAsymmErrors

import PlotTemplates
from PlotTemplates import *

import array as arr

nbins = 4
edges = arr.array('f')
min = 0.0
max = 10.0
file = TFile("fitDiagnostics.root")


#------------------------TOPE------------------------------#

Tope = "shapes_fit_b/TOPE/"
#getDir = file.cd("shapes_fit_b/TOPE")

#get the histogram inside shapes_fit_b/TOPE
TopeDYjets = file.Get(Tope+"dyjets")
for i in range(nbins):
    low = TopeDYjets.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
up = TopeDYjets.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)
print edges

Topedata = file.Get(Tope+"data")
dataTope = TH1F("dataTope","",nbins,edges)
nPointsTope = Topedata.GetN()
for i in range(nPointsTope):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Topedata.GetPoint(i, x, y)
    k = dataTope.FindFixBin(x)
    print "y", y
    dataTope.SetBinContent(k, y)
    dataTope.SetBinError(i+1, Topedata.GetErrorY(i))
Topediboson = file.Get(Tope+"diboson")

TopeQCD = file.Get(Tope+"qcd")
TopeST = file.Get(Tope+"singlet")
TopeSMH = file.Get(Tope+"smh")
TopeWjets = file.Get(Tope+"wjets")

tt_mc_in_topE = file.Get(Tope+"tt")
tt_data_in_topE = dataTope - (Topediboson + TopeDYjets + TopeQCD + TopeST + TopeSMH + TopeWjets)

#-----------------------TOPMU-----------------------------#

Topmu = "shapes_fit_b/TOPMU/"

#get the histogram inside shapes_fit_b/TOPMU
Topmudata = file.Get(Topmu+"data")
dataTopmu = TH1F("dataTopmu","",nbins,edges)
nPointsTopmu = Topmudata.GetN()
for i in range(nPointsTopmu):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Topmudata.GetPoint(i, x, y)
    k = dataTopmu.FindFixBin(x)
    dataTopmu.SetBinContent(k,y)
    dataTopmu.SetBinError(i+1, Topmudata.GetErrorY(i))
Topmudiboson = file.Get(Topmu+"diboson")
TopmuDYjets = file.Get(Topmu+"dyjets")
TopmuQCD = file.Get(Topmu+"qcd")
TopmuST = file.Get(Topmu+"singlet")
TopmuSMH = file.Get(Topmu+"smh")
TopmuWjets = file.Get(Topmu+"wjets")

tt_mc_in_topMu = file.Get(Topmu+"tt")
tt_data_in_topMU = dataTopmu - (Topmudiboson + TopmuDYjets + TopmuQCD + TopmuST + TopmuSMH + TopmuWjets)


#----------------------SR-----------------------------------#

SR = "shapes_fit_b/SR/"

#get the histogram inside shapes_fit_b/SR
SRdata = file.Get(SR+"data")
dataSR = TH1F("dataSR","",nbins,edges)
nPointsSR = SRdata.GetN()
for i in range(nPointsSR):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    SRdata.GetPoint(i, x, y)
    k = dataSR.FindFixBin(x)
    dataSR.SetBinContent(k,y)
    dataSR.SetBinError(i+1, SRdata.GetErrorY(i))
SRdiboson = file.Get(SR+"diboson")
SRqcd = file.Get(SR+"qcd")
SRst = file.Get(SR+"singlet")
SRsmh = file.Get(SR+"smh")
SRwjets = file.Get(SR+"wjets")
SRzjets = file.Get(SR+"zjets")

tt_mc_in_SR = file.Get(SR+"tt")
tt_data_in_SR = dataSR - (SRdiboson + SRqcd + SRst + SRsmh + SRwjets + SRzjets)


#----------------------yield ratio--------------------------#

#**********DATA*************#

yieldratioTopeData = tt_data_in_topE.Clone("yieldratioTopeData")
yieldratioTopmuData = tt_data_in_topMU.Clone("yieldratioTopmuData")
yieldratioTopeData.Divide(tt_data_in_SR)#, 1.0, 1.0, "B")
yieldratioTopmuData.Divide(tt_data_in_SR)#, 1.0, 1.0, "B")

print "Top e data", yieldratioTopeData.GetBinContent(4)
print "Top mu data", yieldratioTopmuData.GetBinContent(4)

#***********MC************#

yieldratioTopeMC = tt_mc_in_topE.Clone("yieldratioTopeMC")
yieldratioTopmuMC = tt_mc_in_topMu.Clone("yieldratioTopmuMC")
yieldratioTopeMC.Divide(tt_mc_in_SR)
yieldratioTopmuMC.Divide(tt_mc_in_SR)

print "Top e MC", yieldratioTopeMC.GetBinContent(4)
print "Top mu MC", yieldratioTopmuMC.GetBinContent(4)

#-----------------Plot the Top e yield ratio----------------#

c1 = PlotTemplates.myCanvas()

h_yieldratioTopeData = PlotTemplates.Save1DHisto(yieldratioTopeData, c1, "Recoil", "Yield Ratio (TopE/tt)")
h_yieldratioTopeData.SetMaximum(max)
h_yieldratioTopeData.SetMinimum(min)
h_yieldratioTopeData.SetMarkerStyle(20)
h_yieldratioTopeData.SetLineWidth(1)

h_yieldratioTopeMC = PlotTemplates.Save1DHisto(yieldratioTopeMC, c1, "Recoil", "Yield Ratio (TopE/tt)")
h_yieldratioTopeMC.SetMaximum(max)
h_yieldratioTopeMC.SetMinimum(min)
#h_yieldratioTopeMC.SetMarkerStyle(20)
#h_yieldratioTopeMC.SetMarkerColor(2)
h_yieldratioTopeMC.SetLineColor(2)
h_yieldratioTopeMC.SetLineWidth(1)

h_yieldratioTopeMC.Draw("e1")
h_yieldratioTopeData.Draw("e1same")

leg1 = PlotTemplates.SetLegend(coordinate_=[.15,.7,.47,.87])
leg1.AddEntry(h_yieldratioTopeMC, "MC")
leg1.AddEntry(yieldratioTopeData, "Data")
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

h_yieldratioTopmuData = PlotTemplates.Save1DHisto(yieldratioTopmuData, c2, "Recoil", "Yield Ratio (TopMu/tt)")
h_yieldratioTopmuData.SetMaximum(max)
h_yieldratioTopmuData.SetMinimum(min)
h_yieldratioTopmuData.SetMarkerStyle(20)
h_yieldratioTopmuData.SetLineWidth(1)

h_yieldratioTopmuMC = PlotTemplates.Save1DHisto(yieldratioTopmuMC, c1, "Recoil", "Yield Ratio (TopMu/tt)")
h_yieldratioTopmuMC.SetMaximum(max)
h_yieldratioTopmuMC.SetMinimum(min)
#h_yieldratioTopmuMC.SetMarkerStyle(20)
#h_yieldratioTopmuMC.SetMarkerColor(2)
h_yieldratioTopmuMC.SetLineColor(2)
h_yieldratioTopmuMC.SetLineWidth(1)

h_yieldratioTopmuMC.Draw("e1")
h_yieldratioTopmuData.Draw("e1same")

leg2 = PlotTemplates.SetLegend(coordinate_=[.15,.7,.47,.87])
leg2.AddEntry(h_yieldratioTopmuMC, "MC")
leg2.AddEntry(yieldratioTopmuData, "Data")
leg2.Draw()
E2 = PlotTemplates.drawenergy(is2017 = True, data=True)
for i in E2:
    i.Draw()

c2.cd()
c2.Modified()
c2.Update()
c2.SaveAs("Topmu_test.pdf")
c2.SaveAs("Topmu_test.png")


#------------------Get Each Histogram--------------------#

c3 = PlotTemplates.myCanvas()
h_data_in_topE = PlotTemplates.Save1DHisto(dataTope, c3, "Recoil", "Events")
c3.cd()
c3.Modified()
c3.Update()
c3.SaveAs("data_in_topE.pdf")
'''
c4 = PlotTemplates.myCanvas()
h_tt_data_in_topMu = PlotTemplates.Save1DHisto(tt_data_in_topMU, c4, "Recoil", "Events")
c4.cd()
c4.Modified()
c4.Update()
c4.SaveAs("tt_data_in_topMu.pdf")

c5 = PlotTemplates.myCanvas()
h_tt_data_in_SR = PlotTemplates.Save1DHisto(tt_data_in_SR, c5, "Recoil", "Events")
c5.cd()
c5.Modified()
c5.Update()
c5.SaveAs("tt_data_in_SR.pdf")

c6 = PlotTemplates.myCanvas()
h_dataSR = PlotTemplates.Save1DHisto(dataSR, c6, "Recoil", "Events")
c6.cd()
c6.Modified()
c6.Update()
c6.SaveAs("dataSR.pdf")
'''

#created by Fasya Khuzaimah on 2020.05.01

import ROOT
from ROOT import TFile, TH1F, TGraph, TGraphAsymmErrors

import PlotTemplates
from PlotTemplates import *

import array as arr

nbins = 4
edges = arr.array('f')
min = -6.0
max = 9.0
file = TFile("fitDiagnostics.root")


#------------------------TOPE------------------------------#

We = "shapes_fit_b/WE/"

#get the histogram inside shapes_fit_b/WE
WeDYjets = file.Get(We+"dyjets")
for i in range(nbins):
    low = WeDYjets.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
    #Error = WeDYjets.GetBinError(i+1)
    #print "ERROR_",i+1,Error
up = WeDYjets.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)
print edges

Wedata = file.Get(We+"data")
dataWe = TH1F("dataWe","",nbins,edges)
nPointsWe = Wedata.GetN()
for i in range(nPointsWe):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Wedata.GetPoint(i, x, y)
    k = dataWe.FindFixBin(x)
    #print "y", y
    dataWe.SetBinContent(k, y)
    dataWe.SetBinError(i+1, Wedata.GetErrorY(i))

Wediboson = file.Get(We+"diboson")
WeQCD = file.Get(We+"qcd")
WeST = file.Get(We+"singlet")
WeSMH = file.Get(We+"smh")
WeTT = file.Get(We+"tt")
WeWjets = file.Get(We+"wjets")
'''
for i in range(nbins):
    ErrorWjet = WeWjets.GetBinError(i+1)
    print "W+jets error_",i+1, ErrorWjet
'''

Wjets_data_in_WE = dataWe - (Wediboson + WeDYjets + WeQCD + WeST + WeSMH + WeTT)

#-----------------------TOPMU-----------------------------#

Wmu = "shapes_fit_b/WMU/"

#get the histogram inside shapes_fit_b/WMU
Wmudata = file.Get(Wmu+"data")
dataWmu = TH1F("dataWmu","",nbins,edges)
nPointsWmu = Wmudata.GetN()
for i in range(nPointsWmu):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Wmudata.GetPoint(i, x, y)
    k = dataWmu.FindFixBin(x)
    dataWmu.SetBinContent(k,y)
    dataWmu.SetBinError(i+1, Wmudata.GetErrorY(i))
Wmudiboson = file.Get(Wmu+"diboson")
WmuDYjets = file.Get(Wmu+"dyjets")
WmuQCD = file.Get(Wmu+"qcd")
WmuST = file.Get(Wmu+"singlet")
WmuSMH = file.Get(Wmu+"smh")
WmuTT = file.Get(Wmu+"tt")
WmuWjets = file.Get(Wmu+"wjets")


Wjets_data_in_WMU = dataWmu - (Wmudiboson + WmuDYjets + WmuQCD + WmuST + WmuSMH + WmuTT)


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
SRtt = file.Get(SR+"tt")

Wjets_data_in_SR = dataSR - (SRdiboson + SRqcd + SRst + SRsmh + SRzjets +SRtt)


#----------------------yield ratio--------------------------#

#**********DATA*************#

yieldratioWeData = Wjets_data_in_WE.Clone("yieldratioWeData")
yieldratioWmuData = Wjets_data_in_WMU.Clone("yieldratioWmuData")
yieldratioWeData.Divide(Wjets_data_in_SR)#, 1.0, 1.0, "B")
yieldratioWmuData.Divide(Wjets_data_in_SR)#, 1.0, 1.0, "B")

#print "W e data", yieldratioWeData.GetBinContent(4)
#print "W mu data", yieldratioWmuData.GetBinContent(4)

#***********MC************#

yieldratioWeMC = WeWjets.Clone("yieldratioWeMC")
yieldratioWmuMC = WmuWjets.Clone("yieldratioWmuMC")
yieldratioWeMC.Divide(SRwjets)
yieldratioWmuMC.Divide(SRwjets)

#print "W e MC", yieldratioWeMC.GetBinContent(4)
#print "W mu MC", yieldratioWmuMC.GetBinContent(4)

#-----------------Plot the Top e yield ratio----------------#

c1 = PlotTemplates.myCanvas()

h_yieldratioWeData = PlotTemplates.Save1DHisto(yieldratioWeData, c1, "Recoil", "Yield Ratio (We/WJets)")
h_yieldratioWeData.SetMaximum(max)
h_yieldratioWeData.SetMinimum(min)
h_yieldratioWeData.SetMarkerStyle(20)
h_yieldratioWeData.SetLineWidth(1)

h_yieldratioWeMC = PlotTemplates.Save1DHisto(yieldratioWeMC, c1, "Recoil", "Yield Ratio (We/WJets)")
h_yieldratioWeMC.SetMaximum(max)
h_yieldratioWeMC.SetMinimum(min)
#h_yieldratioWeMC.SetMarkerStyle(20)
#h_yieldratioWeMC.SetMarkerColor(2)
h_yieldratioWeMC.SetLineColor(2)
h_yieldratioWeMC.SetLineWidth(1)

h_yieldratioWeMC.Draw("e1")
h_yieldratioWeData.Draw("e1same")

leg1 = PlotTemplates.SetLegend(coordinate_=[.15,.7,.47,.87])
leg1.AddEntry(h_yieldratioWeMC, "MC")
leg1.AddEntry(yieldratioWeData, "Data")
leg1.Draw()
E1 = PlotTemplates.drawenergy(is2017 = True, data=True)
for i in E1:
    i.Draw()

c1.cd()
#c1.Modified()
#c1.Update()
c1.SaveAs("We_test.pdf")
c1.SaveAs("We_test.png")


#----------------Plot the Top Mu yield ratio----------------#

c2 = PlotTemplates.myCanvas()

h_yieldratioWmuData = PlotTemplates.Save1DHisto(yieldratioWmuData, c2, "Recoil", "Yield Ratio (Wmu/WJets)")
h_yieldratioWmuData.SetMaximum(max)
h_yieldratioWmuData.SetMinimum(min)
h_yieldratioWmuData.SetMarkerStyle(20)
h_yieldratioWmuData.SetLineWidth(1)

h_yieldratioWmuMC = PlotTemplates.Save1DHisto(yieldratioWmuMC, c1, "Recoil", "Yield Ratio (Wmu/WJets)")
h_yieldratioWmuMC.SetMaximum(max)
h_yieldratioWmuMC.SetMinimum(min)
#h_yieldratioWmuMC.SetMarkerStyle(20)
#h_yieldratioWmuMC.SetMarkerColor(2)
h_yieldratioWmuMC.SetLineColor(2)
h_yieldratioWmuMC.SetLineWidth(1)

h_yieldratioWmuMC.Draw("e1")
h_yieldratioWmuData.Draw("e1same")

leg2 = PlotTemplates.SetLegend(coordinate_=[.15,.7,.47,.87])
leg2.AddEntry(h_yieldratioWmuMC, "MC")
leg2.AddEntry(yieldratioWmuData, "Data")
leg2.Draw()
E2 = PlotTemplates.drawenergy(is2017 = True, data=True)
for i in E2:
    i.Draw()

c2.cd()
#c2.Modified()
#c2.Update()
c2.SaveAs("Wmu_test.pdf")
c2.SaveAs("Topmu_test.png")

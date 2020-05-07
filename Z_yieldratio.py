#created by Fasya Khuzaimah on 2020.05.01

import ROOT
from ROOT import TFile, TH1F, TGraph, TGraphAsymmErrors

import PlotTemplates
from PlotTemplates import *

import array as arr

nbins = 4
edges = arr.array('f')
min = 0.0
max = 18.0
file = TFile("fitDiagnostics.root")


#------------------------ZEE------------------------------#

Zee = "shapes_fit_b/ZEE/"

#get the histogram inside shapes_fit_b/ZEE
ZeeDYjets = file.Get(Zee+"dyjets")
for i in range(nbins):
    low = ZeeDYjets.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
    #Error = ZeeDYjets.GetBinError(i+1)
    #print "ERROR_",i+1,Error
up = ZeeDYjets.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)
print edges

Zeedata = file.Get(Zee+"data")
dataZee = TH1F("dataZee","",nbins,edges)
nPointsZee = Zeedata.GetN()
for i in range(nPointsZee):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Zeedata.GetPoint(i, x, y)
    k = dataZee.FindFixBin(x)
    #print "y", y
    dataZee.SetBinContent(k, y)
    dataZee.SetBinError(i+1, Zeedata.GetErrorY(i))

Zeediboson = file.Get(Zee+"diboson")
ZeeST = file.Get(Zee+"singlet")
ZeeSMH = file.Get(Zee+"smh")
ZeeTT = file.Get(Zee+"tt")

'''
for i in range(nbins):
    ErrorWjet = WeWjets.GetBinError(i+1)
    print "W+jets error_",i+1, ErrorWjet
'''

DYjets_data_in_ZEE = dataZee - (Zeediboson + ZeeST + ZeeSMH + ZeeTT)

#-----------------------ZMUMU-----------------------------#

Zmumu = "shapes_fit_b/ZMUMU/"

#get the histogram inside shapes_fit_b/ZMUMU
Zmumudata = file.Get(Zmumu+"data")
dataZmumu = TH1F("dataZmumu","",nbins,edges)
nPointsZmumu = Zmumudata.GetN()
for i in range(nPointsZmumu):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Zmumudata.GetPoint(i, x, y)
    k = dataZmumu.FindFixBin(x)
    dataZmumu.SetBinContent(k,y)
    dataZmumu.SetBinError(i+1, Zmumudata.GetErrorY(i))
Zmumudiboson = file.Get(Zmumu+"diboson")
ZmumuST = file.Get(Zmumu+"singlet")
ZmumuSMH = file.Get(Zmumu+"smh")
ZmumuTT = file.Get(Zmumu+"tt")
ZmumuDYjets = file.Get(Zmumu+"dyjets")


DYjets_data_in_ZMUMU = dataZmumu - (Zmumudiboson + ZmumuST + ZmumuSMH + ZmumuTT)


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
SRtt = file.Get(SR+"tt")
SRwjets = file.Get(SR+"wjets")
SRzjets = file.Get(SR+"zjets")

Zjets_data_in_SR = dataSR - (SRdiboson + SRqcd + SRst + SRsmh + SRtt + SRwjets)


#----------------------yield ratio--------------------------#

#**********DATA*************#

yieldratioZeeData = DYjets_data_in_ZEE.Clone("yieldratioZeeData")
yieldratioZmumuData = DYjets_data_in_ZMUMU.Clone("yieldratioZmumuData")
yieldratioZeeData.Divide(Zjets_data_in_SR)#, 1.0, 1.0, "B")
yieldratioZmumuData.Divide(Zjets_data_in_SR)#, 1.0, 1.0, "B")

#print "Z ee data", yieldratioZeeData.GetBinContent(4)
#print "Z mumu data", yieldratioZmumuData.GetBinContent(4)

#***********MC************#

yieldratioZeeMC = ZeeDYjets.Clone("yieldratioZeeMC")
yieldratioZmumuMC = ZmumuDYjets.Clone("yieldratioZmumuMC")
yieldratioZeeMC.Divide(SRzjets)
yieldratioZmumuMC.Divide(SRzjets)

#print "Z ee MC", yieldratioZeeMC.GetBinContent(4)
#print "Z mumu MC", yieldratioZmumuMC.GetBinContent(4)

#-----------------Plot the Z ee yield ratio----------------#

c1 = PlotTemplates.myCanvas()

h_yieldratioZeeData = PlotTemplates.Save1DHisto(yieldratioZeeData, c1, "Recoil", "Yield Ratio (Zee/ZJets)")
h_yieldratioZeeData.SetMaximum(max)
h_yieldratioZeeData.SetMinimum(min)
h_yieldratioZeeData.SetMarkerStyle(20)
h_yieldratioZeeData.SetLineWidth(1)

h_yieldratioZeeMC = PlotTemplates.Save1DHisto(yieldratioZeeMC, c1, "Recoil", "Yield Ratio (Zee/ZJets)")
h_yieldratioZeeMC.SetMaximum(max)
h_yieldratioZeeMC.SetMinimum(min)
#h_yieldratioZeeMC.SetMarkerStyle(20)
#h_yieldratioZeeMC.SetMarkerColor(2)
h_yieldratioZeeMC.SetLineColor(2)
h_yieldratioZeeMC.SetLineWidth(1)

h_yieldratioZeeMC.Draw("e1")
h_yieldratioZeeData.Draw("e1same")

leg1 = PlotTemplates.SetLegend(coordinate_=[.15,.7,.47,.87])
leg1.AddEntry(h_yieldratioZeeMC, "MC")
leg1.AddEntry(h_yieldratioZeeData, "Data")
leg1.Draw()
E1 = PlotTemplates.drawenergy(is2017 = True, data=True)
for i in E1:
    i.Draw()

c1.cd()
#c1.Modified()
#c1.Update()
c1.SaveAs("Zee_test.pdf")
c1.SaveAs("Zee_test.png")


#----------------Plot the Z MuMu yield ratio----------------#

c2 = PlotTemplates.myCanvas()

h_yieldratioZmumuData = PlotTemplates.Save1DHisto(yieldratioZmumuData, c2, "Recoil", "Yield Ratio (Zmumu/ZJets)")
h_yieldratioZmumuData.SetMaximum(max)
h_yieldratioZmumuData.SetMinimum(min)
h_yieldratioZmumuData.SetMarkerStyle(20)
h_yieldratioZmumuData.SetLineWidth(1)

h_yieldratioZmumuMC = PlotTemplates.Save1DHisto(yieldratioZmumuMC, c1, "Recoil", "Yield Ratio (Zmumu/ZJets)")
h_yieldratioZmumuMC.SetMaximum(max)
h_yieldratioZmumuMC.SetMinimum(min)
#h_yieldratioZmumuMC.SetMarkerStyle(20)
#h_yieldratioZmumuMC.SetMarkerColor(2)
h_yieldratioZmumuMC.SetLineColor(2)
h_yieldratioZmumuMC.SetLineWidth(1)

h_yieldratioZmumuMC.Draw("e1")
h_yieldratioZmumuData.Draw("e1same")

leg2 = PlotTemplates.SetLegend(coordinate_=[.15,.7,.47,.87])
leg2.AddEntry(h_yieldratioZmumuMC, "MC")
leg2.AddEntry(h_yieldratioZmumuData, "Data")
leg2.Draw()
E2 = PlotTemplates.drawenergy(is2017 = True, data=True)
for i in E2:
    i.Draw()

c2.cd()
#c2.Modified()
#c2.Update()
c2.SaveAs("Zmumu_test.pdf")
c2.SaveAs("Zmumu_test.png")

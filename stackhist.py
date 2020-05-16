#created by Fasya Khuzaimah on 2020.05.14

import ROOT
from ROOT import TFile, TH1F, TGraph, TGraphAsymmErrors, THStack, TCanvas, TLegend, TPad, gStyle, gPad

import PlotTemplates
from PlotTemplates import *

import array as arr

# gethist function is under progress #
'''
def gethist(region, prefitbackgroundlist_, nbins=4, fname="fitDiagnostics.root"):
    
    openfile = TFile(fname)
    
    print region
    print " "
    
    prefit_path = "shapes_prefit/"+region+"/"
    postfit_path = "shapes_fit_b/"+region+"/"

    
    #get the histograms from prefit directory
    
    print prefit_path
    print " "
    
    allhist = []
    
    for j in prefitbackgroundlist_:
        allhist.append(openfile.Get(prefit_path + j))
    
    edges = arr.array('f')
    for i in range(nbins):
        low = allhist[0].GetXaxis().GetBinLowEdge(i+1)
        edges.append(low)
    up = allhist[0].GetXaxis().GetBinUpEdge(nbins)
    edges.append(up)
    #print edges

    data = openfile.Get(prefit_path + "data")
    datahist = TH1F("datahist","",nbins,edges)
    nPoints = data.GetN()
    for i in range(nPoints):
        x = ROOT.Double(0)
        y = ROOT.Double(0)
        data.GetPoint(i, x, y)
        k = datahist.FindFixBin(x)
        #print "y", y
        datahist.SetBinContent(k, y)
        datahist.SetBinError(i+1, data.GetErrorY(i))
    allhist.append(datahist)

    
    #get the histogram from post fit directory
    
    print postfit_path
    print " "

    totalBkgPostfit = openfile.Get(postfit_path + "total_background")
    allhist.append(totalBkgPostfit)


    return allhist
'''

def drawenergy():
    pt = TPaveText(0.1577181,0.905,0.9580537,0.96,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(52)
    
    cmstextSize = 0.07
    preliminarytextfize = cmstextSize * 0.7
    lumitextsize = cmstextSize *0.7
    pt.SetTextSize(cmstextSize)
    pt.AddText(0.01,0.57,"#font[61]{CMS}")
    
    pt1 = TPaveText(0.1777181,0.905,0.9580537,0.96,"brNDC")
    pt1.SetBorderSize(0)
    pt1.SetTextAlign(12)
    pt1.SetFillStyle(0)
    pt1.SetTextFont(52)
    pt1.SetTextSize(preliminarytextfize)
    #pt1.AddText(0.155,0.4,"Preliminary")
    pt1.AddText(0.125,0.45," Internal")
    
    pt2 = TPaveText(0.1877181,0.9045,1.1,0.96,"brNDC")
    pt2.SetBorderSize(0)
    pt2.SetTextAlign(12)
    pt2.SetFillStyle(0)
    pt2.SetTextFont(52)
    pt2.SetTextFont(42)
    pt2.SetTextSize(lumitextsize)
    pt2.AddText(0.53,0.5,"41.5 fb^{-1} (13 TeV)")
    
    return [pt, pt1, pt2]

def myPad():
    c = TCanvas("c", "", 800, 900)
    c.SetTopMargin(0.4)
    c.SetBottomMargin(0.05)
    c.SetRightMargin(0.1)
    c.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)
    
    padMain = TPad("padMain", "", 0.0, 0.25, 1.0, 0.97)
    padMain.SetTopMargin(0.4)
    padMain.SetRightMargin(0.05)
    padMain.SetLeftMargin(0.17)
    padMain.SetBottomMargin(0.0)
    padMain.SetTopMargin(0.1)
    
    padRatio = TPad("padRatio", "", 0.0, 0.0, 1.0, 0.25)
    padRatio.SetRightMargin(0.05)
    padRatio.SetLeftMargin(0.17)
    padRatio.SetTopMargin(0.0)
    padRatio.SetBottomMargin(0.3)
    padMain.Draw()
    padRatio.Draw()
    
    return [c, padMain, padRatio]

def myLegend(coordinate=[0.5,0.6,0.87,0.87], ncol=1):
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

def dataPredRatio(data_, totalBkg_):
    dataPredRatio_ = data_ - totalBkg_
    dataPredRatio_.Divide(totalBkg_)
    return dataPredRatio_

def myStack(colorlist_, backgroundlist_, signal_, prefit_, data_, postfit_, legendname_, pdfname_):
    leg = myLegend(ncol = 2)
    pad = myPad()
    
    pad[1].cd()

    data_.SetLineColor(1)
    data_.SetLineWidth(2)
    data_.SetMarkerStyle(20)
    data_.SetMarkerColor(1)
    data_.GetYaxis().SetLabelSize(0.04)
    data_.GetYaxis().SetTitleOffset(1.2)
    data_.GetYaxis().SetTitleSize(0.04)
    data_.GetYaxis().SetTitle("Events/(200)")
    leg.AddEntry(data_, "Data", "lep")
    data_.Draw("e1")
    
    hs = THStack("hs", "")
    for j in range(len(colorlist_)):
        h = backgroundlist_[j]
        h.SetFillColor(colorlist_[j])
        h.SetLineColor(colorlist_[j])
        hs.Add(h, "")
        leg.AddEntry(h,legendname_[j],"f")
    #hs.GetYaxis().SetLabelSize(0.04)
    #hs.GetYaxis().SetTitleOffset(1.2)
    #hs.GetYaxis().SetTitleSize(0.04)
    #hs.GetYaxis().SetTitle("Events/(200)")
    hs.Draw("same")
    data_.Draw("e1same")

    signal_.SetLineColor(4)
    signal_.SetLineWidth(3)
    signal_.SetMarkerStyle(21)
    signal_.SetMarkerColor(2)
    leg.AddEntry(signal_, "Signal", "l")
    signal_.Draw("histsame")

    postfit_.SetLineColor(634)
    postfit_.SetLineWidth(3)
    postfit_.GetXaxis().SetLabelSize(0.07)
    postfit_.GetYaxis().SetLabelSize(0.06)
    postfit_.GetYaxis().SetTitleOffset(0.1)
    leg.AddEntry(postfit_, "Post-fit", "l")
    postfit_.Draw("histsame")

    leg.Draw()

    drawE = drawenergy()
    for i in drawE:
        i.Draw()

    pad[2].cd()

    leg1 = myLegend(coordinate=[0.5,0.35,0.87,0.55])
    leg1.SetTextSize(0.1)

    prefithist = dataPredRatio(data_ = data_, totalBkg_ = prefit_)
    prefithist.SetLineColor(1)
    prefithist.SetLineWidth(2)
    prefithist.GetXaxis().SetLabelSize(0.115)
    prefithist.GetXaxis().SetTitleOffset(1)
    prefithist.GetXaxis().SetTitleSize(0.115)
    prefithist.GetYaxis().SetLabelSize(0.1)
    prefithist.GetYaxis().SetTitleOffset(0.5)
    prefithist.GetYaxis().SetTitleSize(0.115)
    prefithist.GetYaxis().SetTitle("#frac{Data-Pred}{Pred}")
    prefithist.GetXaxis().SetTitle("Recoil (GeV)")
    leg1.AddEntry(prefithist, "Prefit", "lep")
    prefithist.Draw("e1")

    postfithist = dataPredRatio(data_ = data_, totalBkg_ = postfit_)
    postfithist.SetLineColor(4)
    postfithist.SetLineWidth(2)
    postfithist.GetYaxis().SetTitle("#frac{Data-Pred}{Pred}")
    postfithist.GetXaxis().SetTitle("Recoil (GeV)")
    leg1.AddEntry(postfithist, "Postfit", "lep")
    postfithist.Draw("e1same")

    leg1.Draw()

    pad[0].Modified()
    pad[0].Update()
    pad[0].SaveAs(pdfname_+".pdf")

# Finish defining functions #
#--------------------------------------------------------------------------------#




nbins = 4
edges = arr.array('f')
#min = 0.0
#max = 10.0
openfile = TFile("fitDiagnostics.root")


#------------------------shapes_prefit/SR------------------------------#
prefitpathSR = "shapes_prefit/SR/"
    
bkglist = []
    
#get the histograms in shapes_prefit/SR
    
dibosonSR = openfile.Get(prefitpathSR+"diboson")
bkglist.append(dibosonSR)
qcdSR = openfile.Get(prefitpathSR+"qcd")
bkglist.append(qcdSR)
stSR = openfile.Get(prefitpathSR+"singlet")
bkglist.append(stSR)
smhSR = openfile.Get(prefitpathSR+"smh")
bkglist.append(smhSR)
ttSR = openfile.Get(prefitpathSR+"tt")
bkglist.append(ttSR)
wjetsSR = openfile.Get(prefitpathSR+"wjets")
bkglist.append(wjetsSR)
zjetsSR = openfile.Get(prefitpathSR+"zjets")
bkglist.append(zjetsSR)
    
signalSR = openfile.Get(prefitpathSR+"signal")
prefitSR = openfile.Get(prefitpathSR+"total_background")
    
for i in range(nbins):
    low = dibosonSR.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
up = dibosonSR.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)
    
dataSR = openfile.Get(prefitpathSR+"data")
datahistSR = TH1F("datahistSR","",nbins,edges)
nPointsSR = dataSR.GetN()
for i in range(nPointsSR):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    dataSR.GetPoint(i, x, y)
    k = datahistSR.FindFixBin(x)
    datahistSR.SetBinContent(k,y)
    datahistSR.SetBinError(i+1, dataSR.GetErrorY(i))
    
    
postfitpathSR = "shapes_fit_b/SR/"
    
#get the histogram in shapes_fit_b/SR
    
postfitSR = openfile.Get(postfitpathSR + "total_background")

#Make the Stack#

#["diboson", "qcd", "singlet", "smh", "tt", "wjets", "zjets"]
makeStack = myStack(colorlist_=[874, 922, 802, 422, 799, 6, 811], backgroundlist_ = bkglist, legendname_ = ["WWW/WZ/ZZ", "QCD", "Single t", "SM H", "t#bar{t}", "W(l#nu)+jets", "Z(ll)+jets"], data_ = datahistSR, signal_ = signalSR, prefit_ = prefitSR, postfit_ = postfitSR, pdfname_="SRtest")



# SR

#SRhist = gethist(region="SR", prefitbackgroundlist_ = ["diboson", "qcd", "singlet", "smh", "tt", "wjets", "zjets", "signal", "total_background"], nbins=4, fname="fitDiagnostics.root")

#makeStack = myStack(colorlist_=[4, 922, 802, 422, 799, 6, 812], backgroundlist_ = SRhist, legendname_ = ["WWW/WZ/ZZ", "QCD", "Single t", "SM h", "t#bar{t}", "W(l#nu)+jets", "Z(ll)+jets"], signal_ = SRhist[7], prefit_ = SRhist[8], data_ = SRhist[9], postfit_ = SRhist[10], pdfname_="SRtest")

//
//  pulls.cpp
//  
//
//  Created by Fasya Khuzaimah on 08.05.20.
//

void pulls(){
    TFile file("pulls.root","READ");
    TCanvas *c = (TCanvas*)file.Get("nuisances");
    c->ls(); //check inside the c canvas
    c->Size(1250,400);
    c->SetBottomMargin(0.35);
    gStyle->SetOptStat(0);
    gStyle->SetOptTitle(0);
    
    TH1F *h1 = (TH1F*)c->GetPrimitive("prefit_nuisancs");
    h1->LabelsOption("v");
    
    TLegend leg1 = TLegend(0.6, 0.74, 0.89, 0.89);
    TLegend *leg2 = (TLegend*)(c->GetPrimitive("TPave"));
    leg1.Copy(*leg2);
    
    TPaveText *pt = new TPaveText(0.0877181,0.9,0.9580537,0.96,"brNDC");
    pt->SetBorderSize(0);
    pt->SetTextAlign(12);
    pt->SetFillStyle(0);
    pt->SetTextFont(52);
    
    double cmstextSize = 0.07;
    double preliminarytextfize = cmstextSize * 0.7;
    double lumitextsize = cmstextSize *0.7;
    pt->SetTextSize(cmstextSize);
    pt->AddText(0.01,0.57,"#font[61]{CMS}");
    
    TPaveText *pt1 = new TPaveText(0.0877181,0.905,0.9580537,0.96,"brNDC");
    pt1->SetBorderSize(0);
    pt1->SetTextAlign(12);
    pt1->SetFillStyle(0);
    pt1->SetTextFont(52);
    
    pt1->SetTextSize(preliminarytextfize);
    //pt1->AddText(0.155,0.4,"Preliminary");
    pt1->AddText(0.125,0.4,"Internal");
    
    TPaveText *pt2 = new TPaveText(0.0877181,0.9,0.8480537,0.96,"brNDC");
    pt2->SetBorderSize(0);
    pt2->SetTextAlign(12);
    pt2->SetFillStyle(0);
    pt2->SetTextFont(52);
    pt2->SetTextFont(42);
    pt2->SetTextSize(lumitextsize);
    pt2->AddText(0.81, 0.5, "41 fb^{-1} (13 TeV)");
    
    h1->Draw("same");
    leg2->Draw();
    pt->Draw();
    pt1->Draw();
    pt2->Draw();
    
    c->Update();
    c->Modified();
    c->SaveAs("pulls.pdf");
}

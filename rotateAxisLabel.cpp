//
//  rotateAxisLabel.cpp
//  
//
//  Created by Fasya Khuzaimah on 08.05.20.
//

void rotateAxisLabel(){
    TFile file("pulls.root","READ");
    TCanvas *c = (TCanvas*)file.Get("nuisances");
    c->ls(); //check inside the c canvas
    gPad->GetListOfPrimitives()->Print();
    c->Size(1250,400);
    c->SetBottomMargin(0.35);
    //gStyle->SetOptStat(0);
    TH1F *h1 = (TH1F*)c->GetPrimitive("prefit_nuisancs");
    h1->LabelsOption("v");
    h1->Draw("same");
    c->Update();
    c->Modified();
    c->SaveAs("pulls.pdf");
    //c->SaveAs("pulls_noStatisticsBox.pdf");
}

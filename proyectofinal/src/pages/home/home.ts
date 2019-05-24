import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';
import { InfoPage } from '../info/info';
import { BuscarPage } from '../buscar/buscar';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  maestros =[];
  infoPag = InfoPage
  BUSCA = BuscarPage
  constructor(public navCtrl: NavController,public http:HttpClient) {
    this.http.get('/v1/').subscribe(data =>{
      this.maestros=data['Maestros'];
      console.log(JSON.stringify(this.maestros));
    },error => {
      console.log(JSON.stringify(error));
    });

  }
  info(maestro){
    this.navCtrl.push(this.infoPag,{maestro:maestro});
  }
  search(){
    this.navCtrl.push(this.BUSCA,{maestro:this.maestros})
  }
 

}

import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { InfoPage } from '../info/info';

/**
 * Generated class for the BuscarPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-buscar',
  templateUrl: 'buscar.html',
})
export class BuscarPage {
  lista = [];
  mastro = [];
  infoPage = InfoPage
  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.lista = this.navParams.get('maestro')
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad BuscarPage');
  }
  getItems(ev: any) {
    console.log(ev.target.value);
    let nom_profe = ev.target.value.toLowerCase();
    this.mastro = this.lista.filter(mae => {
      return mae.Mombre_materia.toLowerCase().includes(nom_profe) || mae.Nombre_maestro.toLowerCase().includes(nom_profe)
    });
    console.log(JSON.stringify(this.mastro));
  }
  info(maestro){
    this.navCtrl.push(this.infoPage, {maestro: maestro});
}



}

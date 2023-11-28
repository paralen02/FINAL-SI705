import { IngredientService } from './../../../services/ingredient.service';
import { Component, OnInit } from '@angular/core';
import { ChartDataset, ChartOptions, ChartType } from 'chart.js';

@Component({
  selector: 'app-reporte01',
  templateUrl: './reporte01.component.html',
  styleUrls: ['./reporte01.component.css'],
})
export class Reporte01Component implements OnInit {
  barChartOptions: ChartOptions = {
    responsive: true,
  };
  barChartLabels: string[] = [];
  barChartType: ChartType = 'bar';
  barChartLegend = true;
  barChartData: ChartDataset[] = [];
  constructor(private iS: IngredientService) {}
  ngOnInit(): void {
    this.iS.getCount().subscribe((data) => {
      this.barChartLabels = data.map((item) => item.nameDessert);
      this.barChartData=[
        {
          data:data.map(item=>item.quantityIngredients),
          label:'Cantidad de Ingredientes',
          backgroundColor:'rgba(0,0,255,0.3)'
        }
      ]
    });
  }
}

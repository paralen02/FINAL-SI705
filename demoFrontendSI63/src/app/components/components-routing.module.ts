import { ReporteComponent } from './reporte/reporte.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DessertComponent } from './dessert/dessert.component';
import { CreaeditaDessertComponent } from './dessert/creaedita-dessert/creaedita-dessert.component';
import { ReporteDessertComponent } from './dessert/reporte-dessert/reporte-dessert.component';
import { IngredientComponent } from './ingredient/ingredient.component';
import { CreaeditaIngredientComponent } from './ingredient/creaedita-ingredient/creaedita-ingredient.component';

const routes: Routes = [
  {
    path: 'postres',
    component: DessertComponent,
    children: [
      { path: 'nuevo', component: CreaeditaDessertComponent },
      { path: 'ediciones/:id', component: CreaeditaDessertComponent },
      { path: 'reporte', component: ReporteDessertComponent },
    ],
  },
  {
    path: 'ingredients',
    component: IngredientComponent,
    children: [{ path: 'nuevo', component: CreaeditaIngredientComponent }],
  },
  {
    path: 'reportes',
    component: ReporteComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ComponentsRoutingModule {}

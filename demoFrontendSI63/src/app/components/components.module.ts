import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatListModule } from '@angular/material/list';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ComponentsRoutingModule } from './components-routing.module';
import { DessertComponent } from './dessert/dessert.component';
import { CreaeditaDessertComponent } from './dessert/creaedita-dessert/creaedita-dessert.component';
import { ListarDessertComponent } from './dessert/listar-dessert/listar-dessert.component';
import { ReporteDessertComponent } from './dessert/reporte-dessert/reporte-dessert.component';
import { CreaeditaIngredientComponent } from './ingredient/creaedita-ingredient/creaedita-ingredient.component';
import { ListarIngredientComponent } from './ingredient/listar-ingredient/listar-ingredient.component';
import { IngredientComponent } from './ingredient/ingredient.component';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatNativeDateModule } from '@angular/material/core';
import { MatTableModule } from '@angular/material/table';
import { MatSelectModule } from '@angular/material/select';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { ReporteComponent } from './reporte/reporte.component';
import { Reporte01Component } from './reporte/reporte01/reporte01.component';
import { NgChartsModule } from 'ng2-charts';


@NgModule({
  declarations: [
    DessertComponent,
    CreaeditaDessertComponent,
    ListarDessertComponent,
    ReporteDessertComponent,
    IngredientComponent,
    CreaeditaIngredientComponent,
    ListarIngredientComponent,
    ReporteComponent,
    Reporte01Component,
  ],
  imports: [
    CommonModule,
    ComponentsRoutingModule,
    MatListModule,
    MatDatepickerModule,
    MatPaginatorModule,
    MatNativeDateModule,
    MatTableModule,
    MatSelectModule,
    FormsModule,
    ReactiveFormsModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    NgChartsModule
  ]
})
export class ComponentsModule { }

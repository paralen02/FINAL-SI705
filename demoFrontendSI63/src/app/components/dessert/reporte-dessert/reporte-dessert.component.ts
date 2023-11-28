import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { Dessert } from 'src/app/models/dessert';
import { DessertService } from 'src/app/services/dessert.service';

@Component({
  selector: 'app-reporte-dessert',
  templateUrl: './reporte-dessert.component.html',
  styleUrls: ['./reporte-dessert.component.css']
})
export class ReporteDessertComponent implements OnInit {
  dataSource: MatTableDataSource<Dessert> = new MatTableDataSource<Dessert>();
  fechaForm: FormGroup = new FormGroup({});
  mensaje: string = '';
  fechaVacia: boolean = false;

  displayedColumns: string[] = ['codigo', 'postre', 'tipo', 'calorias'];

  constructor(private dS: DessertService, private formBuilder: FormBuilder) {}

  ngOnInit() {
    this.fechaForm = this.formBuilder.group({
      fecha: [null, Validators.required],
    });
  }

 
  buscar() {
    if (this.fechaForm.valid) {
      const fechas = this.fechaForm.value.fecha.toISOString().substring(0, 10);
      this.dS.buscar(fechas).subscribe((data) => {        
        this.dataSource.data = data;       
        if (data.length === 0) {
          this.mensaje = "No se encontraron resultados para la fecha seleccionada.";
        } else {
          this.mensaje = '';
        }
      });
    } else {
      if (this.fechaForm.get('fecha')?.hasError('required')) {
        this.mensaje = 'Por favor, ingrese una fecha.';
      }
    }
}


  obtenerControlCampo(nombreCampo: string): AbstractControl {
    const control = this.fechaForm.get(nombreCampo);
    if (!control) {
      throw new Error(`Control no encontrado para el campo ${nombreCampo}`);
    }
    return control;
  }
}

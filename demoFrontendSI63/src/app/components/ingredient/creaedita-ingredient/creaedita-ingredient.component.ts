import { IngredientService } from './../../../services/ingredient.service';
import { Router } from '@angular/router';
import { DessertService } from './../../../services/dessert.service';
import { Dessert } from './../../../models/dessert';
import { Ingredient } from './../../../models/ingredient';
import { FormGroup, FormBuilder, Validators, AbstractControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-creaedita-ingredient',
  templateUrl: './creaedita-ingredient.component.html',
  styleUrls: ['./creaedita-ingredient.component.css']
})
export class CreaeditaIngredientComponent implements OnInit {
  form: FormGroup = new FormGroup({});
  ing: Ingredient = new Ingredient()
  mensaje: string = '';
  tiposingredientes: { value: string; viewValue: string }[] = [
    { value: 'Vegetal', viewValue: 'Vegetal' },
    { value: 'Proteina', viewValue: 'Proteina' },
  ];
  listaPostres: Dessert[] = []

  constructor(
    private dS: DessertService,
    private router: Router,
    private formBuilder: FormBuilder,
    private iS: IngredientService
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      nameIngredient: ['', Validators.required],
      amountIngredient: ['', Validators.required],
      typeIngredient: ['', Validators.required],
      dessert: ['', Validators.required]
    });
    this.dS.list().subscribe(data => {
      this.listaPostres = data;
    })

  }

  aceptar(): void {
    if (this.form.valid) {
      this.ing.nameIngredient = this.form.value.nameIngredient;
      this.ing.amountIngredient = this.form.value.amountIngredient;
      this.ing.typeIngredient = this.form.value.typeIngredient;
      this.ing.dessert.idDessert = this.form.value.dessert;

      this.iS.insert(this.ing).subscribe(data => {
        this.iS.list().subscribe(data => {
          this.iS.setList(data)
        })
      })
      this.router.navigate(['components/ingredients'])
    } else {
      this.mensaje = 'Ingrese todos los campos!!'
    }
  }
  obtenerControlCampo(nombreCampo: string): AbstractControl {
    const control = this.form.get(nombreCampo);
    if (!control) {
      throw new Error(`Control no encontrado para el campo ${nombreCampo}`);
    }
    return control;

  }
}

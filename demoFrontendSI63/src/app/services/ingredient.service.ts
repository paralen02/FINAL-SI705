import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { Ingredient } from './../models/ingredient';
import { environment } from './../../environments/environment';
import { Injectable } from '@angular/core';
import { QuantityIngredientsDTO } from '../models/QuantityIngredientsDTO';
const base_url = environment.base;

@Injectable({
  providedIn: 'root',
})
export class IngredientService {
  private url = `${base_url}/ingredientes`;
  private listaCambio = new Subject<Ingredient[]>();
  constructor(private http: HttpClient) {}
  list() {
    let token = sessionStorage.getItem('token');

    return this.http.get<Ingredient[]>(this.url, {
      headers: new HttpHeaders()
        .set('Authorization', `Bearer ${token}`)
        .set('Content-Type', 'application/json'),
    });
  }
  insert(i: Ingredient) {
    let token = sessionStorage.getItem('token');

    return this.http.post(this.url, i, {
      headers: new HttpHeaders()
        .set('Authorization', `Bearer ${token}`)
        .set('Content-Type', 'application/json'),
    });
  }
  setList(listaNueva: Ingredient[]) {
    this.listaCambio.next(listaNueva);
  }

  getList() {
    return this.listaCambio.asObservable();
  }

  getCount(): Observable<QuantityIngredientsDTO[]> {
    let token = sessionStorage.getItem('token');
    return this.http.get<QuantityIngredientsDTO[]>(`${this.url}/cantidades`, {
      headers: new HttpHeaders()
        .set('Authorization', `Bearer ${token}`)
        .set('Content-Type', 'application/json'),
    });
  }
}

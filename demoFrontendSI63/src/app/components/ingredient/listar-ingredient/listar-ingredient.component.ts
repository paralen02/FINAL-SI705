import { IngredientService } from './../../../services/ingredient.service';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { Ingredient } from './../../../models/ingredient';
import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-listar-ingredient',
  templateUrl: './listar-ingredient.component.html',
  styleUrls: ['./listar-ingredient.component.css']
})
export class ListarIngredientComponent implements OnInit {

  dataSource: MatTableDataSource<Ingredient> = new MatTableDataSource();
  displayedColumns: string[] =
    ['codigo', 'ingrediente', 'cantidad', 'tipo', 'postre'];
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  constructor(private iS: IngredientService) {

  }
  ngOnInit(): void {
    this.iS.list().subscribe(data => {
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.paginator = this.paginator;
    })
    this.iS.getList().subscribe((data) => {
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.paginator = this.paginator;

    });
  }
}

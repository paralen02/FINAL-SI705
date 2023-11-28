import { DessertService } from './../../../services/dessert.service';
import { Dessert } from './../../../models/dessert';
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
@Component({
  selector: 'app-listar-dessert',
  templateUrl: './listar-dessert.component.html',
  styleUrls: ['./listar-dessert.component.css'],
})
export class ListarDessertComponent implements OnInit {
  dataSource: MatTableDataSource<Dessert> = new MatTableDataSource();
  displayedColumns: string[] =
  ['codigo', 'dulce', 'fecha', 'tipo', 'calorias','accion01','accion02'];
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  constructor(private dS: DessertService) {}

  ngOnInit(): void {
    this.dS.list().subscribe((data) => {
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.paginator = this.paginator;
    });
    this.dS.getList().subscribe((data) => {
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.paginator = this.paginator;

    }); 
  }
  eliminar(id: number) {
    this.dS.delete(id).subscribe((data) => {
      this.dS.list().subscribe((data) => {
        this.dS.setList(data);
      });
    });
  }
  filter(en: any) {
    this.dataSource.filter = en.target.value.trim();
  }
}

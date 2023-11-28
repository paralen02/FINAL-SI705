import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-dessert',
  templateUrl: './dessert.component.html',
  styleUrls: ['./dessert.component.css'],
})
export class DessertComponent {
  constructor(public route: ActivatedRoute) {}

  ngOnInit(): void {}
}

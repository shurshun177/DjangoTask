import { Component, OnInit } from '@angular/core';
import {MyExpense} from "./MyExpense";
import {MyexpensesService} from "./myexpenses.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title: 'my-app';
  myexpenses: MyExpense[];

  constructor(private  myexpensesService:MyexpensesService){

  }
  ngOnInit(){
    this.getMyExpenses();
  }

  getMyExpenses():void{
    this.myexpensesService.list().subscribe(myexpenses=>this.myexpenses = myexpenses)
  }

  add(title: string, sum: number): void {
  if (!title || !sum) { return; }
//   var param1 = title;
//   var param2 = sum;
//   var entry:MyExpense = {
//     title,
//     sum
// };
  this.myexpensesService.addExpense({ title, sum } as MyExpense)
    .subscribe(expense => {
      this.myexpenses.push(expense);
    });
}
}

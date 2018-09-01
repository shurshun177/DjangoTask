import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Observable, of } from 'rxjs';
import { MyExpense } from './MyExpense';
import {tap} from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})

export class MyexpensesService {
  private readonly LIST_URL = "http://127.0.0.1:8000/expenses/list/";
  private readonly NEW_URL = "http://127.0.0.1:8000/expense/new/";

  constructor(
    protected httpClient: HttpClient,
  ) {}


  public list(): Observable<Array<MyExpense>> {
    return this.httpClient.get<Array<MyExpense>>(this.LIST_URL);
  }
  /** POST: add a new hero to the server */
  public addExpense (expense: MyExpense): Observable<MyExpense> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
      })
    };
    const body = new HttpParams()
      .set('title', expense.title)
      .set('sum', expense.sum.toString());
    return this.httpClient.post<MyExpense>(this.NEW_URL, body, httpOptions);
  }
}

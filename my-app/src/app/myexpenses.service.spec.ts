import { TestBed, inject } from '@angular/core/testing';

import { MyexpensesService } from './myexpenses.service';

describe('MyexpensesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MyexpensesService]
    });
  });

  it('should be created', inject([MyexpensesService], (service: MyexpensesService) => {
    expect(service).toBeTruthy();
  }));
});

import { TestBed, inject } from '@angular/core/testing';

import { MembershipService } from './membership.service';

describe('MembershipService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MembershipService]
    });
  });

  it('should ...', inject([MembershipService], (service: MembershipService) => {
    expect(service).toBeTruthy();
  }));
});

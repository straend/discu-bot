import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DiscussiondetailComponent } from './discussiondetail.component';

describe('DiscussiondetailComponent', () => {
  let component: DiscussiondetailComponent;
  let fixture: ComponentFixture<DiscussiondetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DiscussiondetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DiscussiondetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

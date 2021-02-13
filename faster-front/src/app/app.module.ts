import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ChannelsComponent } from './channels/channels.component';
import { MatTooltipModule } from '@angular/material/tooltip';
import { HttpClientModule } from '@angular/common/http';
import { DiscussionlistComponent } from './discussionlist/discussionlist.component';
import { DiscussiondetailComponent } from './discussiondetail/discussiondetail.component';

import { MatTableModule } from '@angular/material/table';
import { MatListModule } from '@angular/material/list'; 


@NgModule({
  declarations: [
    AppComponent,
    ChannelsComponent,
    DiscussionlistComponent,
    DiscussiondetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTooltipModule,
    HttpClientModule,
    MatTableModule,
    MatListModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

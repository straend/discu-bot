import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ChannelsComponent } from './channels/channels.component';
import { DiscussionlistComponent } from './discussionlist/discussionlist.component';
import { DiscussiondetailComponent } from './discussiondetail/discussiondetail.component';


const routes: Routes = [
  { path: '', component: ChannelsComponent },
  { path: ':channel_name', component: DiscussionlistComponent },
  { path: ':channel_name/:discussion_id', component: DiscussiondetailComponent },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

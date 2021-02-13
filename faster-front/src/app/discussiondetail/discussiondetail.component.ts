import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Observable } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { Channel } from '../channel';
import { Discussion } from '../discussion';
import { Message } from '../message';
import { ChannelService } from '../channel.service';
import {MatTableDataSource} from '@angular/material/table';

@Component({
  selector: 'app-discussiondetail',
  templateUrl: './discussiondetail.component.html',
  styleUrls: ['./discussiondetail.component.css']
})
export class DiscussiondetailComponent implements OnInit {
  discussion: Discussion;
  
  messages: Message[] = [];
  dataSource = new MatTableDataSource(this.messages);
  columnsToDisplay: string[] = ['when', 'author__nick', 'text' ];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private channelService: ChannelService
  ) { }

  getInfo(discussion_id: number): void {
    this.channelService.getDiscussion(discussion_id)
        .subscribe(discussion => {
          this.discussion = discussion;
          this.dataSource = new MatTableDataSource(discussion.messages);
      });
  }
  ngOnInit(): void {
    const discussion_id: number = Number(this.route.snapshot.params.discussion_id);

    this.getInfo(discussion_id);
  }

}


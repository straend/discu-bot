import { Component, OnInit } from '@angular/core';

import { Channel } from '../channel';
import { Discussion } from '../discussion';
import { ChannelService } from '../channel.service';
import {MatTableDataSource} from '@angular/material/table';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-discussionlist',
  templateUrl: './discussionlist.component.html',
  styleUrls: ['./discussionlist.component.css']
})
export class DiscussionlistComponent implements OnInit {

  channel: Channel;
  discussions: Discussion[] = [];

  columnsToDisplay: string[] = ['time_start', 'starter__nick', 'topic' ];
  dataSource = new MatTableDataSource(this.discussions); //= new MatTableDataSource(Discussion[]);
  getInfo(channel_name: string): void {
    this.channelService.getChannel(channel_name)
        .subscribe(channel => {
          this.channel = channel;
          this.dataSource = new MatTableDataSource(channel.discussions);
          console.log(this.dataSource);
        });
  }
  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private channelService: ChannelService
  ) { }

  ngOnInit(): void {
    const channel_name: string = this.route.snapshot.params.channel_name;
    this.getInfo(channel_name);
    
  }

}

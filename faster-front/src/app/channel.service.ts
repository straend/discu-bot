import { environment } from '../environments/environment';

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';

import { Channel } from './channel';
import { Discussion } from './discussion';

@Injectable({
  providedIn: 'root'
})
export class ChannelService {

  constructor( private http: HttpClient) { }
  //private apiBaseUrl = '//api.discobot.t.fik1.net/';  // URL to web api
  private apiBaseUrl = environment.CHANNEL_API_URL;  // URL to web api
  
  /** GET heroes from the server */
  getChannels(): Observable<Channel[]> {
    return this.http.get<Channel[]>(this.apiBaseUrl+"/channels")
  }
  getChannel(channel_name: string): Observable<Channel> {
    return this.http.get<Channel>(this.apiBaseUrl+"/channels/"+channel_name)
  }
  getDiscussion(discussion_id: number): Observable<Discussion> {
    return this.http.get<Discussion>(this.apiBaseUrl+"/discussions/"+discussion_id)
  }
}

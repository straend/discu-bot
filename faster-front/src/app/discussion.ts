import { Author } from './author';
import { Channel } from './channel';
import { Message } from './message';

export interface Discussion {
    id: number;
    topic: string;
    time_start: Date;
    time_end: Date;
    author: Author;
    channel: Channel;
    messages: Message[];
}

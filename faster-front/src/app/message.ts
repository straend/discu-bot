import { Author } from './author';
import { Channel } from './channel';

export interface Message {
    id: number;
    text: string;
    when: Date;
    author: Author;
    channel: Channel;
}

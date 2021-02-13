import { Discussion } from './discussion';

export interface Channel {
    id: number;
    name: string;
    discussions: Discussion[];

  }
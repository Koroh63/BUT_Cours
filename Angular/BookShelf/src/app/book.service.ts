import { Injectable } from '@angular/core';
import { Book } from './book/book';
import { BOOK } from './book/book.mock';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  constructor() {}

  getBooks() : Book[]{
    return BOOK;
  }

}

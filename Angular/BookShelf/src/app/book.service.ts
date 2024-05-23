import { Injectable } from '@angular/core';
import { Book } from './book/book';
import { BOOK } from './book/book.mock';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  books : Book[] = BOOK;
  constructor() {}

  getBooks() : Book[]{
    return BOOK;
  }

  addBooks(book:Book): boolean{
    try{
      this.books.push(book);
    }catch{
      return false
    }
    return true
  } 

}

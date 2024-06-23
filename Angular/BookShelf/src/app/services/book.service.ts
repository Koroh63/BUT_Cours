import { Injectable } from '@angular/core';
import { Book } from '../model/book.model';
import { bookStub } from '../data/stub';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  private books: Book[] = bookStub;

  constructor() { }


  getBooks(): Book[] {
    return this.books;
  }

  addBook(book : Book){
    this.books.push(book)
  }
}

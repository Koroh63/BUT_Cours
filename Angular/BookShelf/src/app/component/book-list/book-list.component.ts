import { Component } from '@angular/core';
import { Book } from '../../model/book.model';
import { BookService } from '../../services/book.service';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [NgFor],
  providers: [BookService],
  templateUrl: './book-list.component.html',
  styleUrl: './book-list.component.css'
})
export class BookListComponent {

  books: Book[] = [];

  constructor(protected bookService: BookService){

  }

  ngOnInit(){
    this.books = this.bookService.getBooks();
  }

  addBook(book : Book){
    this.books.push(book)
    this.bookService.addBook(book)
  }
}

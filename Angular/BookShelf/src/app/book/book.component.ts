import { Component } from '@angular/core';
import { Book } from './book';
import { BOOK } from './book.mock';
import { NgFor } from '@angular/common';
import { BookService } from '../book.service';

@Component({
  selector: 'app-book',
  standalone: true,
  imports: [NgFor],
  templateUrl: './book.component.html',
  styleUrl: './book.component.css'
})
export class BookComponent {

  constructor(private bookService : BookService){}

  ngOnInit():void {
    this.getBooks()
  }
  books : Book[] = []

  getBooks() : void {
    this.books = this.bookService.getBooks()
  }
}


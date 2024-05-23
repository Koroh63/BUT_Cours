import { Component } from '@angular/core';
import { Book } from './book';
import { BOOK } from './book.mock';
import { NgFor } from '@angular/common';
import { BookService } from '../book.service';
import { JsonpClientBackend } from '@angular/common/http';

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

/*
Joan 2 + 1 + 3 + 0.5 + 2 + 2 + 4 + 2 + 2 + 4 + 2 + 3 + 1 + 2 + 2 + 2 + 6 + 4 + 5 + 8 + 4 + 10 + 4 + 7 + 7 = 89.5
Corentin 2 + 1 +0.5 + 1 + 3 + 0.5 + 2 + 2 + 0.2 + 1 + 4 + 3 + 1 + 2 + 2 + 1 + 2 +2 +2 + 2 + 10 + 13 + 4 +10 + 2 + 6 + 7.5 = 86.7
Dorian 2 + 1 + 2 + 0.5 + 2 + 2 + 6 + 2 + 3 + 3 + 1 + 1 + 2 + 6 + 20 + 5 + 4 +9.5 + 4 + 6 + 12 + 1 = 95
Jérémy 2 + 1 + 3 + 0.5 + 2 + 2 + 2 + 4 +2 + 2 +2 + 3 + 2 + 2 + 2 + 9 + 10 + 8.5 + 14 + 4 + 9 + 1 = 87

*/


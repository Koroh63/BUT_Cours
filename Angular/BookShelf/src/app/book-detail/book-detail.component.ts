import { Component, Input, OnInit } from '@angular/core';
import { Book } from '../book/book';
import { BookService } from '../book.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-book-detail',
  standalone: true,
  imports: [],
  templateUrl: './book-detail.component.html',
  styleUrl: './book-detail.component.css'
})
export class BookDetailComponent implements OnInit{
  
  bookSelected : Book | null = null;
  bookId: string | null = null;
  constructor(private bookService : BookService, private route: ActivatedRoute){}

  ngOnInit(): void {
    this.bookId = this.route.snapshot.paramMap.get('id');
    if(this.bookId!=null)
    this.bookSelected = this.bookService.getBookById(parseInt(this.bookId))
  }
}

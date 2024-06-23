import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BookListComponent } from './component/book-list/book-list.component';
import { BookFormComponent } from './component/book-form/book-form.component';
import { Book } from './model/book.model';
import { BookService } from './services/book.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, BookListComponent,BookFormComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  
  constructor(private bookService : BookService){}
  
  title = 'BookShelf';

  addBook($event: Book){
    this.bookService.addBook($event)
  }
}

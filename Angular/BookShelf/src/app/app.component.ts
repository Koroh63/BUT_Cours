import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BookComponent } from './book/book.component';
import { BookFormComponent } from './book-form/book-form.component';



@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,BookComponent,BookFormComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'BookShelf';


  addBook(){
    
  }
}


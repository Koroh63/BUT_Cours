import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { BookComponent } from './book/book.component';
import { BookFormComponent } from './book-form/book-form.component';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,BookComponent,BookFormComponent, RouterLink,RouterLinkActive, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'BookShelf';


  addBook(){
    
  }
}


import { Component, EventEmitter, Output } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { BookService } from '../book.service';
import { Book } from '../book/book';


@Component({
  selector: 'app-book-form',
  template: `
    Favorite Color: <input type="text" [formControl]="favoriteColorControl">
  `,
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './book-form.component.html',
  styleUrl: './book-form.component.css'
})
export class BookFormComponent {

  constructor(private bookService : BookService){}
    bookForm =new FormGroup({
      title: new FormControl(''),
      author: new FormControl(''),
      publicationDate: new FormControl('')
    });

  @Output() messageEmitter = new EventEmitter<Book>();


  submitBook(){

    if(true){
      console.log()
    }else{
      // this.messageEmitter.emit({})
      // print(this.bookForm.title)
    }

  }
}

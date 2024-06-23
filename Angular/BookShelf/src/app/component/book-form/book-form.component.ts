import { Component, EventEmitter, Output } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Book } from '../../model/book.model';

@Component({
  selector: 'app-book-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './book-form.component.html',
  styleUrls: ['./book-form.component.css']
})
export class BookFormComponent {
  @Output() formSubmitted = new EventEmitter<Book>();

  bookForm = new FormGroup({
    id: new FormControl('', { nonNullable: true }),
    title: new FormControl('', { nonNullable: true }),
    author: new FormControl('', { nonNullable: true }),
    publicationDate: new FormControl('', { nonNullable: true })
  });


  onSubmit() {
    if(this.bookForm.valid){
      const book: Book = {
        id: parseInt(this.bookForm.value.id!),
        title: this.bookForm.value.title!,
        author: this.bookForm.value.author!,
        publicationDate: new Date(this.bookForm.value.publicationDate!)
      };
      this.formSubmitted.emit(book);
      // console.log('emitted')
      this.bookForm.reset()
    }
    
  }
}

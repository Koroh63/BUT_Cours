import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-book-editor',
  standalone: true,
  imports: [],
  templateUrl: './book-editor.component.html',
  styleUrl: './book-editor.component.css'
})
export class BookEditorComponent {
  profileForm = new FormGroup({
    title: new FormControl(''),
    author: new FormControl(''),
    publicationDate: new FormControl('')
  });

}

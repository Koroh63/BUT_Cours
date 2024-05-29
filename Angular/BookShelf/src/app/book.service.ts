import { Injectable } from '@angular/core';
import { Book } from './book/book';
import { BOOK } from './book/book.mock';
import { HttpClient, HttpHandler } from '@angular/common/http';
import { catchError, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  books : Book[] = BOOK;
  constructor(private http: HttpClient) {}

  getBooks() : Book[]{

    // let list: Book[] = BOOK;
    // let json : String = this.http.get'https://664ba07f35bbda10987d9f99.mockapi.io/api/books')    
    // list.concat(json)


    return BOOK;

    
  }

  addBooks(book:Book): boolean{
    try{
      this.books.push(book);
    }catch{
      return false
    }
    return true
  } 

  getBookById(id : number) : Book{

    let book : Book = {id:0,title:'default',publicationDate:new Date('1970-01-01'),author:''};
    this.books.forEach((bookItem) => {
      if(book.id==id){
        book = bookItem;
    }else{}
    });
    return book;
  
  }

}

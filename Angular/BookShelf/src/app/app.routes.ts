import { Routes, provideRouter, withComponentInputBinding } from '@angular/router';
import { BookComponent } from './book/book.component';
import { BookFormComponent } from './book-form/book-form.component';
import { HomeComponent } from './home/home.component';
import { ApplicationConfig } from '@angular/core';
import { BookDetailComponent } from './book-detail/book-detail.component';

export const routes: Routes = [
    { path: 'Home', component: HomeComponent},
    { path: 'Book', component: BookComponent},
    { path: 'Form', component: BookFormComponent},
    { path: 'Book/:id', component : BookDetailComponent},
    { path: '**', component: HomeComponent}
];

export const appConfig: ApplicationConfig = {
    providers: [provideRouter(routes,withComponentInputBinding())]
}

# DRF Library API

## Get a List of all Books

### request:

type: 'GET'

url: books/

### response:

```json
[
  {
    "url": "http://127.0.0.1:8000/books/1/",
    "title": "Test!",
    "author": "Test",
    "publication_date": "1111-01-01",
    "genre": "Test",
    "featured": true,
    "user": "admin"
  },
  {
    "url": "http://127.0.0.1:8000/books/2/",
    "title": "Another one!!",
    "author": "Another one",
    "publication_date": "1111-11-11",
    "genre": "Test",
    "featured": false,
    "user": "admin"
  },
  {
    "url": "http://127.0.0.1:8000/books/4/",
    "title": "Test",
    "author": "Test",
    "publication_date": "1111-01-01",
    "genre": "Test",
    "featured": true,
    "user": "testuser"
  },
  {
    "url": "http://127.0.0.1:8000/books/5/",
    "title": "Chicken",
    "author": "Wings",
    "publication_date": "1111-01-01",
    "genre": "Chicken",
    "featured": true,
    "user": "testuser"
  },
  {
    "url": "http://127.0.0.1:8000/books/6/",
    "title": "Another book",
    "author": "Another Book",
    "publication_date": "1111-11-11",
    "genre": "Not a valid string.",
    "featured": false,
    "user": "testuser"
  },
  {
    "url": "http://127.0.0.1:8000/books/8/",
    "title": "Demo",
    "author": "Demo",
    "publication_date": "1111-11-11",
    "genre": "Demo",
    "featured": false,
    "user": "admin"
  }
]
```

## Get a List of all Featured Books

### request:

type: 'GET'

url: featured/

### response:

```json
[
  {
    "url": "http://127.0.0.1:8000/books/1/",
    "title": "Test!",
    "author": "Test",
    "publication_date": "1111-01-01",
    "genre": "Test",
    "featured": true,
    "user": "admin"
  },
  {
    "url": "http://127.0.0.1:8000/books/4/",
    "title": "Test",
    "author": "Test",
    "publication_date": "1111-01-01",
    "genre": "Test",
    "featured": true,
    "user": "testuser"
  },
  {
    "url": "http://127.0.0.1:8000/books/5/",
    "title": "Chicken",
    "author": "Wings",
    "publication_date": "1111-01-01",
    "genre": "Chicken",
    "featured": true,
    "user": "testuser"
  }
]
```

## Create a new book

### request:

type: 'POST'

Requires Basic authentication.

title, author, publication date, genre, and user are required fields.

```json
{
  "url": "http://127.0.0.1:8000/books/3/",
  "title": "Demo",
  "author": "Demo",
  "publication_date": "1111-11-11",
  "genre": "Demo",
  "user": "admin"
}
```

### response:

```json
{
  "url": "http://127.0.0.1:8000/books/8/",
  "title": "Demo",
  "author": "Demo",
  "publication_date": "1111-11-11",
  "genre": "chicken wings",
  "featured": false,
  "user": "admin"
}
```

## Retrieve Details about a Book

### request:

type: 'GET'

url: books/{bookpk}

### response

```json
{
  "url": "http://127.0.0.1:8000/books/3/",
  "title": "Demo",
  "author": "Demo",
  "publication_date": "1111-11-11",
  "genre": "demo",
  "user": "admin"
}
```

## Search for a Book by Title or Author

### request:

type: 'GET'

url: books/?search={title or author}

### response:

```json
{
  "url": "http://127.0.0.1:8000/books/3/",
  "title": "The Anatomy of Melancholy",
  "author": "Robert Burton",
  "publication_date": "1111-11-11",
  "genre": "chicken wings",
  "featured": false,
  "user": "admin"
}
```

## List of all Books Current User is Tracking

type: 'GET'

Requires Basic authentication.

url: book_trackers/

### response:

```json
[
  {
    "url": "http://127.0.0.1:8000/book_trackers/12/",
    "status": "Want to Read",
    "book": "Chicken",
    "user": "admin"
  },
  {
    "url": "http://127.0.0.1:8000/book_trackers/13/",
    "status": "Want to Read",
    "book": "Not a valid string.",
    "user": "admin"
  }
]
```

## Track a Book and Add a Status

### request:

type: 'POST'

Requires Basic authentication.

url: /book_trackers

Status Options: 'Want To Read', 'Reading', 'Reading/Done'

url, status, book, and user are required fields.

```json
{
  "url": "http://127.0.0.1:8000/book_trackers/",
  "status": "Reading",
  "book": "Chicken",
  "user": "admin"
}
```

### response:

```json
{
  "url": "http://127.0.0.1:8000/book_trackers/17/",
  "status": "Reading",
  "book": "Chicken",
  "user": "admin"
}
```

## Change a Book Tracker's Status

### request:

type: 'PUT'

Requires Basic authentication.

url: book_trackers/{trackerpk}

Status Options: 'Want To Read', 'Reading', 'Reading/Done'

url, status, book, and user are required fields.

```json
{
  "url": "http://127.0.0.1:8000/book_trackers/12/",
  "status": "Reading",
  "book": "Chicken",
  "user": "admin"
}
```

### response:

```json
{
  "url": "http://127.0.0.1:8000/book_trackers/17/",
  "status": "Reading",
  "book": "Chicken",
  "user": "admin"
}
```

## View all Books by status

### request:

type: 'GET'

Requires Basic authentication.

Status Options: 'Want To Read', 'Reading', 'Reading/Done'

url: book_trackers/{Status}

```json
[
  {
    "url": "http://127.0.0.1:8000/book_trackers/17/",
    "status": "Reading",
    "book": "Demo",
    "user": "admin"
  }
]
```

## Retrieve All Private Book Notes

### request:

type: 'GET'

Requires Basic authentication.

url: notes/

```json
    "url": "http://127.0.0.1:8000/notes/6/",
    "book": "The Anatomy of Melancholy",
    "user": "admin",
    "created_date": "2022-04-03T03:18:17.313164Z",
    "text": "This is Melancholy's note",
    "public": false,
    "page_number": null
```

## Retrieve All Public Book Notes

### request:

type: 'GET'

Requires Basic authentication.

url: public-notes/

```json
[
  {
    "url": "http://127.0.0.1:8000/notes/3/",
    "book": "The Anatomy of Melancholy",
    "user": "testuser",
    "created_date": "2022-04-02T15:25:39.717457Z",
    "text": "Editing my notes",
    "public": true,
    "page_number": null
  },
  {
    "url": "http://127.0.0.1:8000/notes/5/",
    "book": "Test!",
    "user": "testuser",
    "created_date": "2022-04-02T15:41:30.353145Z",
    "text": "Reverse Order",
    "public": true,
    "page_number": null
  }
]
```

## Create a Note for a Book

### request:

type: 'POST'

Requires Basic authentication.

url: notes/

book, user, and text are required fields.

```json
{
  "book": "Chicken",
  "user": "admin",
  "text": "A Test",
  "public": false,
  "page_number": "30"
}
```

### response:

```json
{
  "url": "http://127.0.0.1:8000/notes/7/",
  "book": "Chicken",
  "user": "admin",
  "created_date": "2022-04-03T03:22:53.792382Z",
  "text": "A Test",
  "public": false,
  "page_number": 30
}
```

## Edit a Note

### request:

type: 'PUT'

Requires Basic authentication.

url: notes/{notepk}

book, user, and text are required fields.

```json
{
  "book": "Chicken",
  "user": "admin",
  "text": "A Test of an edit!",
  "public": false,
  "page_number": "30"
}
```

### response:

```json
{
  "url": "http://127.0.0.1:8000/notes/7/",
  "book": "Chicken",
  "user": "admin",
  "created_date": "2022-04-03T03:22:53.792382Z",
  "text": "A Test of an edit!",
  "public": false,
  "page_number": 30
}
```

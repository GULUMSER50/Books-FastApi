from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'Title': 'Title One', 'Author': 'Author One', 'Category': 'Science'},
    {'Title': 'Title Two', 'Author': 'Author Two', 'Category': 'Science'},
    {'Title': 'Title Three', 'Author': 'Author Three', 'Category': 'History'},
    {'Title': 'Title Four', 'Author': 'Author Four', 'Category': 'Math'},
    {'Title': 'Title Five', 'Author': 'Author Five', 'Category': 'Math'},
    {'Title': 'Title Six', 'Author': 'Author Two', 'Category': 'Math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/mybook")
async def read_all_books():
    return {'book_title': 'My Favourite Book!'}


# dynamic param
@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('Title').casefold() == book_title.casefold():
            return book


# query param --> ?
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('Category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('Author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('Author').casefold() == book_author.casefold() and \
                book.get('Category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('Title').casefold() == updated_book.get('Title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('Title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('Author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return




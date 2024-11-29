
from Batch03.Module03.save_all_book import save_all_books
def update_book(books,isbn):
    new_books_list=[]
    for book in books:
        if book['isbn']==isbn:
            title = input("Enter Book Title")
            author = input("Enter Author Name")
            year = int(input("Enter Publishing Year Number"))
            price = int(input("Enter Book Price"))
            quntaty = int(input("Enter Quantity Number"))
            updated_book = {
                "title": title,
                "author": author,
                "isbn": isbn,
                "year": year,
                "price": price,
                "quntaty": quntaty
            }
            new_books_list.append(updated_book)
        else:
            new_books_list.append(book)
    save_all_books(new_books_list)
    return new_books_list
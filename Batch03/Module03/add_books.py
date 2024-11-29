from Batch03.Module03.save_all_book import save_all_books


def add_books(all_books):
    title=input("Enter Book Title")
    author=input("Enter Author Name")
    isbn=input("Enter ISBN Number")
    year=int(input("Enter Publishing Year Number"))
    price=int(input("Enter Book Price"))
    quntaty=int(input("Enter Quantity Number"))

    book={
        "title":title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quntaty": quntaty
    }
    all_books.append(book)
    save_all_books(all_books)
    print("Books Added Successfully")
    return all_books
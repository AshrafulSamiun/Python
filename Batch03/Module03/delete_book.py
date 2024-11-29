from Batch03.Module03.save_all_book import save_all_books

def delete_book(all_books,isbn_num):
    filterbooklist=[book for book in all_books if book['isbn']!=isbn_num]
    save_all_books(filterbooklist)
    return filterbooklist

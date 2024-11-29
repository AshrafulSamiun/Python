import view_all_books
import add_books
import update_book
import delete_book

all_books=[]
while True:
    print("Welcom to library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Delete Book")
    menu=input("Select Any Number: ")

    if menu=="0":
        print("Thanks for library Management System")
        break
    elif menu=="1":
        all_books=add_books.add_books(all_books)
        print("Books Added Successfully ")
    elif menu=="2":
        view_all_books.view_all_books(all_books)
        print("Books displayed Successfully")
    elif menu=="3":
        isbn = input("Enter ISBN Number")
        all_books=update_book.update_book(all_books,isbn)
        print("Books Updated Successfully ")
    elif menu=="4":
        isbn = input("Enter ISBN Number")
        all_books=delete_book.delete_book(all_books,isbn)
        print("Books Deleted Successfully")
    else:
        print("Chose a Valid Number ")
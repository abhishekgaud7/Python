# write a program to build a libraary management system using for loop.
# user inputs book names to add to the library until they decide to stop.
# After adding books, display the list of all books in the library.


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'Book "{book_name}" added to the library.')

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(f'- {book}')
# Example usage
library = Library() 
library.add_book("To Kill a Mockingbird")
library.add_book("1984")
library.add_book("The Great Gatsby")
library.display_books()

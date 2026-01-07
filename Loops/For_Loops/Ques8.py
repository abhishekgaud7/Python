# write a program to build a libraary management system using for loop.
# user inputs book names to add to the library until they decide to stop.
# After adding books, display the list of all books in the library.
library = []
while True:
    book_name = input("Enter the name of the book to add to the library (or type 'stop' to finish): ")
    if book_name.lower() == 'stop':
        break
    library.append(book_name)
print("\nBooks in the library:")
for book in library:
    print("- " + book)

# add more features like removing a book, searching for a book, and displaying the total number of books in the library.
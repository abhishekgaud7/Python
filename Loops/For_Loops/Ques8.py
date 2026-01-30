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
# Removing a book
remove_book = input("\nEnter the name of the book to remove from the library (or type 'skip' to skip): ")

if remove_book.lower() != 'skip':
    if remove_book in library:
        library.remove(remove_book)
        print(f"'{remove_book}' has been removed from the library.")
    else:
        print(f"'{remove_book}' not found in the library.")
# Searching for a book
search_book = input("\nEnter the name of the book to search in the library: ")
if search_book in library:
    print(f"'{search_book}' is available in the library.")
else:
    print(f"'{search_book}' is not available in the library.")
# Displaying the total number of books
print(f"\nTotal number of books in the library: {len(library)}")


if remove_book.lower() != 'skip':
    if remove_book in library:
        library.remove(remove_book)
        print(f"'{remove_book}' has been removed from the library.")
    else:
        print(f"'{remove_book}' not found in the library.")
# Searching for a book
search_book = input("\nEnter the name of the book to search in the library: ")
if search_book in library:
    print(f"'{search_book}' is available in the library.")
else:
    print(f"'{search_book}' is not available in the library.")
# Displaying the total number of books
print(f"\nTotal number of books in the library: {len(library)}")
    

# Displaying the final list of books
print("\nFinal list of books in the library:")
for book in library:
    print("- " + book)
    
from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available      (COMPLETED)
# Output should include book ID, title, and author

def available():
    #for the for loop, I asked on AI to understand how to print the dictionary.
    for book in library_books:
        print(f'ID: {book['id']}')
        print(f'Title: {book['title']}')
        print(f'Author: {book['author']}')
        print('') #to separate the books.
available()

    



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre                  (COMPLETED)
# Search should be case-insensitive
# Return a list of matching books

def search_list():
    search = input("What would you like to search for? enter a genre or author: ").title()
    for book in library_books:
        #in the if condition I checked is in the book for loop, I understood why we need to for loop in this by looking it up.
        if book['author'].title() == search or book['title'].title() == search:
            print(f"Here are some results that we found matching your input: \n Author: {book['author']} and Title: {book['title'] }")
    if book['author'].title() != search or book['title'].title() != search:
        print("This title or author is not in our library.")
search_list()
        



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
for book in library_books:
    id_search = input("Please enter the book ID: ")
    if id_search == book['id']:
        print(book['id'])
    if id_search != book['id']:
        print("Not a valid ID.")
    
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass

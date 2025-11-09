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
                break
    else:
        print("This title or author is not in our library.")  
    print(" ")   

        



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID                    (COMPLETED)
# If the book is available:   
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


#researched time-delta and date.time for this part. i called these functions globally so i can access them in overdue books
today = datetime.today()
twoWeeks = timedelta(weeks=2)
return_time = (today+twoWeeks)

def id_checkout():
    user = input("Enter Book Id to CHECKOUT: ").upper()
    for book in library_books:
        if user == book['id']:
            print("Processing...")
            if book['available'] == False:
                print("The book is Not Available")
            if book['available'] == True:
                print("The book is Available.")
                
                print(f'Please return this book before {return_time}')
                book['available'] = False
                break
    if user != book['id']:
        print("Invalid Book ID.")
    return twoWeeks, today, return_time      
    print(" ")


    #(notes to self: )
        #code that checks in the book if book that the user chose is available, if so return true, if not return false
        #book id belongs to that book, then it has to check the book, and then check the availability of that book

                                 # THIS IS FOR THE OVERDUE FUNCTION LEVEL 4
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def overdue_books():
    borrowed = return_time - today
    if borrowed > twoWeeks:
        print("This book is OVERDUE. Please contact the librarian to pay the fee at (123-456-LIBRARY)")
    else:
        print("Book returned ON TIME.")
    print(" ")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID                  (COMPLETED)
# Set its availability to True and clear the due_date

#The return function is similar to the checkout function

def return_books():
    return_input = input("Enter Book Id to Return: ").upper()
    for book in library_books:
        if return_input == book['id']:
            print("Processing...")
            overdue_books()
            if book['available'] == True:
                print("The book is already Available. You CANNOT turn in this book.")
                break
            if book['available'] == False:
                print("You have successfully turned in the book.")
                book['available'] = True
                break
    if return_input != book['id']:
        print("Invalid Book ID.")
    print(" ")


    
    
    


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.


# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:                                                (COMPLETED)
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

while True:
    print("What option would you like: \n * 1.) Book Title, Author, and Id \n * 2.) Search for Title or Author \n * 3.) Checkout Books \n * 4.) Return Books \n * 5.)Exit")
    option = input("Enter option from 1-5: ")
    if option == '1':
        available()
        True
    if option == '2':
        search_list()
        True
    if option == '3':
        id_checkout() 
        True
    if option == '4':
        return_books()
        True
    if option == '5':
        False
        break
        
        
    




if __name__ == "__main__":
    # You can use this space to test your functions
        pass

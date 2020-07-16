import datetime
import time
def getTime():
    return datetime.datetime.now()

class Library:
    def __init__(self,list,name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self,):
        print(f"We have following books in our {self.name} library as of now : \n")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.bookList:
            print("No such book found!!!")
        else:
            print(f"Checking if {book} is lent by anyone...")
            time.sleep(2)
            if book not in self.lendDict.keys():
                print(f"\nNo... {book} hasn't been lent by anyone yet.")
                self.lendDict.update({book:user})
                with open("database.txt", "a") as op:
                    op.write(str([str(getTime())])+" : "+book+" by "+self.lendDict[book]+"(LENT)\n")
                print("\nYou can take the book.\nLender-Book database has been updated successfully.")
            else:
                print(f"\nSorry...Book is already lent by {self.lendDict[book]}")

    def addBook(self,book):
        print(f"Adding {book} in the library... ")
        time.sleep(2)
        self.bookList.append(book)
        print(f"{book} has been added successfully in the library.")
        with open("database.txt", "a") as op:
                op.write(str([str(getTime())])+" : "+book+"(ADDED)\n")

    def returnBook(self,book):
        try:
            if book not in self.bookList:
                print("No such book in the library...")
            else:
                print(f"Returning {book}....")
                time.sleep(2)
                self.lendDict.pop(book)
                with open("database.txt", "a") as op:
                    op.write(str([str(getTime())])+" : "+book+"(RETURNED)\n")
                print(f"{book} returned successfully...")
        except KeyError:
            print("Book not lent by anyone yet!!")


if __name__ == "__main__":
    dev = Library(['C','C++','Data Structures and Algorithms','Java','Python','Database Management System'],"DEVIL")

    while(True):
        print(f"Welcome to {dev.name} Library.\n")
        print("1. Display all books")
        print("2. Lend a book")
        print("3. Return a book")
        print("4. Add a book")
        user_choice = input("\nEnter your choice to continue : ")
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid choice.")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice==1:
            dev.displayBooks()

        elif user_choice==2:
            user = input("Enter your name : ")
            book = input("Enter name of the book you want to lend : ")
            dev.lendBook(user,book)

        elif user_choice==3:
            book = input("Enter name of the book you want to return : ")
            dev.returnBook(book)

        elif user_choice==4:
            book = input("Enter name of the book you want to add : ")
            dev.addBook(book)

        else:
            print("Invalid Choice!!!")

        print("\nPress c to Continue and q to Quit : ")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input("")
            if user_choice2=="c":
                continue
            elif user_choice2=="q":
                exit()

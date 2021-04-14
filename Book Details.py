import sqlite3
BookStore = sqlite3.connect('BookStore.db')
cursbs = BookStore.cursor()

def tablecreation():
    
    cursbs.execute('''CREATE TABLE Books (Title Text(30) PRIMARY KEY,
    Author Text(20),
    Price Float);''')
    print("Table Created Successfully!")

def tableinsertion():
    
    title = input("Enter the title of Book\n")
    author = input("Enter author's name\n")
    price = float(input("Enter the price of book\n"))

    try:
        cursbs.execute("INSERT INTO Books (Title,Author,Price) VALUES(?,?,?)",
           (title,author,price))
        BookStore.commit()
        print("One record added successfully")
        
        
    except:
        print("Error in operation")
        BookStore.rollback()
        

b = input("Press 1 if you want to create a table\nPress 2 if you want to add book details\n")

if b == '1':
    try:
        tablecreation()
        d = input("Do you want to add Books to the table?\n")
        while d == 'yes':
            tableinsertion()
            d = input("Do you want to add Books to the table?\n")
        else:
            print("Thank You!")
            exit

    except:
        print("Table is already created!")
        d = input("Do you want to add Books to the table?\n")
        while d == 'yes':
            tableinsertion()
            d = input("Do you want to add Books to the table?\n")
        else:
            print("Thank You!")
            exit
elif b == '2':
    tableinsertion()
    a = input("Do you want to add more books? Enter yes or no\n")
    while a == 'yes':
        tableinsertion()
        a = input("Do you want to add more books? Enter yes or no\n")
    else:
        print("Done")
        exit

BookStore.close()


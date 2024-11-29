# CONNECTING
def connectSQL():
    import mysql.connector as sql

    myCon = sql.connect(
        host="localhost", user="root", password="root", database="library"
    )
    return myCon


# ADDING BOOK DETAILS


def add_book():
    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()
    # Creating Interface
    print("] ADDING BOOKS |\n")

    # Accepting Information
    book_id = int(input("] Book ID : "))
    title = input("] Book Title : ")
    author = input("] Name Of Author : ")
    isbn = input("] International Standard Book Number [ISBN] : ")
    publisher = input("] Name Of Publisher : ")
    year = input("] Year Of Publish : ")
    genre = input("] Genre (if any) : ")
    quantity = int(input("] Quantity : "))
    borrowed_count = int(input("] No. Of Times Borrowed : "))
    status = input("] Status [ available | checked out | reserved | lost ] : ")

    query = "INSERT INTO book VALUES({},'{}','{}',{},'{}',{},'{}',{},{},'{}')".format(
        book_id,
        title,
        author,
        isbn,
        publisher,
        year,
        genre,
        quantity,
        borrowed_count,
        status,
    )

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("New Book Added To Database Successfully!")
    except:
        print("An Error Occured!")
    finally:
        myCon.close()


# SEARCHING BOOK DETAILS
def search_book():
    myCon = connectSQL()
    myCur = myCon.cursor()
    print("SEARCHING DETAILS |\n")
    bookID = int(input("Book ID : "))
    query="SELECT * FROM book WHERE book_id = {}".format(bookID)
    myCur.execute(query)
    columns = myCur.fetchall()
# UPDATING BOOK DETAILS


def update_book():
    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    myCur.execute("describe book")
    sqlData = myCur.fetchall()
    details = {}
    for i in range(1, len(sqlData)):
        details[i] = sqlData[i][0]

    # Creating Interface
    print("UPDATING DETAILS |\n")
    bookID = int(input("\tEnter Book ID : "))
    print("\tDetails Available")
    for i in range(1, len(details) + 1):
        print("\t", i, " - ", details[i])
    ans = int(input("\tEnter Selection Number : "))
    inputDetail = details[ans]
    print()

    query = "SELECT {} FROM book WHERE book_id = {}".format(inputDetail, bookID)
    myCur.execute(query)
    oldDetail = myCur.fetchall()[0][0]
    print("Old {}".format(inputDetail), " = ", oldDetail)
    newDetail = input("\n\tEnter New {} : ".format(inputDetail))
    query = "UPDATE book SET {} = '{}' WHERE book_id = {}".format(
        inputDetail, newDetail, bookID
    )

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("Successfully Submitted!")
    except:
        print("An Error Occured!")
    finally:
        myCon.close()

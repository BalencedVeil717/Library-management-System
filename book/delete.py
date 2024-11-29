# DELETING BOOK RECORDS
def delete_book():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Creating Interface
    print("DELETING BOOK RECORD |\n")
    bookID = int(input("\tEnter Book ID: "))

    # Formulating Query
    query = "DELETE FROM books WHERE book_id = {}".format(bookID)

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("Delete Book Record Successfully!")
    except:
        print("Error Occurred!")
    finally:
        myCon.close()

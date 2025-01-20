# ADDING BOOK DETAILS


def add_book():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Creating Interface
    print("] ADDING BOOKS |\n")

    # Accepting Information
    book_id = int(input("] Book ID: "))
    title = input("] Book Title: ")
    author = input("] Name Of Author: ")
    isbn = input("] International Standard Book Number [ISBN]: ")
    publisher = input("] Name Of Publisher: ")
    year = input("] Year Of Publish: ")
    genre = input("] Genre (if any): ")
    quantity = int(input("] Quantity: "))
    borrowed_count = int(input("] No. Of Times Borrowed: "))
    status = input("] Status [ available | checked out | reserved | lost ]: ")

    # Formulating Query
    query = "INSERT INTO books VALUES({}, '{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}')".format(
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
        print("Book Added Successfully!")
    except Exception as e:
        print("An Error Occurred!: {}".format(e))
    finally:
        myCon.close()

def total_books():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL Query to count total books
    query = "SELECT COUNT(*) FROM books"

    # Execute the query
    myCur.execute(query)
    result = myCur.fetchone()

    # Closing the connection
    myCon.close()

    return result[0]


def most_borrowed_book():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to show the most borrowed book
    query = "SELECT max(quantity) FROM books"

    # Execute the query
    myCur.execute(query)
    max_count = myCur.fetchone()[0]

    # SQL query to get the name of book
    query2 = "SELECT title FROM books WHERE quantity = {}".format(max_count)

    # Execute the query
    myCur.execute(query2)
    result = myCur.fetchone()

    # Closing the connection
    myCon.close()

    return result[0]


def available_books():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to show the most borrowed book
    query = "SELECT title FROM books WHERE status = 'available'"

    # Execute the query
    myCur.execute(query)
    books = myCur.fetchall()

    # Extract book names
    result = []
    for name in books:
        result.append(name[0])

    # Closing the connection
    myCon.close()

    return result

def loaned_books():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to show the most borrowed book
    query = "SELECT title FROM books WHERE status = 'checked out'"

    # Execute the query
    myCur.execute(query)
    books = myCur.fetchall()

    # Extract book names
    result = []
    for name in books:
        result.append(name[0])

    # Closing the connection
    myCon.close()

    return result



def reserved_books():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to show the most borrowed book
    query = "SELECT title FROM books WHERE status = 'reserved'"

    # Execute the query
    myCur.execute(query)
    books = myCur.fetchall()

    # Extract book names
    result = []
    for name in books:
        result.append(name[0])

    # Closing the connection
    myCon.close()

    return result

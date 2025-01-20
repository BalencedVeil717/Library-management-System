def total_loans():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL Query to count total books
    query = "SELECT COUNT(*) FROM loans"

    # Execute the query
    myCur.execute(query)
    result = myCur.fetchone()

    # Closing the cursor and connection
    myCur.close()
    myCon.close()

    return result[0]


def most_loaned_book():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to show the most borrowed book
    query = "SELECT book_id, COUNT(member_id) as loan_count FROM loans GROUP BY book_id ORDER BY loan_count DESC"

    # Execute the query
    myCur.execute(query)
    max_loaned_id = myCur.fetchone()[0]

    # Fetch all remaining rows to ensure no unread results
    myCur.fetchall()

    # SQL query to get the name of book
    query2 = "SELECT title FROM books WHERE book_id = {}".format(max_loaned_id)

    # Execute the query
    myCur.execute(query2)
    result = myCur.fetchone()

    # Closing the connection
    myCon.close()

    return result[0]


def current_loans():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to show the most borrowed book
    query = "SELECT book_id, member_id FROM loans WHERE status = 'loaned'"

    # Execute the query
    myCur.execute(query)
    response = myCur.fetchall()

    loaned_books = {}
    for book_id, member_id in response:
        book_query = "SELECT title FROM books WHERE book_id = {}".format(book_id)
        myCur.execute(book_query)
        book_name = myCur.fetchone()[0]

        member_query = (
            "SELECT first_name, last_name FROM members WHERE member_id = {}".format(
                member_id
            )
        )
        myCur.execute(member_query)
        member = myCur.fetchone()
        member_name = member[0] + " " + member[1]

        if book_name not in loaned_books:
            loaned_books[book_name] = member_name

    # Closing the connection
    myCon.close()

    return loaned_books




def overdue_loans():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to show the most borrowed book
    query = "SELECT book_id, member_id FROM loans WHERE status = 'overdue'"

    # Execute the query
    myCur.execute(query)
    response = myCur.fetchall()

    loaned_books = {}
    for book_id, member_id in response:
        book_query = "SELECT title FROM books WHERE book_id = {}".format(book_id)
        myCur.execute(book_query)
        book_name = myCur.fetchone()[0]

        member_query = (
            "SELECT first_name, last_name FROM members WHERE member_id = {}".format(
                member_id
            )
        )
        myCur.execute(member_query)
        member = myCur.fetchone()
        member_name = member[0] + " " + member[1]

        if book_name not in loaned_books:
            loaned_books[book_name] = member_name

    # Closing the connection
    myCon.close()

    return loaned_books



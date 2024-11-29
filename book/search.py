# SEARCHING BOOK DETAILS
def search_book():
    from config import connectSQL
    from tabulate import tabulate

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Getting Headers
    myCur.execute("DESCRIBE book")
    columns = myCur.fetchall()
    headers = [column[0] for column in columns]

    # Creating Interface
    print("SEARCHING DETAILS |\n")
    bookID = int(input("\tEnter Book ID: "))

    # Executing Query
    query = "SELECT * FROM books WHERE book_id = {}".format(bookID)
    myCur.execute(query)
    details = list(myCur.fetchone())

    # Preparing Data for Display
    data = list(zip(headers, details))

    # Printing Book Details
    print("\n\tBook Details |")
    table = tabulate(data, tablefmt="fancy_grid")
    for line in table.split("\n"):
        print("\t", line)

    # Closing Connection
    myCon.close()

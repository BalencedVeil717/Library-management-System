# SEARCHING LOAN DETAILS
def search():
    from config import connectSQL
    from tabulate import tabulate

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Getting Headers
    myCur.execute("DESCRIBE loans")
    columns = myCur.fetchall()
    headers = [column[0] for column in columns]

    # Creating Interface
    print("] SEARCHING LOAN DETAILS |\n")
    loanID = int(input("\tEnter Loan ID: "))

    # Executing Query
    query = "SELECT * FROM loans WHERE loan_id = {}".format(loanID)
    myCur.execute(query)
    details = list(myCur.fetchone())

    # Preparing Data for Display
    data = list(zip(headers, details))

    # Printing Book Details
    print("\n\tLoan Details |")
    table = tabulate(data, tablefmt="fancy_grid")
    for line in table.split("\n"):
        print("\t", line)

    # Closing Connection
    myCon.close()

# SEARCHING MEMBER DETAILS
def search_member():
    from config import connectSQL
    from tabulate import tabulate

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Getting Headers
    myCur.execute("DESCRIBE members")
    columns = myCur.fetchall()
    headers = [column[0] for column in columns]

    # Creating Interface
    print("] SEARCHING DETAILS |\n")
    memberID = int(input("\tEnter Member ID: "))

    # Executing Query
    query = "SELECT * FROM members WHERE member_id = {}".format(memberID)
    myCur.execute(query)
    details = list(myCur.fetchone())

    # Preparing Data for Display
    data = list(zip(headers, details))

    # Printing Book Details
    print("\n\tMember Details |")
    table = tabulate(data, tablefmt="fancy_grid")
    for line in table.split("\n"):
        print("\t", line)

    # Closing Connection
    myCon.close()

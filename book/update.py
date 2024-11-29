# UPDATING BOOK DETAILS


def update():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Fetching Table Headers
    myCur.execute("DESCRIBE books")
    sqlData = myCur.fetchall()
    details = {i: sqlData[i][0] for i in range(1, len(sqlData))}

    # Creating Interface
    print("] UPDATING BOOK DETAILS |\n")
    bookID = int(input("\tEnter Book ID: "))
    print("\tDetails Available :")
    for i in range(1, len(details) + 1):
        print("\t", i, "-", details[i])

    ans = int(input("\tEnter Selection Number : "))
    inputDetail = details[ans]
    print()

    # Fetching Current Detail
    query = "SELECT {} FROM books WHERE book_id = {}".format(inputDetail, bookID)
    myCur.execute(query)
    oldDetail = myCur.fetchone()[0]
    print("\tOld {} = {}".format(inputDetail, oldDetail))

    # Updating Detail
    newDetail = input("\n\tEnter New {}: ".format(inputDetail))
    query = "UPDATE books SET {} = '{}' WHERE book_id = {}".format(
        inputDetail, newDetail, bookID
    )

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("Details Updated Successfully!")
    except:
        print("An Error Occurred!")
    finally:
        myCon.close()

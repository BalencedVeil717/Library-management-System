# UPDATING MEMBER DETAILS


def update():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Fetching Table Headers
    myCur.execute("DESCRIBE members")
    sqlData = myCur.fetchall()
    details = {i: sqlData[i][0] for i in range(1, len(sqlData))}

    # Creating Interface
    print("] UPDATING MEMBER DETAILS |\n")
    memberID = int(input(("\tEnter Member ID : ")))
    print("\tDetails Available :")
    for i in range(1, len(details) + 1):
        print("\t", i, "-", details[i])

    ans = int(input("\tEnter Selection Number : "))
    inputDetail = details[ans]
    print()

    # Fetching Current Detail
    query = "SELECT {} FROM members WHERE member_id = {}".format(inputDetail, memberID)
    myCur.execute(query)
    oldDetail = myCur.fetchone()[0]
    print("\tOld {} = {}".format(inputDetail, oldDetail))

    # Updating Detail
    newDetail = input("\n\tEnter New {}: ".format(inputDetail))
    query = "UPDATE members SET {} = '{}' WHERE member_id = {}".format(
        inputDetail, newDetail, memberID
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

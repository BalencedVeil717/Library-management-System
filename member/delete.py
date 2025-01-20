# DELETING MEMBER RECORDS
def delete_member():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Creating Interface
    print("] DELETING MEMBER RECORD |\n")
    memberID = int(input("\tEnter Member ID: "))

    # Formulating Query
    query = "DELETE FROM members WHERE member_id = {}".format(memberID)

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("Deleted Record Successfully!")
    except:
        print("An Error Occurred!")
    finally:
        myCon.close()


# REMOVING LOAN DETAILS
def delete_loan():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Creating Interface
    print("] RETURNING BOOKS |\n")
    loanID = int(input("\tEnter Loan ID : "))

    # Formulating Query
    query = "DELETE FROM loans WHERE loan_id = {}".format(loanID)

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("Loan Removed Successfully!")
    except:
        print("An Error Occurred!")
    finally:
        myCon.close()



# ADDING LOAN DETAILS
def add_loan():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Creating Interface
    print("] LOANING BOOKS |\n")

    # Accepting Information
    loan_id = int(input("] Loan ID: "))
    member_id = int(input("] Member ID: "))
    book_id = int(input("] Book ID: "))
    loan_date = input("] Loan Date [YYYY-MM-DD]: ")
    due_date = input("] Due Date [YYYY-MM-DD]: ")
    return_date = input("] Return Date [YYYY-MM-DD]: ")
    status = input("] Status [ loaned | returned | overdue ]: ")

    # Formulating Query
    query = "INSERT INTO loans (loan_id, member_id, book_id, loan_date, due_date, return_date, status) VALUES ({}, {}, {}, '{}', '{}', '{}', '{}')".format(
        loan_id, member_id, book_id, loan_date, due_date, return_date, status
    )

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("Loan Added Successfully!")
    except:
        print("An Error Occurred!")
    finally:
        myCon.close()

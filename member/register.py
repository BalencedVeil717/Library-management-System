# REGISTERING NEW MEMBER


def register():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # Creating Interface
    print("] REGISTERING MEMBERS |\n")

    # Accepting Information
    member_id = int(input("] Member ID : "))
    first_name = input("] First Name : ")
    last_name = input("] Last Name : ")
    date_of_birth = input("] Date Of Birth [YYYY-MM-DD] : ")
    address = input("] Address : ")
    phone_number = input("] Phone Number : ")
    email = input("] Email : ")
    join_date = input("] Join Date [YYYY-MM-DD] : ")
    membership_type = input("] Membership [ standard | premium | student ] : ")
    status = input("] Status [ active | inactive ] : ")

    # Formulating Query
    query = "INSERT INTO members VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        member_id,
        first_name,
        last_name,
        date_of_birth,
        address,
        phone_number,
        email,
        join_date,
        membership_type,
        status,
    )

    # Applying Changes
    try:
        myCur.execute(query)
        myCon.commit()
        print("Member Registered Successfully!")
    except:
        print("An Error Occured")
    finally:
        myCon.close()

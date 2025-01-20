def total_members():
    from config import connectSQL

    # Connection Establishment
    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL Query to count total books
    query = "SELECT COUNT(*) FROM members"

    # Execute the query
    myCur.execute(query)
    result = myCur.fetchone()

    # Closing the cursor and connection
    myCur.close()
    myCon.close()

    return result[0]


def active_member():
    from config import connectSQL

    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to find the most active member
    query = "SELECT member_id, COUNT(*) as loan_count FROM loans GROUP BY member_id ORDER BY loan_count DESC LIMIT 1"

    # Execute the query
    myCur.execute(query)
    active_member_id = myCur.fetchone()[0]

    # Fetch all remaining rows to ensure no unread results
    myCur.fetchall()

    # SQL query to get the name of the most active member
    query2 = "SELECT first_name, last_name FROM members WHERE member_id = {}".format(
        active_member_id
    )

    # Execute the query
    myCur.execute(query2)
    response = myCur.fetchone()

    f_name = response[0]

    l_name = response[1]

    name = f_name + " " + l_name

    # Closing the connection
    myCon.close()

    return name


def inactive_member():
    from config import connectSQL

    myCon = connectSQL()
    myCur = myCon.cursor()

    # SQL query to find the most active member
    query = "SELECT first_name, last_name FROM members WHERE member_id NOT IN (SELECT member_id FROM loans)"

    # Execute the query
    myCur.execute(query)
    response = myCur.fetchall()
    names = []
    for data in response:
        names.append(data[0] + " " + data[1])


    # Closing the connection
    myCon.close()

    return names

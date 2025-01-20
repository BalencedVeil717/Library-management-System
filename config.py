# CREATING CONNECTION
def connectSQL():
    import mysql.connector as sql

    myCon = sql.connect(
        host="localhost", user="root", password="root", database="library"
    )
    return myCon

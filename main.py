while True:
    print("Welcome")
    print("\n\n|-  ADVANCED LIBRARY MANAGEMENT SYSTEM\n\n")
    print("  |1 - Books Management")
    print("  |2 - Members Management")
    print("  |3 - Loans Management")
    print("  |4 - Exit")

    table_opt = input("  |Enter Choice: ")
    while table_opt not in ["1", "2", "3", "4"]:
        print("  | Incorrect option selected! Try Again.")
        table_opt = input("  | Enter Choice: ")

    if table_opt == "1":  # Books Management
        while True:
            print("\n\n  |-- BOOKS MANAGEMENT")
            print("    | 1 - Add Book")
            print("    | 2 - Delete Book")
            print("    | 3 - Search Book")
            print("    | 4 - Update Details")
            print("    | 5 - Back")

            books_opt = input("    | Enter Choice: ")
            while books_opt not in ["1", "2", "3", "4", "5"]:
                print("    | Incorrect option selected! Try Again.")
                books_opt = input("    | Enter Choice: ")

            if books_opt == "1":
                from book.add import add_book

                add_book()
            elif books_opt == "2":
                from book.delete import delete_book

                delete_book()
            elif books_opt == "3":
                from book.search import search_book

                search_book()
            elif books_opt == "4":
                from book.update import update_book

                update_book()
            elif books_opt == "5":
                break

    elif table_opt == "2":  # Members Management
        while True:
            print("\n\n  |-- MEMBERS MANAGEMENT")
            print("    | 1 - Register Member")
            print("    | 2 - Delete Member")
            print("    | 3 - Search Member")
            print("    | 4 - Update Details")
            print("    | 5 - Back")

            members_opt = input("    | Enter Choice: ")
            while members_opt not in ["1", "2", "3", "4", "5"]:
                print("    | Incorrect option selected! Try Again.")
                members_opt = input("    | Enter Choice: ")

            if members_opt == "1":
                from member.register import register_member

                register_member()
            elif members_opt == "2":
                from member.delete import delete_member

                delete_member()
            elif members_opt == "3":
                from member.search import search_member

                search_member()
            elif members_opt == "4":
                from member.update import update_member

                update_member()
            elif members_opt == "5":
                break

    elif table_opt == "3":  # Loans Management
        while True:
            print("\n\n  |-- LOANS MANAGEMENT")
            print("    | 1 - Add Loan")
            print("    | 2 - Delete Loan")
            print("    | 3 - Search Loan")
            print("    | 4 - Back")

            loans_opt = input("    | Enter Choice: ")
            while loans_opt not in ["1", "2", "3", "4"]:
                print("    | Incorrect option selected! Try Again.")
                loans_opt = input("    | Enter Choice: ")

            if loans_opt == "1":
                from loan.add import add_loan

                add_loan()
            elif loans_opt == "2":
                from loan.delete import delete_loan

                delete_loan()
            elif loans_opt == "3":
                from loan.search import search_loan

                search_loan()
            elif loans_opt == "4":
                break

    elif table_opt == "4":  # Exit
        print("\n\n  | Exiting the system...")
        break

import reports
import reports.books_data
import reports.loans_data
import reports.members_data


def display_library_report():
    total_books_count = reports.books_data.total_books()
    most_borrowed_book_title = reports.books_data.most_borrowed_book()
    available_books_list = reports.books_data.available_books()
    loaned_books_list = reports.books_data.loaned_books()
    reserved_books_list = reports.books_data.reserved_books()
    total_loans_count = reports.loans_data.total_loans()
    most_loaned_book_title = reports.loans_data.most_loaned_book()
    current_loans_list = reports.loans_data.current_loans()
    overdue_loans_list = reports.loans_data.overdue_loans()
    total_members_count = reports.members_data.total_members()
    most_active_member_name = reports.members_data.active_member()
    inactive_members_list = reports.members_data.inactive_member()

    # Generate the report
    report_lines = []
    report_lines.append("====================")
    report_lines.append("   Library Report   ")
    report_lines.append("====================\n")
    report_lines.append("\n|  BOOKS REPORT:")
    report_lines.append(f"\n📚 Total Books: {total_books_count}")
    report_lines.append(f"📘 Most Borrowed Book: {most_borrowed_book_title}\n")
    report_lines.append("📖 Available Books:")
    report_lines.extend(format_list(available_books_list))
    report_lines.append("\n📕 Loaned Books:")
    report_lines.extend(format_list(loaned_books_list))
    report_lines.append("\n📗 Reserved Books:")
    report_lines.extend(format_list(reserved_books_list))
    report_lines.append("\n|  LOANS REPORT:")
    report_lines.append(f"\n🔢 Total Loans: {total_loans_count}")
    report_lines.append(f"📚 Most Loaned Book: {most_loaned_book_title}\n")
    report_lines.append("📚 Current Loans:")
    report_lines.extend(format_current_loans(current_loans_list))
    report_lines.append("\n⏰ Overdue Loans:")
    report_lines.extend(format_overdue_loans(overdue_loans_list))
    report_lines.append("\n|  MEMBERS REPORT:")
    report_lines.append(f"\n👥 Total Members: {total_members_count}")
    report_lines.append(f"⭐ Most Active Member: {most_active_member_name}\n")
    report_lines.append("🛑 Inactive Members:")
    report_lines.extend(format_list(inactive_members_list))

    # Print the report
    print("\n".join(report_lines))


def format_list(items):
    return [f"  - {item}" for item in items]


def format_current_loans(current_loans_list):
    return [
        f"  - {book} borrowed by {member}"
        for book, member in current_loans_list.items()
    ]


def format_overdue_loans(overdue_loans_list):
    return [
        f"  - {book} overdue by {member}" for book, member in overdue_loans_list.items()
    ]

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
    QLabel,
)
from PySide6.QtGui import QAction
from books.add import AddBook


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 1000, 600)

        main_layout = QHBoxLayout()
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Sidebar
        self.sidebar = QVBoxLayout()
        self.sidebar.setSpacing(10)

        books_button = QPushButton("Books")
        loans_button = QPushButton("Loans")
        members_button = QPushButton("Members")

        books_button.clicked.connect(self.show_books)
        loans_button.clicked.connect(self.show_loans)
        members_button.clicked.connect(self.show_members)

        self.sidebar.addWidget(books_button)
        self.sidebar.addWidget(loans_button)
        self.sidebar.addWidget(members_button)

        # Main Content Area
        self.main_content = QStackedWidget()

        self.books_page = QWidget()
        self.loans_page = QWidget()
        self.members_page = QWidget()

        self.books_page.setLayout(self.create_books_layout())
        self.loans_page.setLayout(self.create_loans_layout())
        self.members_page.setLayout(self.create_members_layout())

        self.main_content.addWidget(self.books_page)
        self.main_content.addWidget(self.loans_page)
        self.main_content.addWidget(self.members_page)

        main_layout.addLayout(self.sidebar)
        main_layout.addWidget(self.main_content)

        self.show_books()

        # Apply stylesheet
        self.apply_stylesheet()

    def create_books_layout(self):
        layout = QVBoxLayout()
        add_book_button = QPushButton("Add Book")
        update_book_button = QPushButton("Update Book")
        search_book_button = QPushButton("Search Book")
        delete_book_button = QPushButton("Delete Book")

        add_book_button.clicked.connect(self.open_add_book)

        layout.addWidget(add_book_button)
        layout.addWidget(update_book_button)
        layout.addWidget(search_book_button)
        layout.addWidget(delete_book_button)
        return layout

    def create_loans_layout(self):
        layout = QVBoxLayout()
        add_loan_button = QPushButton("Add Loan")
        search_loan_button = QPushButton("Search Loan")
        delete_loan_button = QPushButton("Delete Loan")

        layout.addWidget(add_loan_button)
        layout.addWidget(search_loan_button)
        layout.addWidget(delete_loan_button)
        return layout

    def create_members_layout(self):
        layout = QVBoxLayout()
        register_member_button = QPushButton("Register Member")
        update_member_button = QPushButton("Update Member")
        search_member_button = QPushButton("Search Member")
        delete_member_button = QPushButton("Delete Member")

        layout.addWidget(register_member_button)
        layout.addWidget(update_member_button)
        layout.addWidget(search_member_button)
        layout.addWidget(delete_member_button)
        return layout

    def show_books(self):
        self.main_content.setCurrentWidget(self.books_page)

    def show_loans(self):
        self.main_content.setCurrentWidget(self.loans_page)

    def show_members(self):
        self.main_content.setCurrentWidget(self.members_page)

    def open_add_book(self):
        self.add_book_window = AddBook()
        self.add_book_window.show()

    def apply_stylesheet(self):
        stylesheet = """
        QMainWindow {
            background-color: #f0f0f0;
        }

        QVBoxLayout {
            margin: 10px;
        }

        QPushButton {
            background-color: #4CAF50;
            color: white;
            font-size: 14px;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            margin-bottom: 10px;
        }

        QPushButton:hover {
            background-color: #45a049;
        }

        QStackedWidget {
            background-color: #ffffff;
            border: 1px solid #d4d4d4;
            border-radius: 5px;
            margin-left: 20px;
            padding: 10px;
        }
        """
        self.setStyleSheet(stylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

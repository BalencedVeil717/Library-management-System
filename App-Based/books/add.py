from config import connectSQL
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QApplication,
)
import sys


class AddBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add Book")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.book_id_input = self.create_input_field("Book ID:")
        layout.addWidget(self.book_id_input[0])
        layout.addWidget(self.book_id_input[1])

        self.title_input = self.create_input_field("Book Title:")
        layout.addWidget(self.title_input[0])
        layout.addWidget(self.title_input[1])

        self.author_input = self.create_input_field("Name Of Author:")
        layout.addWidget(self.author_input[0])
        layout.addWidget(self.author_input[1])

        self.isbn_input = self.create_input_field(
            "International Standard Book Number [ISBN]:"
        )
        layout.addWidget(self.isbn_input[0])
        layout.addWidget(self.isbn_input[1])

        self.publisher_input = self.create_input_field("Name Of Publisher:")
        layout.addWidget(self.publisher_input[0])
        layout.addWidget(self.publisher_input[1])

        self.year_input = self.create_input_field("Year Of Publish:")
        layout.addWidget(self.year_input[0])
        layout.addWidget(self.year_input[1])

        self.genre_input = self.create_input_field("Genre (if any):")
        layout.addWidget(self.genre_input[0])
        layout.addWidget(self.genre_input[1])

        self.quantity_input = self.create_input_field("Quantity:")
        layout.addWidget(self.quantity_input[0])
        layout.addWidget(self.quantity_input[1])

        self.borrowed_count_input = self.create_input_field("No. Of Times Borrowed:")
        layout.addWidget(self.borrowed_count_input[0])
        layout.addWidget(self.borrowed_count_input[1])

        self.status_input = self.create_input_field(
            "Status [ available | checked out | reserved | lost ]:"
        )
        layout.addWidget(self.status_input[0])
        layout.addWidget(self.status_input[1])

        submit_button = QPushButton("Add Book")
        submit_button.clicked.connect(self.add_book)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def create_input_field(self, label_text):
        label = QLabel(label_text)
        input_field = QLineEdit()
        return label, input_field

    def add_book(self):
        try:
            myCon = connectSQL()
            myCur = myCon.cursor()

            book_id = int(self.book_id_input[1].text())
            title = self.title_input[1].text()
            author = self.author_input[1].text()
            isbn = self.isbn_input[1].text()
            publisher = self.publisher_input[1].text()
            year = self.year_input[1].text()
            genre = self.genre_input[1].text()
            quantity = int(self.quantity_input[1].text())
            borrowed_count = int(self.borrowed_count_input[1].text())
            status = self.status_input[1].text()

            query = (
                "INSERT INTO books (book_id, title, author, isbn, publisher, year, genre, quantity, borrowed_count, status) "
                "VALUES ({}, '{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}')".format(
                    book_id,
                    title,
                    author,
                    isbn,
                    publisher,
                    year,
                    genre,
                    quantity,
                    borrowed_count,
                    status,
                )
            )

            myCur.execute(query)
            myCon.commit()
            QMessageBox.information(self, "Success", "Book Added Successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Error", "An Error Occurred: {}".format(e))

        finally:
            myCon.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddBook()
    window.show()
    sys.exit(app.exec())

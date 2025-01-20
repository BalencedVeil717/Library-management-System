# Library Management System

Welcome to the Library Management System! This project is a practice exercise designed to help understand the basics of managing a library system using Python and MySQL. Please note that this project is intended for educational purposes and may not be fully optimized for production use.

## Features

- **Books Management**: Add, delete, search, and update book details.
- **Members Management**: Register, delete, search, and update member details.
- **Loans Management**: Add, delete, and search loan records.

## Requirements

- Python 3.7+
- MySQL Server
- MySQL Connector for Python

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/Library-management-System.git
    cd Library-management-System
    ```

2. **Install the required Python packages**:

    ```sh
    pip install mysql-connector-python
    ```

3. **Set up the MySQL database**:
    - Create a new database named library in MySQL.
    - Create tables books, loans, members with appropriate attributes in it.
    - Import the provided SQL script to set up the necessary tables.

4. **Configure the database connection**:
    - Update the database connection details in the configuration file (e.g., `config.py`).

## Usage

1. **Run the main script**:

    ```sh
    python main.py
    ```

2. **Follow the on-screen instructions** to navigate through the different management options.

## Project Structure

```sh
Library-management-System/
│
├── book/
│   ├── add.py
│   ├── delete.py
│   ├── search.py
│   └── update.py
│
├── member/
│   ├── register.py
│   ├── delete.py
│   ├── search.py
│   └── update.py
│
├── loan/
│   ├── add.py
│   ├── delete.py
│   └── search.py
│
├── main.py
├── config.py
└── README.md
```

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- This project was inspired by various online tutorials and resources.
- Special thanks to the open-source community for providing valuable tools and libraries.

## Disclaimer

This project is for educational purposes only. It uses MySQL as a local feature, so the project may not work if you download and run it without proper configuration.

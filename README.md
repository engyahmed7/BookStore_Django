# Bookstore Django Project

This Django project implements a bookstore application with CRUD (Create, Read, Update, Delete) functionality for managing books.

## Installation

To run this Django project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/engyahmed7/BookStore_Django.git
```

2. Navigate to the project directory:

```bash
cd BookStore_Django
```

3. Install the required dependencies:

```bash
pip install Django
```

4. Run the Django development server:

```bash
python manage.py runserver
```

5. Access the bookstore application in your web browser at `http://127.0.0.1:8000/book/`.

## Features

- **Create a New Book:** Users can add new books to the bookstore by providing details such as title, author, and description.

- **Show/Edit/Delete Specific Book:** Users can view, edit, or delete specific books based on their unique identifiers.

- **Display List of All Books:** Users can see a list of all books available in the bookstore.

## Project Structure

The project has the following structure:

- `base_templates/main`: Contains base templates for the main layout of the website.
- `bookStore`: Django app for managing books.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django project management script.

## Usage

- **Creating a New Book:** Navigate to the `/book/add` URL to add a new book. Fill in the required details such as title, author, and description, then click on the "Add Book" button.

- **Showing/Edit/Delete Specific Book:** Navigate to the `/book/<book_id>` URL to view a specific book. You can also edit or delete the book from this page.

- **Displaying List of All Books:** Navigate to the `/book/` URL to see a list of all books available in the bookstore.

## Screenshots

![Screenshot (314)](https://github.com/engyahmed7/BookStore_Django/assets/68815210/a1257304-07ad-4377-875d-bb5bf14cc4c9)

![Screenshot (315)](https://github.com/engyahmed7/BookStore_Django/assets/68815210/7a6a136b-2d63-495e-bd85-f0be17f0d089)

![Screenshot (316)](https://github.com/engyahmed7/BookStore_Django/assets/68815210/fae2d93a-6648-408e-b268-0fe601311fd5)

![Screenshot (317)](https://github.com/engyahmed7/BookStore_Django/assets/68815210/43936e02-65b3-4197-89ae-e694842dadae)

![Screenshot (318)](https://github.com/engyahmed7/BookStore_Django/assets/68815210/e2430a82-f3db-48c0-a4c0-37cb5c0d2bfe)

![Screenshot (319)](https://github.com/engyahmed7/BookStore_Django/assets/68815210/eae8420b-17f9-457d-929f-071fc7e989a7)

![Screenshot (320)](https://github.com/engyahmed7/BookStore_Django/assets/68815210/b20158a9-4208-493c-9f3f-e245c2c8cd01)


## Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests through the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
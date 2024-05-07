# Django Bookstore CRUD Application

This is a simple Django web application that allows users to perform CRUD (Create, Read, Update, Delete) operations on a bookstore. Users can view a list of books, add new books, edit existing books, and delete books.

## Features

- View a list of all books in the bookstore.
- Add new books with title, description, rating, views, and publication date.
- Edit existing books to update their information.
- Delete books from the bookstore.

## Installation

To run this application locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/engyahmed7/BookStore_Django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd BookStore_Django
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Setup MYSQL Database:

    ```bash
    pip install mysqlclient 
    ```

6. Create the migration:

    ```bash
    python manage.py makemigration
    ```

7. Apply migrations to create the database schema:

    ```bash
    python manage.py migrate
    ```

8. Create a superuser to access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

9. Start the development server:

    ```bash
    python manage.py runserver
    ```

10. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

## Usage

- Visit the homepage to view a list of all books in the bookstore.
- Click on the "Add New Book" button to add a new book to the bookstore.
- Click on the "Edit" button next to a book to edit its details.
- Click on the "Delete" button next to a book to delete it from the bookstore.

## Admin Interface

To access the Django admin interface:

1. Navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) in your web browser.
2. Log in with the credentials of the superuser you created earlier.
3. You can now manage books and other models through the admin interface.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

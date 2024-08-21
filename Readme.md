Flask Authentication System with Bootstrap 5

This project is a simple web application built with Flask that demonstrates user authentication using a login form. The application uses Flask-WTF for form handling and Bootstrap 5 for styling.
Features

    User login form with email and password validation
    Form validation and error handling
    Responsive design using Bootstrap 5
    Example success and denied pages based on login credentials

Technologies Used

    Flask: A lightweight WSGI web application framework in Python.
    Flask-WTF: An extension for Flask that simplifies form handling.
    Bootstrap 5: A popular CSS framework for responsive and modern web design.

Running the Application

    Clone the Repository


git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Activate the Virtual Environment

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Start the Flask Development Server

    flask run

    The application will be available at http://127.0.0.1:5000/.

Usage

    Home Page: Accessible at /. Displays a welcome message.
    Login Page: Accessible at /login. Use the form to enter your credentials.
        Valid credentials: admin@email.com and 12345678.
        Invalid credentials will redirect to a denied page.
    Success Page: Displays a success message upon correct login.
    Denied Page: Displays an error message for invalid login attempts.

Contributing

Feel free to fork the repository, create a branch, and submit pull requests for any improvements or bug fixes. Please ensure to follow proper coding standards and include relevant tests.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For any questions or feedback, please contact me at your-email@example.com.
# E-Receipt Generator

This project is an e-receipt generator application built with Flask. It allows users to generate and manage electronic receipts, providing a streamlined way to create and store digital records of transactions.

## Why This Project?

This project was initially developed for my Leo Club, aiming to provide a simple online system for generating and managing e receipts. The primary goal was to create a functional tool for club use, rather than a system designed with robust security features in mind. It serves as a straightforward solution for basic e receipt generation.

## How It Works

The core functionality of this application revolves around image manipulation. It utilizes a pre designed JPG e receipt template. The Python Imaging Library (Pillow) is then employed to dynamically overlay and render text onto this base image, effectively creating a personalized e receipt.

## Technologies Used

- **Backend Framework:** Flask
- **Programming Language:** Python 3.12.7
- **Database:** MySQL (via `mysqlclient`)
- **ORM:** SQLAlchemy, Flask-SQLAlchemy
- **User Authentication:** Flask-Login
- **Forms:** Flask-WTF, WTForms
- **Image Processing:** Pillow
- **Templating Engine:** Jinja2

## How to Run Locally

Follow these steps to set up and run the e-receipt generator on your local machine:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

    (Replace `<repository_url>` with the actual URL of your GitHub repository.)

2.  **Navigate to the project directory:**

    ```bash
    cd e-receipt-generator
    ```

3.  **Create a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.

    ```bash
    python3 -m venv venv
    ```

4.  **Activate the virtual environment:**

    - **On macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```
    - **On Windows:**
      ```bash
      .\venv\Scripts\activate
      ```

5.  **Install dependencies:**
    Install all required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

6.  **Database Setup:**

    - Ensure you have a MySQL server running on your system.
    - Create a database named `<your_database_name>`. You can do this via your MySQL client (e.g., MySQL Workbench, command line):
      ```sql
      CREATE DATABASE <your_database_name>;
      ```
    - The application is configured using the `SQLALCHEMY_DATABASE_URI` variable in `config.py`.
    - Before running the application, copy `config.example.py` to `config.py`:
      ```bash
      cp config.example.py config.py
      ```
    - Then, open `config.py` and update the `SQLALCHEMY_DATABASE_URI` with your MySQL credentials and database name. For example:
      ```python
      SQLALCHEMY_DATABASE_URI = "mysql://<DB_USERNAME>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>"
      ```
      Replace `<DB_USERNAME>`, `<DB_PASSWORD>`, `<DB_HOST>`, `<DB_PORT>`, and `<DB_NAME>` with your actual database details.
    - The necessary database tables will be automatically created when the application runs for the first time due to `db.create_all()` in `run.py`.

7.  **Run the application:**
    Start the Flask development server:

    ```bash
    python run.py
    ```

8.  **Access the application:**
    Open your web browser and navigate to `http://0.0.0.0:3000` (or `http://localhost:3000`).

## How to Contribute

We welcome contributions to the E-Receipt Generator project! If you'd like to contribute, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name` or `git checkout -b bugfix/your-bug-fix`.
3.  **Make your changes** and ensure your code adheres to the project's coding standards.
4.  **Write clear, concise commit messages.**
5.  **Push your branch** to your forked repository.
6.  **Open a Pull Request** to the `main` branch of the original repository, describing your changes in detail.

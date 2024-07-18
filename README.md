# UrbanCart
Welcome to UrbanCart, a modern eCommerce platform built with Next.js and various technologies to deliver a robust and user-friendly shopping experience.

<img src="https://github.com/wisdom-geek/UrbanCart/blob/main/static/assets/imgs/display/UrbanCart2.png" alt="Urban Cart Logo" width="1000" heigth="400">

# Overview
UrbanCart is designed to provide a seamless shopping experience with features that cater to both customers and administrators. It leverages 
html, css and javascript for frontend development, integrating with various technologies for authentication, database management, and UI/UX enhancements.

# Features
1. User Authentication and Management
- Secure user authentication
- User roles and permissions management
- Activity logging
2. Product Management
- Create, read, update, and delete products
- Tagging system for products
- Search functionality
3. Miscellaneous
- Responsive design using Bootstrap
- Admin panel with Django Jazzmin for better UI

# Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Django
- Database: SQLite (with plans to migrate to PostgreSQL)
- Dependencies: 
- - `asgiref==3.8.1`
- - `Django==5.0.7`
- - `django-jazzmin==3.0.0`
- - `django-shortuuidfield==0.1.3`
- - `django-taggit==5.0.1`
- - `pillow==10.4.0`
- - `python-dotenv==1.0.1`
- - `shortuuid==1.0.13`
- - `six==1.16.0`
- - `sqlparse==0.5.0`
- - `tzdata==2024.1`

# Getting Started
## Prerequisites
- Python installed on your system
- Django installed


# Step 1: Clone the Project
1. Open your command line or terminal.
2. Navigate to the directory where you want to store your Django project.
3. Clone the project from GitHub:
    ```bash
    git clone https://github.com/wisdom-geek/UrbanCart
    ```
# Step 2: Create a Virtual Environment
1. Navigate to the project directory:
    ```bash
    cd ecomprj
    ```
2. Create a virtual environment:
    ```bash
    cd ecomprj
    ```
3. Activate the virtual environment:
  - On Windows: 
      ```bash
         venv\Scripts\activate
      ```
  - On macOS and Linux:
      ```bash
        source venv/bin/activate
      ```
# Step 3: Install Dependencies
1. Ensure you're in the project directory with the virtual environment activated.
2. Install the project dependencies using pip:
    ```bash
        pip install -r requirements.txt
    ```
# Step 4: Set Up the Database
1. Create the database tables and apply migrations:
    ```bash
        python manage.py migrate
    ```
2. Create a superuser account:
    ```bash
        python manage.py createsuperuser
    ```
# Step 5: Run the Development Server
1. Start the Django development server:
    ```bash
        python manage.py runserver
    ```
2. Open your web browser and access the development server at http://127.0.0.1:8000/.

# Step 6: Access the Admin Panel
- To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in using the superuser account credentials you created earlier.


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create your feature branch:
    ```bash
    git checkout -b feature-name
    ```
 
3. Commit your changes: 
    ```bash
    git commit -am 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Submit a pull request


# Support and Assistance

If you have any questions about the codebase or encounter issues while working on it, feel free to reach out for assistance. Here are some ways to get support:

- **Contact:** You can reach out [Ambrose](ambrosemusyoka254@gmail.com) for assistance or clarification on any aspect of the code.
- **Documentation:** Refer to the project's documentation for guidance on setup, usage, and troubleshooting.

- **Issue Reporting:** If you encounter bugs or unexpected behavior, please report them by opening a new issue in the [GitHub Issues](https://github.com/wisdom-geek/UrbanCart/issues) section of this repository. Provide as much detail as possible, including steps to reproduce the issue, your environment, and any relevant logs or screenshots.
We're here to help ensure a smooth experience with the codebase and to address any questions or concerns you may have.

## Contact
Created by [Ambrose](ambrosemusyoka254@gmail.com) - feel free to contact me!

# Things to come
## Dockerization
We plan to dockerize the application to simplify deployment across different environments. Docker will encapsulate the application, its dependencies, and settings into a container.

## PostgreSQL Setup
We'll migrate from SQLite to PostgreSQL for improved scalability and performance. PostgreSQL offers robust features suitable for production environments.

## Payment Gateway Integrations
### Mpesa Integration
Integrate Mpesa for seamless mobile payments. This will involve setting up APIs, handling transactions securely, and ensuring compliance with Mpesa's guidelines.
### PayPal Integration
Implement PayPal for international payments. Users will be able to securely complete transactions using their PayPal accounts, enhancing payment flexibility.

## Checkout Page
Develop a robust checkout page to streamline the purchasing process. This page will handle order details, payment processing, and confirmation, ensuring a smooth user experience.

## API Documentation with Swagger
Add documentation using Swagger in Django to provide clear and interactive API documentation.

Stay tuned for updates as we implement these exciting features!😊😊
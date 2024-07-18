# UrbanCart
Welcome to UrbanCart, a modern eCommerce platform built with Next.js and various technologies to deliver a robust and user-friendly shopping experience.

<img src="https://github.com/wisdom-geek/UrbanCart/blob/main/static/assets/imgs/display/UrbanCart2.png" alt="Urban Cart Logo" width="1000" heigth="400">

# Overview
UrbanCart is designed to provide a seamless shopping experience with features that cater to both customers and administrators. It leverages 
html, css and javascript for frontend development, integrating with various technologies for authentication, database management, and UI/UX enhancements.


# Technologies Used
- Python: Backend logic and Django framework.
- HTML/CSS/JavaScript: Frontend development for templating and dynamic interactions.
- Django Packages:
- - django-jazzmin: Customized admin interface.
- - django-taggit: Tagging support for products.
- - django-shortuuidfield: UUID field support.

# Features
1. User Authentication: Secure user authentication using Django's built-in authentication system and additional plugins.
2. Product Management: Manage products with features like CRUD operations, categories, and image uploads.
3. Custom Admin Interface: Enhanced admin interface using django-jazzmin for improved user experience.
4. Tagging System: Utilize django-taggit for tagging products with categories and other labels.
5. Data Persistence: Ensure data integrity and efficiency with PostgreSQL 

# Installation
To run this project locally, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/wisdom-geek/UrbanCart
    ```
2. Navigate to the project directory:
    ```bash
    cd ecomprj
    ```
3. Set up the virtual environment (recommended):
    ```bash
       python -m venv venv
       source venv/bin/activate  # On macOS/Linux
       env\Scripts\activate  # On Windows
    ```
4. Install dependencies:
    ```
      pip install -r requirements.txt
    ```
5. Set up the database:
   ```
      python manage.py migrate
      python manage.py createsuperuser
   ```
6. Access the application:
    Open a web browser and go to http://127.0.0.1:8000/ to view the application.

# Configuration
Before running the project, configure your environment variables:


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

Stay tuned for updates as we implement these exciting features!😊😊
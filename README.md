# THREADORY - E-Commerce Store (College Mini-Project)

**THREADORY** is a modern, feature-rich e-commerce web application developed as a college mini-project. Built using the Django framework, it demonstrates the practical application of full-stack web development concepts. Designed with a clean, aesthetically pleasing, and responsive user interface, it provides a complete shopping experience with advanced features like secure payments, product management, user profiles, and interactive shopping cart functionality.

## Features

*   **Responsive User Interface:** Fully responsive design built with HTML, CSS, and modern UI elements, ensuring a seamless experience across devices (desktop, tablet, and mobile). Includes a visually appealing dark mode compatibility.
*   **User Profiles & Authentication:** Secure user registration, robust login systems, and profile management capabilities. Users can view and update their account details, view order history, and manage their preferences.
*   **Product Catalog & Management:** 
    *   Browse products with diverse categories (Accessories, Shoes, Sweaters, Men's, Women's, etc.).
    *   Dynamic product detail pages featuring multi-image galleries and a customized product hover flip effect.
    *   Interactive pagination for catalog browsing.
    *   Advanced product filtering and search capabilities.
*   **Shopping Cart & Checkout:**
    *   Fully functional, asynchronous shopping cart allowing users to add, update, and remove items seamlessly.
    *   Wishlist functionality enabling users to save their favorite products for later.
*   **Secure Payment Integration:** Integrated with Stripe Payment Gateway for secure and reliable transaction processing (test mode support).
*   **Interactive Engagement:** Includes product reviews and ratings to facilitate community trust and engagement.
*   **Robust Backend:** Built on Django, utilizing its powerful ORM and security features to securely manage user data, inventory, and transactions.

## Technologies Used

*   **Backend:** Python 3.x, Django
*   **Frontend:** HTML5, Vanilla CSS, JavaScript
*   **Database:** SQLite (default for development, scalable to PostgreSQL/MySQL)
*   **Payment Gateway:** Stripe API

## Getting Started

Follow these instructions to set up a local copy of THREADORY for development and testing.

### Prerequisites

*   Python 3.8+ installed on your local machine.
*   `pip` package manager.
*   A Stripe Developer account for testing payments (optional but recommended for full testing).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/threadory.git
    cd threadory
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    *   **macOS and Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, ensure you install `django`, `stripe`, and `pillow`)*

5.  **Configure Environment Variables:**
    *   Set up your Stripe API keys in your `settings.py` or through an `.env` file for secure configuration:
        *   `STRIPE_PUBLIC_KEY`
        *   `STRIPE_SECRET_KEY`

6.  **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Create a Superuser (Admin account):**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

9.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`. You can access the admin panel at `http://127.0.0.1:8000/admin/`.

## Contributing

Contributions are welcome! If you'd like to improve THREADORY, feel free to fork the repository, make changes, and submit a pull request. 
Please ensure your code adheres to standard styling guidelines and includes appropriate comments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

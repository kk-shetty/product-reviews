### Web Scraping Project Documentation
This documentation provides an overview of a web scraping project that fetches product information from Flipkart.com based on user-entered keywords. The project is implemented using Flask, a Python web framework, and includes multiple files and HTML templates.

#### Project Overview
The project allows users to search for products on Flipkart.com by entering keywords on the home page. The application then scrapes the website to fetch relevant product details, including the product name, ratings, overall ratings, and price. The retrieved information is displayed on the results page in a user-friendly format. The project consists of the following components:

1. `application.py`: The main Flask application file that handles routing, web scraping logic, and rendering of HTML templates.
2. `custom_methods.py`: A separate Python module that contains custom methods used in the web scraping process.
3. `index.html`: The home page HTML template with an input field and a search button for entering the product keywords.
4. `result.html`: The results page HTML template that displays the product details fetched from Flipkart.com.
5. `reviews.html` (not included in the provided code): An additional HTML template that can be implemented to display detailed product reviews if the user clicks on a specific product.

#### Dependencies
The project relies on the following dependencies:

* Flask: A Python web framework for creating the application and handling routing.
* Flask-Cors: A Flask extension that enables cross-origin resource sharing (CORS) to handle requests from different domains.
* requests: A library for making HTTP requests to fetch web page content.
* pymongo (optional): A MongoDB library for database operations if required.
Ensure that these dependencies are installed before running the project.

#### Project Structure
The project files and directories are structured as follows:

```
├── application.py
├── custom_methods.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── index.html
    ├── result.html
    └── reviews.html (optional)
```

* `application.py`: This file contains the main Flask application logic, including routing, web scraping, and rendering of HTML templates.
* `custom_methods.py`: This file contains custom methods used for web scraping, specifically the read_to_html method that reads a URL and returns the HTML content.
* `static/css/style.css`: This CSS file contains styles for the HTML templates.
* `templates/index.html`: The home page HTML template with an input field and search button for entering keywords.
* `templates/result.html`: The results page HTML template that displays the fetched product details.
* `templates/reviews.html` (optional): An additional HTML template that can be implemented to display detailed product reviews.

#### Usage
To run the project:

1. Ensure that the required dependencies are installed.
2. Place the provided files in the appropriate structure as mentioned above.
3. Run the `application.py` file using the Python interpreter.
4. Access the application in a web browser by visiting `http://localhost:5000` or the appropriate address specified by the Flask application.
5. On the home page (`index.html`), enter keywords for the desired product and click the search button.
6. The application will scrape Flipkart.com for products matching the keywords and display the results on the results page (`result.html`).
7. Optionally, if the user clicks on a specific product, the application can display detailed product reviews on the `reviews.html` page.

#### Additional Functionality
The project includes some additional features and functionality:

* **Logging**: The application includes logging functionality that logs events and errors to a file named application.log. This can
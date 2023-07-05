# Import necessary libraries
from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS, cross_origin
import requests
import pymongo
import logging

from cutom_methods import read_to_html

# Initializing logging
logging.basicConfig(filename="application.log", level=logging.DEBUG)

# Initializing a flask app
application = Flask(__name__)
app = application


# route to display home page
@app.route("/")
def home():
    """ This method will be executed on home page and will render index.html
    """
    return render_template("index.html")

# route method for /search
@app.route("/search", methods=['POST','GET'])
def search():
    """ This method will be executed after clicking on search button from homepage - index.html
    """
    if(request.method == 'POST'):
        # Fetch search key word from input
        searchString = request.form['search']
        flipkart_url = "https://www.flipkart.com/search?q=" + searchString.replace(" ", "%20")  #.replace is used to remove any white space 

        search_page = read_to_html(flipkart_url, logging)
        # All individual items are under div class = _4ddWXP -- for flipkart. 
        if(search_page.find_all("div", {"class" : "_4ddWXP"})):
            # If the results are displayed in grid format
            product_search_result = search_page.find_all("div", {"class" : "_4ddWXP"})
            display = 'grid'
        elif(search_page.find_all("div", {"class" : "_1AtVbE col-12-12"})):
            # If the results are displayed in list format
             product_search_result = search_page.find_all("div", {"class" : "_1AtVbE col-12-12"})
             display = 'list'
        logging.info(f"Found : {len(product_search_result)} results")

        # Initialize a list to store all the dictionary of individual products 
        products = []

        # Loop though the product_search_result and append the product details to a list
        for product in product_search_result:

            # Initialize a dict to store relevent details
            product_dict = {}

            # Try to fetch product title
            try:
                if display == 'grid':
                    title = product.find_all("a", {"class" : "s1Q9rs"})[0]['title']
                else:
                    title = product.find("div", {"class" : "_4rR01T"}).text
            except Exception as e:
                logging.error(f"TITLE: {e}")
                title = ''
            finally:
                product_dict['title'] = title
            
            # Try to fetch product url 
            try:
                if display == 'grid':
                    url = product.find_all("a", {"class" : "s1Q9rs"})[0]['href']
                else:
                    url = product.find_all("a", {"class" : "_1fQZEK"})[0]['href']
            except Exception as e:
                logging.error(f"HREF: {e}")
                url = ''
            finally:
                product_dict['url'] = url
            
            # Try to fetch product rating 
            try:
                # Convert the ratings from string format to floating point numbers
                rating = float(product.find("div", {"class" : "_3LWZlK"}).text) # _3LWZlK
            except Exception as e:
                logging.error(f"RATING: {e}")
                logging.debug(product.find("div", {"class" : "_3LWZlK"}))
                rating = ''
            finally:
                product_dict['rating'] = rating
            
            # Try to fetch total Ratings 
            try:
                if display == 'grid':
                     # Below statment will also convert string representation of a number with commas into an integer
                    total_tratings = product.find("span", {"class" : "_2_R_DZ"}).text.replace(',', '').replace('(', '').replace(')', '')   # span _2_R_DZ
                else:
                    total_tratings = product.find("span", {"class" : "_2_R_DZ"}).span.span.text.split(" ")[0].replace(',', '')
            except Exception as e:
                logging.error(f"TOTAL RATINGS: {e}")
                logging.debug(product.find("span", {"class" : "_2_R_DZ"}))
                total_tratings = ''
            finally:
                product_dict['total_tratings'] = total_tratings
            
            # Try to fetch product price 
            try:
                if display == 'grid':
                    price = product.find("div", {"class" : "_30jeq3"}).text
                else:
                    price = product.find("div", {"class" : "_30jeq3 _1_WHN1"}).text
            except Exception as e:
                logging.error(f"PRICE: {e}")
                price = ''
            finally:
                product_dict['price'] = price

            products.append(product_dict)
        
        for product in products:
            logging.info(f"{product['title']} : {product['rating']} : {product['total_tratings']} : {product['price']}")
        return render_template('result.html', products = products)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    logging.info("START: application started")

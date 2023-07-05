from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

def read_to_html(url, logging):
    """ THis method will access the give url, reads it and return the content in html format
    """
    # Initialize page_content variable to empty string. return the same if request fails
    page_content = ''
    try:
        logging.info(f"Requesting URL : {url}")
        uClient = uReq(url)
    except Exception as e:
        logging.error(f"Request failed - {e}")
    else:
        # Override page_content with actual content of the requested URL
        page_content = uClient.read()
        uClient.close()
        logging.info(f"URL Request : {url} - Read and closed succesfully")
        # logging.info(page_content)
    finally:
        return bs(page_content, "html.parser")
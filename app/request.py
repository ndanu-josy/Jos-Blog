import urllib.request,json
from .models import Quote

# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_URL']

def getQuotes(): 
    """
    Function to consume the url and return quotes
    """
    with urllib.request.urlopen(base_url) as url:
        quotesData = url.read()
        qoutesResponse = json.loads(quotesData)
        print(quotesResponse)
        qoutesList = []
        id = quotesResponse.get('id')
        author = quotesResponse.get('author')
        quote = quotesResponse.get('quote')

        quoteObject = Quote(id,author,quote)
        qoutesList.append(quoteObject)
        return quoteList


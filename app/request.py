import urllib.request,json
from .models import Quote

# Getting the movie base url


def getQuotes(): 
    """
    Function to consume the url and return quotes
    """
    QUOTE_API_URL='http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(QUOTE_API_URL) as url:
        quotesData = url.read()
        qoutesResponse = json.loads(quotesData)
        # print(quotesResponse)

       
        id = qoutesResponse.get('id')
        author = qoutesResponse.get('author')
        quote = qoutesResponse.get('quote')

        quoteObject = Quote(id,author,quote)
      
        return quoteObject


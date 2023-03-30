import requests
from bs4 import BeautifulSoup


def get_proverbs(): 
    """ 
        Gets proverbs from website 
    """
    url = "https://www.phrases.org.uk/meanings/proverbs.html"
    response = requests.get(url)
    html_page = response.content
    soup = BeautifulSoup(html_page, 'html.parser')
    elements = soup.findAll('p', attrs={'class': 'phrase-list'})
    proverb_list = _extract_proverbs(elements)
    return proverb_list


def _extract_proverbs(elements):
    """
        Eliminates proverbs with some annotation etc.
    """
    substrings = [" - ", ";", "]", ".", "?", "nowt"]
    proverb_list = list()
    for element in elements:
        text = element.getText().strip()
        if any(sub in text for sub in substrings):
            continue
        else:
            proverb_list.append(text)
    return proverb_list

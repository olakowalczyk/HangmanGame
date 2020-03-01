import requests
from bs4 import BeautifulSoup

def get_proverbs(): # gets proverbs from website
    url = "https://www.phrases.org.uk/meanings/proverbs.html"
    res = requests.get(url)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')
    elements = soup.findAll('p', attrs={'class' : 'phrase-list'}) 

    proverb_list=[]
    proverb_list = extract_proverbs(proverb_list, elements)
    return proverb_list
    
def extract_proverbs(proverb_list, elements): # eliminates proverbs with some annotation etc.
    for element in elements:
        element.getText()
        proverb_list.append(element.getText())

    subs = [" - ",";","]",".","?", "nowt"] # 
    for i in proverb_list[:]:
        for sub in subs[:]:
            if sub in i:
                proverb_list.remove(i)
    return proverb_list

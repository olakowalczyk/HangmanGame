import requests
from bs4 import BeautifulSoup


class Proverbs:

    def __init__(self):
        self.proverbs_list = Proverbs.get_proverbs_from_url()


    def __str__(self):
        return f"The list of proverbs ({len(self.proverbs_list)} elements):\n {self.proverbs_list}"


    def __len__(self):
        return len(self.proverbs_list)


    def __getitem__(self, item):
        return self.proverbs_list[item]


    @classmethod
    def get_proverbs_from_url(cls): 
        url = "https://www.phrases.org.uk/meanings/proverbs.html"
        response = requests.get(url)
        html_page = response.content
        soup = BeautifulSoup(html_page, 'html.parser')
        web_elements = soup.findAll('p', attrs={'class': 'phrase-list'})
        return Proverbs._extract_proverbs(web_elements)


    @staticmethod
    def _extract_proverbs(elements):
        """
            Eliminates proverbs with some annotation etc.
        """
        substrings = [" - ", ";", "]", ".", "?", "nowt"]
        proverbs_list = list()
        for element in elements:
            text = element.getText().strip()
            if any(sub in text for sub in substrings):
                continue
            else:
                proverbs_list.append(text)
        return proverbs_list

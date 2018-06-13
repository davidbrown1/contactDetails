from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class SearchByParameters:
    def __init__(self, query: dict, lang: str, num_of_result_pages: int):
        self.query = query
        self.all_query = ' '.join(map(str, query.values()))
        self.google_results = None
        self.num_of_result_pages = num_of_result_pages
        self.lang = lang
        self.tld = SearchByParameters.get_tld_and_contact_trans_by_country(lang='il')
        self.contact = SearchByParameters.get_tld_and_contact_trans_by_country(lang='il')

    #     todo build query to get contact details from google
    def build_query(self):
        """
        get query params from object instance, and build the query string by google advanced search
        :return: query to search
        """
        pass

    def search_details_with_google(self):
        """
        search contact in google search, and update contact details in the self.details dictionary
        :return:
        """
        pass
        details = company = None  # todo implement the google search
        if self.details.get(company):
            for k, v in details:
                self.details[company][k].add(v)
            print('DO SOMETHING - COMPARE THE DIC AND UPDATE, add details to set')
        else:
            self.details[company] = {"for on all exist contact details, and added with k & v, value entered in set"}

    def result_from_google(self, res_num=12):
        """
        search about business by the desired parameters (google land domain, language, limit of result,
            pause between searches
        :param res_num:
        :return: list of business url's
        """
        self.google_results = [q for q in search(self.all_query, tld=self.tld, num=res_num, stop=self.num_of_result_pages, pause=3, hashes = set())]
        return self.google_results

    def get_xml_elements(self, url):
        self.url = url
        r = requests.get(url)
        self.soup = BeautifulSoup(r.content)
        return self.soup

    def get_contact_us(self):
        self.soup.findAll('a', href=True)
        src = [contact_us for contact_us in self.soup.findAll(
            'a', href=True) if 'contact us' in contact_us.text.lower() or contact_us.text.lower() == 'צור קשר']
        if src:
            link = src[0]['href']
            self.link = link if link.startswith('http') else urljoin(self.url, link)
            return self.link

    def get_details(self):
        r = requests.get(self.link)
        phones = re.findall(r"\(\d{3}\) \d{3}-\d{4}", r.content)
        emails = re.findall(r'([\w\.-]+@[\w\.-]+\.[\w]+)+', r.content)
        return phones, emails

    @staticmethod
    def get_tld_and_contact_trans_by_country(lang):
        tld_dic = {'us': 'com', 'uk': 'co.uk', 'france': 'fr', 'italy': 'it', 'il': 'co.il'}
        contact_dic = {'us': 'contact_us', 'uk': 'contact_us', 'france': 'fr', 'italy': 'it', 'il': 'צור קשר'}
        return tld_dic.get(lang, 'co.il'), contact_dic.get(lang, 'צור קשר')

    def start_scraping(self):
        self.search_details_with_google()
        self.result_from_google()


try:
    q = SearchByParameters('shoes store', lang='il')
    # q.result_from_google()
    q.get_xml_elements("https://www.tami4.co.il/reverse-osmosis")

    # q.get_xml_elements(q.google_result[-1])
#     q.get_contact_us()
#     print(q.get_details())
except Exception as e:
    print(e)

# todo if not self.link dont run get details, TODO custom contact us by lang and by string playing

# contact us, Customer Experience, help, Email Us, write to us, About Us, contact in href, צור קשר, יצירת קשר
# itemprop="telephone", <a href="tel:00441506468733">+44 1506 468 733</a>, type=email, type=tel, name=firstname, lastname, tag address


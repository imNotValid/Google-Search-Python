# Cr imNotValid Cr imNotValid Cr imNotValid
# Cr imNotValid Cr imNotValid Cr imNotValid
# Cr imNotValid Cr imNotValid Cr imNotValid
from random import choice
from json import loads
from utils.exceptions import QueriesNotFound
from bs4 import BeautifulSoup
from requests import get
from html import unescape
from re import (
    compile,
    sub
)

def randomUserAgent():
    with open("./utils/userAgents.txt", "r") as r:
        result = choice(r.read().split("\n"))
        r.close()
    return {"User-Agent": result}
class searcher:
    def __init__(self, proxies: dict=None, userAgent=None):
        """
        Get cookies from google.com and create a new session
        Args:     
            Proxy:defult (dict) -> None
            userAgent:defult (str) -> .randomUserAgent()
        """
        self.__tagDeleter = compile(r"<.*?>")
        self.__queryCompletionUrl = "https://www.google.com/complete/search"
        self.__searchUrl = "https://www.google.com/search"
        if userAgent:
            self.__headers = {"User-Agent": userAgent}
        else:
            self.__headers =  randomUserAgent()
        self.__proxies = proxies
    def __SendRequest(self, url, params):
        return get(
            url,
            params,
            proxies=self.__proxies,
            headers=self.__headers
        )
    def getQuery(self, query: str):
        """
        Args:
            query (str): query for search
        result (dict):
            list of query
        """        
        params = {
			"q": query,
			"client": "gws-wiz",
            "hl": "en",
			"xssi": "t",
			"pq": query
		}
        try:
            queries = loads(unescape(self.__SendRequest(self.__queryCompletionUrl, params).text.split("\n", 1)[1]))[0]
        except IndexError:
            raise QueriesNotFound("There are no queries to search")
        return self.__filterStringsAndDict(queries)
    def searchQuery(self, query: str, page: int=1):
        """
        Args:
            query (str): query for search
            page (int, optional): page number for search - Defaults to 1.

        Returns:
            list of (title, link)
        """        
        params = {
            "q": query,
            "hl": "en",
            "sclient": "gws-wiz",
            "start": 10
        }
        return self.__getInfo(self.__SendRequest(self.__searchUrl, params).text)
    def __deleteTag(self, arg): return sub(self.__tagDeleter, "", arg)
    def __filterStringsAndDict(self, arg): return [self.__deleteTag(list(filter(lambda x: type(x) is str, li))[0]) for li in arg]
    def __getInfo(self, text):
        find = []
        soup = BeautifulSoup(text, "html.parser")
        for result in soup.find_all("div", attrs={"class": "g"}):
            title = result.find("h3").get_text()
            link = result.find("a", href=True)["href"]
            find.append((title, link))
        return find

if __name__ == "__main__":
    cls = searcher(userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0")
    print(cls.searchQuery("khazar sea"))
    # > [('Caspian Sea: Largest Inland Body of Water - Live Science', 'https://www.livescience.com/57999-caspian-sea-facts.html')...
    print(cls.getQuery("khazar sea"))
    # > ['khazar sea', 'khazar sea shipping lines', 'are sea shepherds still active', 'who are the hasidim'...

from bs4 import BeautifulSoup 
import requests
import random


async def extract_quote(url):
        results = []
        request = requests.get(url).text
        soup = BeautifulSoup(request, "html.parser")
        for quote in soup.find_all("div", class_= "quote"):
            reponse = quote.find("div", {"class": "quoteText"}).text
            results.append(response.replace('\n', ' ').strip())
        return results

async def random_quote(self):
        pgno = random.randint(1, 100)
        quoteurl = f"https://www.goodreads.com/quotes?format=html&mobile_xhr=1&page={pgno}"
        results = await extract_quote(quoteurl) 
        return random.choice(results)    
        
async def search_quotes(search_query, pages=1):
            pgno = random.randint(1, 5)
            quoteurl = f"https://www.goodreads.com/quotes/search?commit=Search&page={page}&q={search_query.replace(' ', '+')}&utf8=%E2%9C%93"
            results = await extract_quote(quoteurl)
            return random.choice(results)   

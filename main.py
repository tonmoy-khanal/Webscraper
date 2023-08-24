from scraper.weather_api import Weather_API
from scraper.web_scraping import Web_Scraping

def main():
    keyword = input('Enter Keyword to be searched: ').lower()
    w_api = Weather_API(keyword)
    w_api.news_api()

    location = input('Enter Location: ').lower()
    ws = Web_Scraping(location)
    ws.selenium_webdriver()

if __name__ == "__main__":
    main()
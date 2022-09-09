from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from requests import get
from extractors.wwr import extract_wwr_jobs

base_url = 'https://kr.indeed.com/jobs?q='
search_term = 'python'
chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)
browser.get(f"{base_url}{search_term}")
print(browser.page_source)
time.sleep(2)
browser.close()
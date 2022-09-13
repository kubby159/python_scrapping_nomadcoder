from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from requests import get
from extractors.wwr import extract_wwr_jobs


def get_page_count(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get(f'{base_url}{keyword}')
    browser.implicitly_wait(10)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    page_lists = soup.select('ul.pagination-list li')

    if page_lists == []:
        print("There're not Paginaiton")
    else:
        for page in page_lists:
            print(page.text)


get_page_count('nest')


def extract_indeed_jobs(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get(f'{base_url}{keyword}')
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    job_list = soup.find('ul', class_='jobsearch-ResultsList')
    jobs = job_list.find_all('li', recursive=False)
    results = []
    for job in jobs:
        zone = job.find('div', class_='mosaic-zone')
        if zone == None:
            anchor = job.select_one("h2 a")
            title = anchor['aria-label']
            link = anchor['href']
            company = job.find('span', class_='companyName')
            location = job.find('div', class_='companyLocation')
            job_data = {
                "link": f"https://kr.indeed.com{link}",
                "company": company.string,
                "location": location.string,
                "position": title
            }
            results.append(job_data)

    for result in results:
        print(result, "\n///////\n")

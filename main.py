from bs4 import BeautifulSoup
from requests import get
from extractors.wwr import extract_wwr_jobs


jobs = extract_wwr_jobs('python')
print(jobs)








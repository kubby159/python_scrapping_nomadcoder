from bs4 import BeautifulSoup
from requests import get

base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_term = "python"


response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs_posts = soup.find_all('section', class_='jobs')
    jobs_posts.pop(-1) # 가장 마지막 데이터 제거.
    for job_section in jobs_posts:
        job_posts = job_section.find_all('li')
        for post in job_posts:
            print(post.text)


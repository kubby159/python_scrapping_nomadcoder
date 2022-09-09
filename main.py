from bs4 import BeautifulSoup
from requests import get

base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_term = "python"


response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    results = []
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('section', class_='jobs')
    for job_section in jobs:
        jobs_posts = job_section.find_all('li')
        jobs_posts.pop(-1)
        for post in jobs_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            company, kind, region = anchor.find_all('span', class_='company')

            title = anchor.find('span', class_='title')
            job_data = {
                "company": company.string,
                "kind": kind.string,
                "region": region.string,
                "title": title.string
            }
            results.append(job_data) #list 안에 저장하기.

        for result in results:
            print(result)









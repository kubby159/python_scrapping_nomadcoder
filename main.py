from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
      soup = BeautifulSoup(request.text, "html.parser")

      # write your ✨magical✨ code here
      result = soup.select('a.preventLink')
      for x in result:
        print(x.getText().strip())

    else:
      print("Can't get jobs.")

extract_jobs("rust")


from bs4 import BeautifulSoup
import requests

def extract_remoteok_jobs(term):
  
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    ok_results= []
    soup = BeautifulSoup(request.text, "html.parser")
    
    ok_jobs = soup.find_all('tr', class_="job")
    for ok_job in ok_jobs:
      ok_link = ok_job.find('a', class_ ="preventLink")
      ok_link = f"https://remoteok.com/{ok_link['href']}"
      ok_location = ok_job.find('div', class_="location")
      ok_title = ok_job.find('h2', itemprop = "title")
      ok_company = ok_job.find('h3', itemprop = "name")

      ok_job_data = {
        'link': ok_link, 
        'company': ok_company.string.strip().replace(","," "), 
        'location': ok_location.string.replace(","," "),
        'position': ok_title.string.strip().replace(","," "),
      }
      ok_results.append(ok_job_data)
    return ok_results
  else:
    print("Can't get jobs.")
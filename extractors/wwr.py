##requests를 import
from requests import get
##BeautifulSoup import
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  ##base_url을 만들어 검색하는 단어마다 다른 주소가 나오면 합쳐준다
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  ##<Response [200]> 웹사이트의 상태를 호출
  response = get(f"{base_url}{keyword}")
  ##request가 성공이 아니면 문구출력
  if response.status_code != 200:
    print("Can't request website")
  else:
    ##빈리스트를 만들어서 job_data 딕셔너리를 받는다
    results=[ ]
    ##.text 웹사이트를 구성하고 있는 코드를 가져온다
    ##"html.parser"뷰티풀숩에게 html을 보내준다.
    ##html코드 중에서 필요한 데이터를 뽑을 수 있도록
    soup = BeautifulSoup(response.text, "html.parser")
    ##section 안에서 jobs를 가진 class를 추출 * 2개
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      ##li의 아이템을 하나씩 추출
      job_posts = job_section.find_all('li')
      ##.pop마지막 아이템 제거
      job_posts.pop(-1)
      for post in job_posts:
        ##1번째 a에는 로고이미지가 링크되어있기 때문에
        anchors = post.find_all('a')
        ##a를 다 불러와서 그 중에 2번째 링크만 쓴다
        anchor = anchors[1]
        link = anchor['href']
        ##언팩, 파이썬에서는 리스트의 길이를 알면 같은 개수만큼의 변수에 한번에 넣을 수 있다
        company, kind, location = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        ##추출한 데이터를 딕셔너리로 만들어준다
        job_data = {
          'link': f"https://weworkremotely.com/{link}",
          'company': company.string.replace(","," "),
          'location': location.string.replace(","," "),
          'position': title.string.replace(","," ")
        }
        ##job을 추출해서 for loop밖의 빈리스트 result에 넣는다
    
        results.append(job_data)
      return results
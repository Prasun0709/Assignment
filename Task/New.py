import requests
from bs4 import BeautifulSoup

def get_latest_stories():
    url = 'https://time.com'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        stories = []
        story_tags = soup.find_all('a', class_='headline-link')
        
        for tag in story_tags[:6]:  # Extracting the latest 6 stories
            title = tag.get_text()
            link = tag['href']
            stories.append({'title': title, 'link': link})
        
        return stories
    else:
        print("Failed to fetch data from Time.com")
        return None

latest_stories = get_latest_stories()
if latest_stories:
    for story in latest_stories:
        print("Title:", story['title'])
        print("Link:", story['link'])
        print()


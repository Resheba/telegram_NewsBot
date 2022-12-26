from newsapi import NewsApiClient
from config import NEWS_API_TOKEN

newsApi = NewsApiClient(api_key=NEWS_API_TOKEN)

async def searchNews(q: str):
    newsDirtDict = newsApi.get_everything(q=q)
    newsClearList = newsDirtDict.get('articles')
    return newsClearList

async def clearData(new: dict):
	sourceName = new.get('source').get('name')
	title = new.get('title')
	description = new.get('description').replace('<ol>', '').replace('<li>', '').replace('</li>','').replace('</ol>', '')
	url = new.get('url')
	thumb_url = new.get('urlToImage')
	result = dict(sourceName=sourceName, title=title, description=description, url=url, thumb_url=thumb_url)
	return result

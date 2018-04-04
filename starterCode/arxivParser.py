import feedparser
# import re
# from bs4 import BeautifulSoup

def parseRss(url='https://arxiv.org/rss/physics.optics'):
  """ RSS Feed URL -> list of dictionaries for first five articles
  
  This function returns a list of dictionaries with the keys 'abstract', 'articleId', 'authors', 'title', and 'url'
  for the first five articles on the specified arXiv RSS Feed url.
  
  The values for each of the five keys must be strings.
  
  The string for the authors key should parse the list of authors received from the feed into one single string.
  
  The default argument url='https://arxiv.org/rss/physics.optics' shows an example of the expected input.
  """
  
  #YOUR CODE HERE: programmatically producing the articleList of dictionaries described above
    
  articlesList = [{}]
  return articlesList

import os
from gtts import gTTS
from wordcloud import WordCloud

exampleArticlesList=[{'abstract':'Cracked Pots Lecture','authors':'J. Carberry','articleId':'1801.99999','title':'Pyschoceramics','url':'https://arxiv.org/abs/1801.99999'}]
exampleDirectory='public_files'
def createAudioFiles(articlesList=exampleArticlesList, directoryPath=exampleDirectory):
  """  list of article dictionaries -> 
  For each article, create an MP3 audio file that includes title, authors, and abstract.
  MP3 files should be stored in the specified directoryPath.
  """

def createWordCloudImages(articlesList=exampleArticlesList, directoryPath=exampleDirectory):
  """ list of article dictionaries -> 
  For each article, create a square PNG image file using the words from the abstract.
  PNG files should be stored in the specified directoryPath.
  """

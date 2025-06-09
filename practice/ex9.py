!pip install konlpy
from konlpy.tag import Okt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

with open('todayhotnews.txt') as f:
  data = f.readlines()
okt = Okt()
noun_text = ''
for sentence in data:
  for noun in okt.nouns(sentence):
    if len(noun) < 2:
      pass
    elif noun == '이경규':
      noun_text += '장윤형 '
    else:
      noun_text += noun + ' '
mask_image = np.array(Image.open('apple.jpg'))
wc = WordCloud(font_path='NanumSquareEB.ttf',
               background_color = 'white',
               mask = mask_image,
               max_words=200,
               max_font_size=70,
               min_font_size=10,
               colormap='magma').generate(noun_text)
wc.to_file('wc.png')
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path
from PIL import Image
import numpy as np

d = path.dirname(__file__)

f = open(path.join(d,'a_new_hope.txt')).read()

alice_coloring = np.array(Image.open(path.join(d , 'panda.')))

wordcloud = WordCloud(background_color='white', width=1000, height=860, margin=2, mask=alice_coloring).generate(f)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('sanguo.png')



from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt 
import jieba 
from wordcloud import WordCloud, ImageColorGenerator

# 获取当前文件路径
d = path.dirname(__file__)

stopwords = {}
isCN = 1 #默认启用中文分词
back_coloring_path = 'alice.png'
text_path = 'sanguo.txt'
font_path = 'font/msyh.ttc'
stopwords_path = ''
image1 = 'panda2.jpg'
image2 = 'test.png'

back_coloring = imread(path.join(d, back_coloring_path)) #背景图片

#设置词云属性
wc = WordCloud(font_path=font_path,#字体
               background_color="white",#背景颜色
               max_words=2000,#词云显示的最大词数
               mask=back_coloring,#背景图片
               max_font_size=100,#字体最大值
               random_state=42,
               width=1000, height=860, margin=2
        )

text = open(path.join(d, text_path), encoding='UTF-8').read()

wc.generate(text)
image_colors = ImageColorGenerator(back_coloring)

plt.figure()
#以下代码显示图片
plt.imshow(wc)
plt.axis('off')
plt.show()

#保存图片
wc.to_file(path.join(d, image1))


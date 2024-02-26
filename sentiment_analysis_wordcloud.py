import csv
# import pandas as pd
import numpy as np
# from collections import defaultdict
# import os
# import re
import jieba
# import codecs
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import wordcloud as wc
import matplotlib.pyplot as plt
# from scipy.misc import imread
# from imageio import imread
from PIL import Image
import csv
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

#note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
#from vaderSentiment import SentimentIntensityAnalyzer
# --- examples -------
with open('230711_microsoft_wins_ftc_fight_to_buy_activision.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)
sentences = [row[1] for row in data[1:]]
# print(lst)
analyzer = SentimentIntensityAnalyzer()
sum = {'neg': 0,
       'neu': 0,
       'pos': 0}
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
    # print(format(str(vs)))
    if vs['compound'] >= 0.45:
        sum['pos'] += 1
    elif vs['compound'] <= -0.01:
        sum['neg'] += 1
    elif vs['compound'] == 0:
        pass
    else:
        sum['neu'] += 1
# print(sum)

# # word cloud
# with open('230711_microsoft_wins_ftc_fight_to_buy_activision.csv','r',encoding='utf-8') as f:
#     stopwords=set([line.replace('\n','')for line in f])
# f.close()
# def clean_data(content):
#     words =' '
#     for seg_text in content:
#         seg_text=jieba.cut(seg_text)
#         for seg in seg_text:
#             if seg not in stopwords and seg!=" " and len(seg)!=1:    # #文本清洗
#                   words = words +  seg + ' '
#     return words
# # print(clean_data(sentences))
#
# def Cloud_words(words):
#     # 引入字体
#     font = r"C:/Windows/Fonts/simhei.ttf"
#     # mask = np.array(Image.open('love.png'))
#     #     image_colors = ImageColorGenerator(mask)
#     # 从文本中生成词云图
#     cloud = wc.WordCloud(font_path=font,  # 设置字体
#                          background_color='black',  # 背景色为白色
#                          height=800,  # 高度设置为400
#                          width=800,  # 宽度设置为800
#                          scale=20,  # 长宽拉伸程度程度设置为20
#                          prefer_horizontal=0.2,  # 调整水平显示倾向程度为0.2
#                          # mask=mask,  # 添加蒙版
#                          max_font_size=200,  # 字体最大值
#                          max_words=1000,  # 设置最大显示字数为1000
#                          relative_scaling=0.3,  # 设置字体大小与词频的关联程度为0.3
#
#                          )
#     # 绘制词云图
#     mywc = cloud.generate(words)
#     plt.imshow(mywc)
#     mywc.to_file('unnamed.png')
#
# Cloud_words(clean_data(sentences))

with open('output_sentence_analysis.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['Top 10 Words', 'Sentiment'])
    for sentence in sentences:
        # 对句子进行分词
        words = word_tokenize(sentence)
        # 获取前十个单词
        top_10_words = words[:10]
        # 进行情感分析
        vs = analyzer.polarity_scores(sentence)
        # 计算情感分析的总和
        sentiment_sum = vs['pos'] - vs['neg']
        # 将前十个单词和情感分析的总和写入到CSV文件中
        writer.writerow([' '.join(top_10_words), sentiment_sum])



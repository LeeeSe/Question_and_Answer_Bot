from pygtrans import Translate
import time

client = Translate()

# 翻译句子
t1 = time.time()
text1 = client.translate('Look at these pictures and answer the questions.', 'zh-CN')
t2 = time.time()
text2 = client.translate('我和小明同时开始游泳，我先游了一米，又游了三米，他总共游了五米。请问谁游得更远一些？', 'en')
t3 = time.time()
print(t3 - t2, t2 - t1)
print(text1.translatedText)
print(text2.translatedText)



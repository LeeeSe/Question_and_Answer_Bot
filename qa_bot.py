import time

from zh_en_api import zh2en
from en_zh_api import en2zh
from text_text_api import text2text
from pygtrans import Translate

client = Translate()

# 输入中文，输出中文
def qa_robot(text):
    t1 = time.time()
    text_en = zh2en(text)
    t2 = time.time()
    response_en = text2text(text_en)
    t3 = time.time()
    response_zh = en2zh(response_en)
    t4 = time.time()
    print(f'中译英时间:{t2 - t1}\n'
          f'回复时间:{t3 - t2}\n'
          f'英译中时间:{t4 - t3}\n'
          f'总时间:{t4 - t1}\n'
          f'中文:{text}\n'
          f'英文:{text_en}\n'
          f'英文回复:{response_en}\n'
          f'中文回复:{response_zh}')
    return response_zh


# 输入中文，输出中文
def qa_robot_2(text):
    t1 = time.time()
    text_en = client.translate(text, 'en').translatedText
    t2 = time.time()
    response_en = text2text(text_en)
    t3 = time.time()
    response_zh = client.translate(response_en, 'zh-CN').translatedText
    t4 = time.time()
    print(f'中译英时间:{t2 - t1}\n'
          f'回复时间:{t3 - t2}\n'
          f'英译中时间:{t4 - t3}\n'
          f'总时间:{t4 - t1}\n'
          f'中文:{text}\n'
          f'英文:{text_en}\n'
          f'英文回复:{response_en}\n'
          f'中文回复:{response_zh}')
    return response_zh


if __name__ == '__main__':
    print(qa_robot_2("守夜人的头领是谁？"))

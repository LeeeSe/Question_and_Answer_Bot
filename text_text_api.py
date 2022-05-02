import requests
import json

# 调用huggingface的opus-mt-en-zh模型接口
# 定义header
headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://huggingface.co',
    'Content-Length': '51',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Host': 'api-inference.huggingface.co',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
    'Referer': 'https://huggingface.co/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'x-use-cache': 'false'
}


def text2text(text):
    data = {"inputs": text}
    response = requests.post(url='https://api-inference.huggingface.co/models/bigscience/T0pp',
                             headers=headers,
                             data=json.dumps(data))

    if len(response.json()) > 0:
        return response.json()[0]['generated_text']
    else:
        return "没有结果"


if __name__ == '__main__':
    text = 'I am a student.'
    print(text2text(text))

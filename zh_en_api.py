import requests


def zh2en(text):
    response = requests.post(
        url="http://82.156.199.33:8002/v1/models/zh-en/predict",
        json={
            "data": text
        },
    )
    return response.json()['data'][0]['translation_text']


if __name__ == "__main__":
    print(zh2en("你在干吗？"))

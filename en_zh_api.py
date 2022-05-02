import requests


def en2zh(text):
    response = requests.post(
        url="http://82.156.199.33:8001/v1/models/en-zh/predict",
        json={
            "data": text
        },
    )
    return response.json()['data'][0]['translation_text']


if __name__ == "__main__":
    print(en2zh("what are you doing？"))

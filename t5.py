from transformers import pipeline
from pinferencia import Server

t5 = pipeline(model="Question_and_Answer_Bot-small", tokenizer="Question_and_Answer_Bot-small")


def translate(text):
    return t5(text)


service = Server()
service.register(model_name="Question_and_Answer_Bot", model=translate)

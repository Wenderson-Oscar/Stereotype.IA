import chainlit as cl
import requests
from api_gemini import ConfigGemini


def query(txt: str):
    conf = ConfigGemini(txt)
    conf.configure_model()
    return conf.get_ia_response()

@cl.on_message
async def main(message: cl.Message):
    ia = query(message.content)
    await cl.Message(ia).send()

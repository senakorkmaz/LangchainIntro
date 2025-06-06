from http.client import responses

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()
messages = [
    SystemMessage(content="Translate the following from English to Spanish"),
    HumanMessage(content="Hi!")
]

parser = StrOutputParser()
chain = model | parser


if __name__ == "__main__":
    print(chain.invoke(messages))
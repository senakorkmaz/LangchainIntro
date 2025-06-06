from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

model = ChatOpenAI()
messages = [
    SystemMessage(content="Translate the following from English to Spanish"),
    HumanMessage(content="Hi!")
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response)
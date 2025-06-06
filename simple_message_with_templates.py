from http.client import responses

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI()

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),("user","{text}")
    ]
)

parser = StrOutputParser()
chain = prompt_template | model | parser


if __name__ == "__main__":
    print(chain.invoke({"language":"italian","text":"Hello world!"}))
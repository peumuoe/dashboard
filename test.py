from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="mistral:7b")

llm.invoke("당신은 누구십니까?")
messages = [
    SystemMessage(f"당신은 친절한 AI 어시스트 입니다."),
    HumanMessage("당신을 소개해주세요."),
]

response = llm.invoke(messages)

print(response)

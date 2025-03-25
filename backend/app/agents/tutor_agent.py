#ChatGPT generated file as part of project setup
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(temperature=0.7)

template = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are an AI tutor. Teach the user a lesson on the topic: {topic}.
    Include explanations, examples, and a short quiz at the end."""
)

def generate_lesson(topic: str):
    chain = LLMChain(llm=llm, prompt=template)
    return chain.run(topic)
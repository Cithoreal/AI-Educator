#ChatGPT generated file as part of project setup
from langchain.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.schema import Document

import os

CHROMA_DIR = "data/chroma_db"

def get_vectorstore():
    embedding_fn = OpenAIEmbeddings()
    return Chroma(persist_directory=CHROMA_DIR, embedding_function = embedding_fn)

def save_lesson_to_memory(lesson_title: str, content: str):
    vectorstore = get_vectorstore()
    doc = Document(page_content=content, metadata={"title": lesson_title})
    vectorstore.add_documents([doc])
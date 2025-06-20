#!/usr/bin/env python
# coding: utf-8

# In[ ]:




# In[ ]:


from langchain_groq import ChatGroq
llm = ChatGroq(
    temperature = 0,
    groq_api_key = "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",
    model_name = "llama-3.3-70b-versatile"
)
result = llm.invoke("what is langchain in machine learning")
print(result.content)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:





# In[1]:





# In[1]:


from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
import os

def initialize_llm():  
    llm = ChatGroq(
        temperature=0,
        groq_api_key="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",
        model_name="llama3-70b-8192"
    )
    return llm

def create_vector_db():
    loader = DirectoryLoader(
        "C:\\Desktop\\coding\\chatbot\\data",
        glob='*.pdf',
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )
    vector_db = Chroma.from_documents(
        texts, 
        embeddings, 
        persist_directory='./chroma_db'
    )
    print("Chroma DB created and data saved")
    return vector_db

def setup_qa_chain(vector_db, llm):
    retriever = vector_db.as_retriever()
    prompt = PromptTemplate(
        input_variables=["context","question"],
        template="Use the following context to answer the question.\nContext: {context}\nQuestion: {question}\nAnswer:"
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return qa_chain

def main():
    print("Initializing ChatBot...")
    llm = initialize_llm()

    db_path = "C:\\Desktop\\coding\\chatbot\\chroma_db"

    if not os.path.exists(db_path):
        vector_db = create_vector_db()
    else:
        vector_db = Chroma(persist_directory=db_path, embedding_function=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))

    qa_chain = setup_qa_chain(vector_db, llm)

    while True:
        user_input = input("Enter your question: ")
        if user_input.lower() == "exit":
            print("ChatBot:Take Care of Yourself. Goodbye!")
            break
        
        
        result = qa_chain({"query": user_input})
       
        print("ChatBot:", result.get("result", "")) 
        

if __name__ == "__main__":    
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





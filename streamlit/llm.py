
from langchain_upstage import ChatUpstage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_upstage import UpstageEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_classic.chains import RetrievalQA

def get_ai_message(user_message):
    
    embedding = UpstageEmbeddings(model='solar-embedding-1-large')
    index_name = 'tax-vector-index'
    database = PineconeVectorStore.from_existing_index(index_name=index_name,embedding=embedding)
    
    llm = ChatUpstage(model="solar-mini4")
    # hub.pull() 대신 직접 작성한 소득세 답변용 프롬프트
    tax_prompt = PromptTemplate.from_template("""
    주어진 문서를 참고하여 사용자의 질문에 답변해주세요.
    문서에 근거가 없다면 모른다고 답변해주세요.

    Context:
    {context}

    Question: {question}
    """)
    retriever = database.as_retriever(search_kwargs={'k': 4})
    
    qa_chain = RetrievalQA.from_chain_type(
    llm, retriever=retriever,chain_type_kwargs={"prompt": tax_prompt})

    dictionary = ["사람을 나타내는 표현 -> 거주자"]
    
    prompt = ChatPromptTemplate.from_template(f"""
    사용자의 질문을 보고, 우리의 사전을 참고해서 사용자의 질문을 변경해주세요.
    만약 변경할 필요가 없다고 판단된다면, 사용자의 질문을 변경하지 않아도 됩니다.
    그런 경우에는 질문만 리턴해주세요
    사전: {dictionary}
    
    질문: {{question}}""")

    dictionary_chain = prompt | llm | StrOutputParser()
    tax_chain = {"query": dictionary_chain} | qa_chain
    ai_message = tax_chain.invoke({"question": user_message})
    return ai_message["result"]

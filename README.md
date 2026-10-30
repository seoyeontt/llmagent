## LLM Application Development with LangChain

프로젝트 소개

LangChain과 Upstage Solar LLM을 활용하여 소득세 관련 질문에 답변하는 RAG 기반 챗봇을 개발했습니다. 소득세 관련 문서를 벡터 데이터베이스에 저장하고, 사용자 질문과 관련된 문서를 검색하여 이를 바탕으로 답변을 생성하도록 구현했습니다.

기술 스택

Language: Python

LLM: Upstage Solar (solar-mini4)

Framework: LangChain

Embedding: Upstage Embeddings (solar-embedding-1-large)

Vector Database: Pinecone

Web Application: Streamlit

주요 구현 기능

RAG 기반 질의응답: 검색된 소득세 문서를 바탕으로 답변 생성

문서 임베딩 및 저장: 소득세 문서를 벡터로 변환하여 Pinecone에 저장

유사도 기반 검색: 사용자 질문과 관련된 문서를 검색

LLM 연동: LangChain을 통해 검색 결과와 LLM을 연결

대화형 웹 애플리케이션: Streamlit을 이용한 챗봇 인터페이스 구현

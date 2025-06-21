This is a Flipkart Product Assistant.
# Problem Statement:
Let's say we visit flipkart to search for Headphones (to buy a pair for yourself). We often read reviews and rating of the product and based on those feedback we decide whether to buy that product or not.

To automate and simply this process we built a RAG based customer support chatbot.
Any User that comes over the website will have a chatbot (powered by RAG based architecture running product on information). He has to simply ask questions to that chatbot and go through bot concise-accurate bot response to have the best products based on user reviews and ratings.

# RAG Architecture Used:
![Blank diagram](https://github.com/user-attachments/assets/77f84e4b-aa2a-417c-bb02-ad50fdd36d14)

# Components Used:
1) Embedding LLM Model Used: Google-Gemini - "text-embedding-004"
2) Generating LLM Model Used: Groq - "meta-llama/llama-4-scout-17b-16e-instruct"
3) Vector DB Used: Astra DB (provided by IBM)
4) Retrieval Technique Used: Self Query Retrieval + Cross Encoder Reranking.

# Self Retriever Close Look
![SelfQueryRetriever](https://github.com/user-attachments/assets/f5afa352-6ac4-448f-bc9e-c3bcbe1bbd88)

# How to Launch the project
1) Clone the repo
   - git clone https://github.com/Manas2001Agarwal/customer_support_system.git
   - cd customer_support_system
2) Set Up Virtual Env
   - Use Conda : conda create --name myenv python=3.9
   - conda activate myenv
3) Install Dependencies
   - pip install -r requirements.txt
4) Set up .env file with below token
    - ASTRA_DB_API_ENDPOINT = 
    - ASTRA_DB_APPLICATION_TOKEN = 
    - ASTRA_DB_KEYSPACE = 
    - GOOGLE_API_KEY = 
    - HF_TOKEN = 
    - GROQ_API_KEY = 
    - PINECONE_API_KEY = 
    - TAVILY_API_KEY = 
5) Run main.py
   - uvicorn main:app --reload --port 8001
# Working Demo - Screenshot
<img width="1205" alt="Screenshot 2025-06-18 at 1 43 36 AM" src="https://github.com/user-attachments/assets/f6933d6f-b1a8-42d3-a624-f56c34bcf7ee" />

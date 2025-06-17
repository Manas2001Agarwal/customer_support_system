This is a Flipkart Product Assistant.
# Problem Statement:
Let's say we visit flipkart to search for Headphones (to buy a pair for yourself). We often read reviews and rating of the product and based on those feedback we decide whether to buy that product or not.

To automate and simply this process we built a RAG based customer support chatbot.
Any User that comes over the website will have a chatbot (powered by RAG based architecture running product information). He has to simply ask questions to that chatbot and go through bot concise-accurate bot response to have the best products based on user reviews and ratings.

# RAG Architecture Used:
![Blank diagram](https://github.com/user-attachments/assets/d072fe9a-133f-4340-97a9-9641657b8e18)

# Components Used:
1) Embedding LLM Model Used: Google-Gemini - "text-embedding-004"
2) Generating LLM Model Used: Groq - "meta-llama/llama-4-scout-17b-16e-instruct"
3) Vector DB Used: Astra DB (provided by IBM)
4) Retrieval Technique Used: Self Query Retrieval + Cross Encoder Reranking.


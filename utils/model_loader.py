import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config=load_config()
        
    def _validate_env(self):
        """
        Validate necessary environment variables.
        """
        required_vars = ["HF_TOKEN","GOOGLE_API_KEY","GROQ_API_KEY"]
        self.hf_token=os.getenv("HF_TOKEN")
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")
        
    def load_embeddings(self):
        """
        Load and return the embedding model.
        """
        print("Loading Embedding model")
        model_name=self.config["embedding_model"]["model_name"]
        return GoogleGenerativeAIEmbeddings(model=model_name)
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        
        model_name=self.config["llm"]["model_name"]
        groq_model=ChatGroq(model=model_name,max_tokens=250)
        #gemini_model=ChatGoogleGenerativeAI(model=model_name)

        return groq_model 
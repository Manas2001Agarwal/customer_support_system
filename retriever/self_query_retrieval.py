import os
from langchain_astradb import AstraDBVectorStore
from typing import List
from langchain_core.documents import Document
from utils.config_loader import load_config
from utils.model_loader import ModelLoader

from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever


from dotenv import load_dotenv

class Self_Query_Retriever:
    
    def __init__(self):
        self.model_loader=ModelLoader()
        self.config=load_config()
        self._load_env_variables()
        self._load_metadata()
        self.vstore = None
        self.retriever = None
    
    def _load_env_variables(self):
         
        load_dotenv()
         
        required_vars = ["HF_TOKEN","GOOGLE_API_KEY", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN", "ASTRA_DB_KEYSPACE"]
        
        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.db_api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
        self.db_application_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
        self.db_keyspace = os.getenv("ASTRA_DB_KEYSPACE")
        self.hf_token = os.getenv("HF_TOKEN")
        
    def _load_metadata(self):
        self.metadata_field_info = [
            AttributeInfo(
                name="product_name",
                description="The name of the product",
                type="string",
            ),
            AttributeInfo(
                name="product_summary",
                description="Summary of the product review left by user",
                type="string",
            ),
            AttributeInfo(
                name="product_rating", description="A 1-5 rating for the product", type="float"
            )
        ]
        
        self.document_content_description = "Online Product review left by customer on Ecommerce Website"
        
    def load_retriever(self):
        if not self.vstore:
            collection_name = self.config["astra_db"]["collection_name"]
            
            self.vstore = AstraDBVectorStore(
                embedding= self.model_loader.load_embeddings(),
                collection_name=collection_name,
                api_endpoint=self.db_api_endpoint,
                token=self.db_application_token,
                namespace=self.db_keyspace,
            )
        if not self.retriever:
            top_k = self.config["retriever"]["top_k"] if "retriever" in self.config else 3
            
            retriever = SelfQueryRetriever.from_llm(
                llm = self.model_loader.load_llm(),
                vectorstore = self.vstore,
                document_contents = self.document_content_description,
                metadata_field_info = self.metadata_field_info)
            
            print("Retriever loaded successfully.")
            return retriever
       
    def call_retriever(self,query:str)-> List[Document]:
        retriever=self.load_retriever()
        output=retriever.invoke(query) # type: ignore
        return output
        
    
if __name__=='__main__':
    retriever_obj = Self_Query_Retriever()
    user_query = "Can you suggest me some laptops with ratings greater than 3?"
    results = retriever_obj.call_retriever(user_query)

    for idx, doc in enumerate(results, 1):
        print(f"Result {idx}: {doc.page_content}\nMetadata: {doc.metadata}\n")
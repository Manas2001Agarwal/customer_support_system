from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import pandas
import os
from data_ingestion.data_transform import DataConverter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv('ASTRA_DB_API_ENDPOINT')
ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"] = ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = ASTRA_DB_APPLICATION_TOKEN
os.environ["ASTRA_DB_KEYSPACE"] = ASTRA_DB_KEYSPACE

class IngestData:
    
    def __init__(self):
        self.model = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")
        self.data_converter = DataConverter()
    
    def data_ingestion(self,status):
        vstore = AstraDBVectorStore(
            embedding=self.model,
            collection_name="chatbotecom",
            api_endpoint = ASTRA_DB_API_ENDPOINT,
            token = ASTRA_DB_APPLICATION_TOKEN,
            namespace = ASTRA_DB_KEYSPACE
        )
        storage = status
        
        if storage == None:
            docs = self.data_converter.data_transformation()
            inserted_ids = vstore.add_documents(docs)
            print(inserted_ids)
            
        else:
            return vstore
        
        return vstore,inserted_ids
    
if __name__ == "__main__":
    data_ingestion_process = IngestData()
    vstore = data_ingestion_process.data_ingestion(True)
    #print(f"Number of Documents inserted in Vector DB = {len(index_id)}")
    # results = vstore.similarity_search("can you tell me some low budget headphones")
    # for re in results:
    #     print(re.page_content)
    #     print(re.metadata)
            
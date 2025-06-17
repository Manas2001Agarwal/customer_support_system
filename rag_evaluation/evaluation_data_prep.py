from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from retriever.retrieval import Retriever
from utils.model_loader import ModelLoader
from prompt_library.prompt import PROMPT_TEMPLATES
from dotenv import load_dotenv
from tqdm import tqdm
from datasets import Dataset
import pandas as pd
from langchain.prompts import ChatPromptTemplate

load_dotenv()

retriever_obj = Retriever()

model_loader = ModelLoader()

def naive_retrieval_invoke_chain(query:str):
    
    retriever=retriever_obj.load_retriever()
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATES["product_bot"])
    llm= model_loader.load_llm()
    
    chain=(
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    
    )
    
    context = retriever_obj.call_retriever(query)
    
    output=chain.invoke(query)
    
    return output,context

def create_ragas_dataset(eval_dataset,rag_chain):
  rag_dataset = []
  for row in tqdm(eval_dataset):
    answer,context = rag_chain(row["question"])
    rag_dataset.append(
        {"question" : row["question"],
         "answer" : answer,
         "contexts" : [cnt.page_content for cnt in context],
         "ground_truths" : [row["ground_truth"]]
         }
    )
  rag_df = pd.DataFrame(rag_dataset)
  rag_eval_dataset = Dataset.from_pandas(rag_df)
  return rag_eval_dataset

if __name__ == "__main__":
    eval_dataset = pd.read_csv("/Users/mukulagarwal/Desktop/Projects/customer_support_system/rag_test_data.csv")
    basic_qa_ragas_dataset = create_ragas_dataset(eval_dataset,naive_retrieval_invoke_chain)
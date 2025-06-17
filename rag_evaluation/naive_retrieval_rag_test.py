import ast
from ragas import EvaluationDataset
from utils.model_loader import ModelLoader

from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness, LLMContextPrecisionWithReference
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
import pandas as pd

model_loader = ModelLoader()

evaluator_llm = model_loader.load_llm()
evaluator_llm = LangchainLLMWrapper(evaluator_llm)

def evaluate_ragas_dataset():
    rag_test = pd.read_csv("/Users/mukulagarwal/Desktop/Projects/customer_support_system/rag_evaluation/naive_retrieval_rag_test_data.csv")
    
    rag_test = rag_test.rename(columns={
    'question' : 'user_input',
    'contexts' : 'retrieved_contexts',
    'answer' : 'response',
    'ground_truths' : 'reference'})
    
    rag_test['retrieved_contexts'] = rag_test['retrieved_contexts'].apply(ast.literal_eval)
    
    
    evaluation_dataset = EvaluationDataset.from_pandas(rag_test)
    result = evaluate(
        evaluation_dataset,
        metrics=[
        LLMContextRecall(), Faithfulness(), FactualCorrectness(), LLMContextPrecisionWithReference()
        ],
        llm=evaluator_llm
    )
    return result

if __name__ == "__main__":
    evaluate_ragas_dataset()
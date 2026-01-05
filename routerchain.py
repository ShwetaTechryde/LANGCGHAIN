import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing. Set it in .env or the environment.")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.4,
)

policy_prompt = PromptTemplate.from_template(
    """
You are an Indian health insurance expert.
Explain POLICY related questions in very simple language.

Question:
{input}
"""
)

claim_prompt = PromptTemplate.from_template(
    """
You are an Indian health insurance claims expert.
Explain CLAIM related questions in very simple language.

Question:
{input}
"""
)

policy_chain = policy_prompt | llm
claim_chain = claim_prompt | llm

router_chain = RunnableBranch(
    (lambda x: "claim" in x["input"].lower(), claim_chain),
    (lambda x: "policy" in x["input"].lower(), policy_chain),
    policy_chain,  # Default fallback
)

if __name__ == "__main__":
    user_question = "How do I claim my health insurance?"

    response = router_chain.invoke({"input": user_question})

    print("\nAI Response:\n")
    print(response.content)

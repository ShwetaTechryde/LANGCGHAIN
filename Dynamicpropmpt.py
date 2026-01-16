import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing. Set it in .env or the environment.")

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.7,
)

policy_prompt = PromptTemplate(
    template="""
    Suggest a suitable {policy_type} insurance policy
    for a customer aged {age} with annual income {income}.
    Explain in simple bullet points.
    """,
    input_variables=["policy_type", "age", "income"]
)

final_prompt = policy_prompt.format(
    policy_type="Term Life",
    age=19,
    income="19 LPA"
)

response = llm.invoke(final_prompt)
print(response.content)
# Expected output: A simplified explanation of health insurance policy benefits tailored for a non-technical audience in India.

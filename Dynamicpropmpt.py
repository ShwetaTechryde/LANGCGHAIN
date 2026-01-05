from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

OPENAI_API_KEY="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"


llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.7
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
    policy_type="Auto",
    age=12,
    income="19 LPA"
)

response = llm.invoke(final_prompt)
print(response.content)
# Expected output: A simplified explanation of health insurance policy benefits tailored for a non-technical audience in India.
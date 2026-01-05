from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

OPENAI_API_KEY="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"


llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.7
)

prompt = """
Explain Health Insurance policy benefits in simple terms
for a technical customer in India.
"""

response = llm.invoke(prompt)
print(response.content)
# Expected output: A simplified explanation of health insurance policy benefits tailored for a non-technical audience in India.
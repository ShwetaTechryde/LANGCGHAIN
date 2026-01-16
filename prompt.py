import os

from dotenv import load_dotenv
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

prompt = """
Explain Health Insurance policy benefits in simple terms
for a technical customer in India.
"""

response = llm.invoke(prompt)
print(response.content)
# Expected output: A simplified explanation of health insurance policy benefits tailored for a non-technical audience in India.

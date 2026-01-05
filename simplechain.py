from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY="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"


llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.5
)

prompt_template = PromptTemplate(
    input_variables=["customer_type"],
    template="""
You are an expert health insurance advisor in India.

Think internally step-by-step to understand the customer.
Customer type: {customer_type}

Rules:
- Use very simple language
- Avoid technical terms
- Use Indian examples
- Friendly tone
- Do NOT show internal reasoning

Explain health insurance benefits.
"""
)

insurance_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

response = insurance_chain.invoke(
    {"customer_type": "Non-technical Indian customer"}
)

print(response["text"])

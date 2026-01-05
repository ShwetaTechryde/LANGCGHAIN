from langchain_openai import ChatOpenAI

OPENAI_API_KEY="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"

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.6
)

prompt = """
You are an insurance expert in India.

Think step by step internally to understand:
1. The user is non-technical
2. They want to understand health insurance benefits
3. Keep language very simple

Then provide:
- Simple explanation
- Bullet points
- USA examples
- Friendly tone

Do NOT show internal reasoning.
Only give the final answer.
"""

response = llm.invoke(prompt)

print(response.content)

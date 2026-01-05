from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

OPENAI_API_KEY="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"


llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.7
)

examples = [
    {
        "claim_amount": "50,000",
        "policy_active": "Yes",
        "hospital": "Network",
        "decision": "Approved"
    },
    {
        "claim_amount": "2,00,000",
        "policy_active": "No",
        "hospital": "Network",
        "decision": "Rejected"
    }
]

example_prompt = PromptTemplate(
    input_variables=["claim_amount", "policy_active", "hospital", "decision"],
    template="""
    Claim Amount: {claim_amount}
    Policy Active: {policy_active}
    Hospital Type: {hospital}
    Decision: {decision}
    """
)
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="You are an insurance claim assessor.",
    suffix="""
    Claim Amount: {claim_amount}
    Policy Active: {policy_active}
    Hospital Type: {hospital}
    Decision:
    """,
    input_variables=["claim_amount", "policy_active", "hospital"]
)


final_prompt = few_shot_prompt.format(
    claim_amount="1,20,000",
    policy_active="Yes",
    hospital="Network"
)
response = llm.invoke(final_prompt)
print(response.content)
# Expected output: A simplified explanation of health insurance policy benefits tailored for a non-technical audience in India.
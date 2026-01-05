from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import  SequentialChain,LLMChain

llm = ChatOpenAI(
    openai_api_key="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",
    model="gpt-4o-mini",
    temperature=0.5
)
# )

# profile_prompt = PromptTemplate(
#     input_variables=["age", "income","Smoking","City"],
#     template="Customer age: {age}, income: {income}, smoking: {Smoking}, city: {City}. Classify risk level according to city pollution."
# )

# profile_chain = LLMChain(llm=llm, prompt=profile_prompt, output_key="risk")

# recommend_prompt = PromptTemplate(
#     input_variables=["risk"],
#     template="Suggest best health insurance policy for {risk} risk customer in India according to pollution levels."
# )

# recommend_chain = LLMChain(llm=llm, prompt=recommend_prompt, output_key="policy")


# seq_chain = SequentialChain(
#     chains=[profile_chain, recommend_chain],
#     input_variables=["age", "income", "Smoking", "City"],
#     output_variables=["risk", "policy"]
# )

# output = seq_chain.invoke({"age": 35, "income": "9 LPA", "Smoking": "No", "City": "Nanital"})
# print(output)



# from langchain.chains import SimpleSequentialChain

# simplify_prompt = PromptTemplate(
#     input_variables=["text"],
#     template="Simplify this cricket text for Indian cricket Team: {text}"
# )

# simplify_chain = LLMChain(llm=llm, prompt=simplify_prompt)
# simplify_chain=llm|simplify_chain

# example_chain = SimpleSequentialChain(
#     chains=[simplify_chain]
# )

# print(example_chain.invoke("ODI , IPL"))



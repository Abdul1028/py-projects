import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain_experimental.agents.agent_toolkits import create_csv_agent

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0.5)

agent = create_csv_agent(llm,"my_csv_data.csv",verbose=True)

res = agent.invoke("how many rows and columns are there ?")

print(type(res))
print(res["output"])
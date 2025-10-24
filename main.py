from langchain.agents import create_agent
from langchain_ollama.chat_models import ChatOllama


def main():

    print("Hello from main")

    ollama_host = "http://morpheus:8080" 
    llm = ChatOllama(model="gpt-oss", base_url=ollama_host) 

    
    agent = create_agent(
        model=llm,
        tools = [],
        system_prompt="You are a helpful research assistant." )

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": "Tell me something about San Francisco, in one or two sentences at most."}
        ]
    })

    print( "Result: ", result['messages'][1].content)
    

if __name__ == "__main__":
    main()

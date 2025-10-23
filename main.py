from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama.chat_models import ChatOllama


@tool
def search_web( query, limit ):
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    
    pass


@tool
def analyze_data():
    """Analyze the data and decide what to do
    """

    pass


@tool
def send_email():
    """Send the notification email"""
    pass


def main():

    print("Hello from langgraph-1!")



    ollama_host = "http://morpheus:8080" 
    llm = ChatOllama(model="llama3.3", base_url=ollama_host) 

    
    agent = create_agent(
        model=llm,
        tools = [],
        # tools=[search_web, analyze_data, send_email],
        system_prompt="You are a helpful research assistant." )

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": "Tell me something about San Francisco, in one or two sentences at most."}
        ]
    })

    print( "Result: ", result[1].content )
    

if __name__ == "__main__":
    main()

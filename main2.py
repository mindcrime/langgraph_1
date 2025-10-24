from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama.chat_models import ChatOllama


@tool
def get_weather( cityName ):
    """Search for weather details by cityName and returns the weather for a given city.

    Args:
        cityName: the city for which to return the weather 
    """
    print( f"get_weather called for cityName: {cityName}" )    
    return "It's 72° Fahrenheit, sunny, and clear."


@tool
def get_art_scene(cityName):
    """
    Search for a description of the art scene in a given city, searching by cityName.

    Args:
        cityName: the city for which to return the art scene description.
    """
    print( f"get_art_scene called for cityName: {cityName}")
    return "There is a vibrant and diverse art scene, encompassing world-class institutions like STROVA, a thriving landscape of independent galleries, and iconic, colorful street murals, particularly in the Ironclad District."

def main():

    print("Hello from main2")


    ollama_host = "http://morpheus:8080" 
    llm = ChatOllama(model="gpt-oss", base_url=ollama_host) 

    
    agent = create_agent(
        model=llm,
        tools = [get_weather,get_art_scene],
        system_prompt="You are a helpful research assistant." )

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": "Tell me something about San Francisco, in one or two sentences at most. Also tell me about the weather and the art scene there."}
        ]
    })
    
    print( "Result: ", result['messages'][5].content)
    

if __name__ == "__main__":
    main()

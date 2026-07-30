from tavily import TavilyClient
from dotenv import load_dotenv
import os 

# Load environment variables and initialize Tavily client
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search(query, search_depth):
    """Searches the web using the Tavily API and retrieves formatted results.

    Initializes the Tavily client with a static API key, executes a search 
    based on the provided query and depth, and parses up to 10 results 
    into a structured list of dictionaries containing titles, URLs, and snippets.

    Args:
        query (str): The search query to be executed.
        search_depth (str): The depth of the search, which can be 'basic' 
            for faster execution or 'advanced' for deeper exploration.

    Returns:
        list or tuple: A list of dictionaries containing parsed search results 
            if successful. Returns a tuple with an error message string and the 
            exception object if an error occurs.
    """

    try:
        # Execute the search request requesting up to 5 results 
        response = client.search(
            query=query,
            search_depth=search_depth,
            max_results=5
        )

        # Initialize an empty list to store the parsed results
        results = []

        # Iterate through the returned results and format them into dictionaries
        for i, result in enumerate(response.get("results", []), 1):

            title = result.get('title')
            url = result.get('url')
            content = result.get('content')

            # Append the extracted fields to the results list with a numbered key
            results.append({'result n°'+str(i):{
                'title':title,
                'url':url,
                'content':content
            }})

        return results

    except Exception as e:
        # Catch any errors and return the error message along with the exception object
        return "An error occurred while performing the search.", e

# JSON schema definition for the LLM to understand how to call this tool
web_search_schema = {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information about the submitted request. Return 5 different results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The user's query. For example: When was Lionel Messi born?"
                    },
                    "search_depth": {
                        "type": "string",
                        "enum": ['basic', 'advanced']
                    }
                },
                "required": ["query", "search_depth"]
            }
        }
    }


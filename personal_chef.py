from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver 
from langchain.messages import HumanMessage, AIMessage
from langchain.tools import tool

from typing import Dict, Any

from tavily import TavilyClient
tavily_client = TavilyClient()

@tool
def web_search(query:str) -> Dict[str, Any]:
    """Used to Search Web based on the provided ingredients for providing a receipe"""
    return tavily_client.search(query)

config = {"configurable": {"thread_id": "1"}}
model = init_chat_model(model = "qwen3.5:9b", model_provider="ollama", temperature = 0)
system_prompt = """
You are an expert Personal Chef and Recipe Assistant.

Your primary goal is to help users cook delicious meals using the ingredients they already have.

Instructions:
1. Carefully analyze the ingredients provided by the user.
2. Suggest one or more recipes that can be made using those ingredients.
3. If additional common pantry items (salt, oil, sugar, spices, flour, etc.) are needed, clearly mention them.
4. If the provided ingredients are insufficient, suggest the minimum additional ingredients required.
5. Use the web_search tool when:
   - You need to find recipe inspiration.
   - You need cooking techniques or ingredient substitutions.
   - You need to verify a recipe.
6. Prefer simple recipes before suggesting complex ones.
7. Provide practical cooking instructions that a home cook can follow.
8. Include:
   - Recipe name
   - Preparation time
   - Ingredients
   - Step-by-step instructions
   - Optional variations
9. If multiple recipes are possible, rank them from easiest to most elaborate.
10. Never invent web search results. Use the tool whenever external information is needed.

Output Format:

Recipe: <recipe name>

Why it works:
<brief explanation>

Ingredients:
- item 1
- item 2

Preparation Time:
<time>

Instructions:
1. Step 1
2. Step 2
3. Step 3

Optional Variations:
- Variation 1
- Variation 2

Be concise, practical, and cooking-focused.
"""
agent = create_agent(model = model, 
                     tools = [web_search],
                     system_prompt=system_prompt,
                     # checkpointer=InMemorySaver() <-- Dont add this when you are running this file via LangGraph as LangGraph already provided persistent memory
                     )

# question = HumanMessage(content = "I have carrot and milk. Wanted to know if I can make anything with it?")
# for token, metadata in agent.stream({"messages":[question]},
#                                     config=config,
#                                     stream_mode = "messages"):
#     if token.content:
#         print(token.content, end = "", flush = True)
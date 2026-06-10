# Personal Chef AI Agent 🍳

An AI-powered Personal Chef built using LangGraph, LangChain, Ollama, and Tavily Search.

The agent analyzes ingredients provided by the user and recommends recipes that can be prepared with minimal additional ingredients. When necessary, it performs web searches to discover recipe ideas, cooking techniques, and ingredient substitutions before generating structured cooking instructions.

## Features

* Ingredient-based recipe generation
* AI Agent powered by LangGraph
* Tool-calling with Tavily Search
* Local LLM inference using Ollama (Qwen 3.5 9B)
* Structured recipe responses
* Extensible architecture for adding nutrition analysis, meal planning, and grocery recommendations
* Compatible with LangGraph Studio for agent visualization and debugging

## Tech Stack

* LangGraph
* LangChain
* Ollama
* Qwen 3.5 9B
* Tavily Search API
* Python

## Example

**User Input**

> I have carrots, milk, and sugar. What can I make?

**Agent Output**

* Carrot Halwa
* Preparation time
* Ingredients
* Step-by-step instructions
* Optional variations

<video src="Demo.mov" width="100%" controls></video>

This project demonstrates how to build a production-style AI agent that combines LLM reasoning with external tools to solve real-world tasks.

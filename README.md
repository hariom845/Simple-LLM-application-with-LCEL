## Converting English Text Into Any Other Language :- A Simple LLM application with LCEL
Here I am building a simple LLM application with LangChain. This application will translate text from English into another language. This is a relatively simple LLM application - it's just a single LLM call plus some prompting. Still, this is a great way to get started with LangChain - a lot of features can be built with just some prompting and an LLM call!

After these I will be able to handle the operations:- 

- Using language models

- Using PromptTemplates and OutputParsers

- Using LangChain Expression Language (LCEL) to chain components together

- Debugging and tracing your application using LangSmith

- Deploying your application with LangServe

-- We will use open source models like LLama3, Gemma2, Mistral here, for these we are taking help of GROQ Platform

# LangServe Translation App

A simple API server built with **FastAPI**, **LangChain**, and **LangServe** to provide translation functionality using the Groq `Gemma2-9b-It` model.

---

## Features

- Uses **LangChain** prompt templates to structure translation prompts.
- Uses **LangServe** to deploy runnable chains as API endpoints.
- Output parsing with **StrOutputParser**.
- Easy environment variable management using **.env**.
- FastAPI-based server with auto-generated docs at `/docs`.

---

## Requirements

- Python 3.10+
- pip packages:

- fastapi
- uvicorn
- python-dotenv
- langchain-core
- langchain-groq
1. Create a virtual environment (optional but recommended)
2. Clone the repository:langser
3. Install dependencies
4. Set up environment variables
5. Running the Server

# How It Works
1. Prompt Template: Defines a translation prompt with placeholders for text and language.
2. Model: Sends the prompt to the Groq Gemma2-9b-It model.
3. Parser: Extracts and returns the output as a string.
4. Chain: Combines prompt → model → parser and exposes it as a FastAPI route using LangServe.

# Notes
- Ensure your .env file is loaded correctly.
- Do not push your API key to GitHub; GitHub push protection may block commits containing secrets.
- Use the StrOutputParser to get a clean string output from the model.

# serve.py

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("put your key")

# Initialize LLM (Groq model)
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

# 2. Output parser
parser = StrOutputParser()

# 3. Build chain: Prompt -> Model -> Parser
chain = prompt_template | model | parser

# 4. FastAPI app definition
app = FastAPI(
    title="LangServe Translation App",
    version="1.0.0",
    description="A simple API server using LangChain + LangServe"
)

# 5. Add LangServe chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

# 6. Run server using uvicorn
# Usage: uvicorn serve:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

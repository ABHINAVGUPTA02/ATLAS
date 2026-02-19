import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        # calling the object directly as it will create the graph
        react_app = graph()

        # saving the graph
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as file:
            file.write(png_graph)

        print(f"Graph saved successfully as my_graph.png in {os.getcwd()}")

        messages={"messages": [query.query]}
        output = react_app.invoke(messages) 

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
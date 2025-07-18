from fastapi import FastAPI
from app.schemas import InputData, CompareResponse
from app.model_local import run_local_model
from app.model_gpt4mini import run_gpt4_mini
from app.comparator import compare_outputs_with_gpt4
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/compare", response_model=CompareResponse)
async def compare_models(data: InputData):
    loop = asyncio.get_event_loop()

    local_task = loop.run_in_executor(None, run_local_model, data.instruction, data.text)
    gpt_mini_task = loop.run_in_executor(None, run_gpt4_mini, data.instruction, data.text)

    local_result, gpt4mini_result = await asyncio.gather(local_task, gpt_mini_task)

    best = compare_outputs_with_gpt4(data.text, local_result, gpt4mini_result)

    return CompareResponse(
        best_result=best["best"],
        source=best["source"],
        local_result=local_result,
        gpt4mini_result=gpt4mini_result
    )

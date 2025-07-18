from pydantic import BaseModel

class InputData(BaseModel):
    instruction: str
    text: str

class CompareResponse(BaseModel):
    best_result: str
    source: str  # "local" or "gpt4mini"
    local_result: str
    gpt4mini_result: str

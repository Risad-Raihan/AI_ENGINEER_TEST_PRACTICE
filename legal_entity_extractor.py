from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(
    title="Legal Entity Extractor",
    description="Extract legal entities from text",
    version="1.0.0"
)

Legal_Entities = ["Agreement", "Contract", "Plaintiff", "Defendant", "Court", "Statute" , "Case", "Party", "Witness", "Attorney", "Judge", "Jury", "Expert", "Expert Report", "Expert Testimony", "Expert Witness", "Expert Witness Report", "Expert Witness Testimony"]

class TextInput(BaseModel):
    text: str
    
class EntityResponse(BaseModel):
    entities: List[str]

@app.post("/extract_entities", response_model=EntityResponse)
async def extract_entities(input_data: TextInput):
    """
        Extract legal entities from the input text.
        Returns a list of unique legal entities found in the text (case-insensitive).
    """
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = input_data.text.lower()
    
    found_entitities = set()
    
    for entity in Legal_Entities:
        if entity.lower() in text_lower:
            found_entitities.add(entity)
    
    return EntityResponse(entities=sorted(list(found_entitities)))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    

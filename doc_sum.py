from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import string
from collections import Counter
from typing import List

app = FastAPI(title="Document Summarizer API")

# Define the stop words
STOP_WORDS = {"the", "of", "a", "is", "in", "to", "and", "shall", "be", "this", "both"}

class DocumentRequest(BaseModel):
    document: str

class SummaryResponse(BaseModel):
    summary: List[str]

def sum_doc(text: str, top_n: int = 5) -> List[str]:
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    
    # Tokenize into words
    words = text.split()
    
    # Filter out stop words
    filtered_words = [word for word in words if word not in STOP_WORDS]
    
    # Count word frequencies
    word_counts = Counter(filtered_words)
    
    # Get top N most frequent words
    top_words = [word for word, _ in word_counts.most_common(top_n)]
    
    return top_words

@app.post("/summarize_document", response_model=SummaryResponse)
async def summarize_document_endpoint(request: DocumentRequest):
    try:
        summary = sum_doc(request.document)
        return SummaryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
    


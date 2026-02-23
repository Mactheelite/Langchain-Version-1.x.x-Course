from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from upload_document import upload_document_from_bytes, delete_document_by_filename
from rag_chain import build_rag_chain

app = FastAPI(title="RAG Cloud Upload API")


class DeleteRequest(BaseModel):
    filename: str


class QuestionRequest(BaseModel):
    question: str


@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Endpoint for uploading a PDF
    """
    try:
        contents = await file.read()
        upload_document_from_bytes(file.filename, contents)
        return JSONResponse(content={"status": "success", "filename": file.filename})
    except Exception as e:
        return JSONResponse(content={"status": "error", "detail": str(e)}, status_code=500)


@app.delete("/delete_pdf")
async def delete_pdf(request: DeleteRequest):
    """
    Endpoint for deleting a PDF from the vector database by filename
    """
    try:
        result = delete_document_by_filename(request.filename)
        if result["status"] == "not_found":
            return JSONResponse(content=result, status_code=404)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"status": "error", "detail": str(e)}, status_code=500)


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Endpoint for asking questions to the RAG system
    """
    try:
        rag_chain = build_rag_chain()
        answer = rag_chain.invoke(request.question)
        return JSONResponse(content={"question": request.question, "answer": answer})
    except Exception as e:
        return JSONResponse(content={"status": "error", "detail": str(e)}, status_code=500)
    

    # Run this on the terminal to start the API server
    # uvicorn main_rag:app --reload
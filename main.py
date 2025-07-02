import tempfile
from fastapi import FastAPI, UploadFile, File, HTTPException

from schemas import SFWResponseSchema, NSWFResponseSchema
from service import find_nsfw

app = FastAPI()

@app.post("/moderate", response_model= NSWFResponseSchema | SFWResponseSchema)
async def moderate_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail=".jpg or .png files only")

    try:
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=True) as tmp:
            tmp.write(await file.read())
            tmp.flush()

            result = find_nsfw(tmp.name)
            return result

    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI
from .schemas import PredictRequest, PredictResponse
from .model import load_model

app = FastAPI(title="ML Deploy FastAPI")

# Load model once at startup
model = load_model()


@app.get("/")
def root():
    return {"message": "ML model serving API is up!"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    preds = model.predict([req.features])
    return {"prediction": int(preds[0])}

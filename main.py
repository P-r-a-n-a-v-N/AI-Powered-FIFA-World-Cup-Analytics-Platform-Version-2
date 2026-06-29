from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import MatchQuery, MatchPrediction
from .bedrock_llm import get_match_prediction_from_stats

app = FastAPI(title="FIFA World Cup Analytics API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=MatchPrediction)
async def predict_match(query: MatchQuery):
    try:
        fake_stats = {
            "team_a": query.team_a,
            "team_b": query.team_b,
            "stage": query.stage,
            "team_a_recent_form": "WWDLW",
            "team_b_recent_form": "LDWDW",
            "team_a_worldcup_rank": 3,
            "team_b_worldcup_rank": 8,
        }
        result = get_match_prediction_from_stats(fake_stats)
        return MatchPrediction(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

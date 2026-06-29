from pydantic import BaseModel

class MatchQuery(BaseModel):
    team_a: str
    team_b: str
    stage: str | None = None

class MatchPrediction(BaseModel):
    team_a_win_prob: float
    team_b_win_prob: float
    draw_prob: float
    explanation: str

import json
from .aws_clients import bedrock

MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

PROMPT_TEMPLATE = """You are an expert football data analyst. Use the provided structured statistics to explain strengths, weaknesses, and match-up dynamics between two teams. Then provide calibrated win/draw probabilities.
Structured stats:\n{stats}\n\nReturn JSON with keys: team_a_win_prob, team_b_win_prob, draw_prob, explanation."""


def get_match_prediction_from_stats(stats: dict) -> dict:
    prompt = PROMPT_TEMPLATE.format(stats=json.dumps(stats, ensure_ascii=False))
    body = json.dumps({
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.4,
    })

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=body,
        contentType="application/json",
        accept="application/json",
    )

    payload = json.loads(response["body"].read())
    return json.loads(payload["completion"])

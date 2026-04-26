from fastapi import APIRouter, Header, HTTPException
import openai

router = APIRouter()

@router.post("/analyze")
async def analyze_data(data: dict, x_ai_key: str = Header(...)):
    try:
        openai.api_key = x_ai_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Analyze this server data: {data}"}]
        )
        return {"analysis": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
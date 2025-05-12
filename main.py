from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
import openai

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class LyricsRequest(BaseModel):
    lyrics: str

@app.post("/transliterate")
async def transliterate_lyrics(req: LyricsRequest):
    prompt = (
        "Transliterate the following Nepali lyrics to English letters (Romanized), "
        "but preserve pronunciation. Do not translate the meaning.\n\n"
        f"Lyrics: {req.lyrics}\nRomanized:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    romanized = response.choices[0].message.content.strip()
    return {"romanized": romanized}

import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

load_dotenv()

app = FastAPI(title="代码 Review 助手")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")


@app.post("/review")
async def review(payload: dict):
    code = payload.get("code", "").strip()
    language = payload.get("language", "python").strip()

    if not code:
        raise HTTPException(400, "代码不能为空")
    if language not in ("python", "javascript"):
        raise HTTPException(400, "仅支持 python 或 javascript")
    if len(code) > 20000:
        raise HTTPException(400, "代码长度不能超过 20000 字符")

    from utils.reviewer import review_code
    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, lambda: review_code(code, language))
    except ValueError as e:
        raise HTTPException(400, str(e))
    except Exception as e:
        raise HTTPException(500, f"Review 失败：{str(e)}")

    return JSONResponse(result)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)

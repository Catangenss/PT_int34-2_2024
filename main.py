from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/healthz", response_class=PlainTextResponse)
async def health_check():
    return "200 OK"

# Подключение папки static для обслуживания статических файлов
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

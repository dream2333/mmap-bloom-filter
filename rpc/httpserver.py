import uvicorn
from fastapi import FastAPI,WebSocket


app = FastAPI( debug=False)
@app.get("/")
def read_root():
    return True

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

if __name__ == '__main__':
    uvicorn.run("httpserver:app", host="127.0.0.1", port=8000, workers=1)

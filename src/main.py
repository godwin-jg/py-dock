from fastapi import FastAPI
import redis
app = FastAPI()

r = redis.Redis(host="redis",port=6379)

@app.get("/")
async def root():
    return {"message": "Hello MYY"}

@app.get("/hits")
async def root():
    r.incr("hits")
    return {"Hello": r.get("hits")}
from fastapi import FastAPI

app = FastAPI(
    title="AHR Auth",
    version="1.0.0",
    description="Authentication & Identity Service"
)


@app.get("/")
def root():
    return {
        "service": "ahr-auth",
        "status": "running"
    }
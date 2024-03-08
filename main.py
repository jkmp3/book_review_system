from app.config.config import engine
from app.dependencies import app
from app.models import models

models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

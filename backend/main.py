from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.users import User
from models.games import Games
import uvicorn
import database
# Router
from core.users import router as users_router
from core.games import router as games_router
from core.rawg import router as rawg_router
from core.authentication import router as auth_router

database.db.connect()
database.db.create_tables([User, Games])
database.db.close()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(games_router)
app.include_router(rawg_router)
app.include_router(auth_router)    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True, reload=True)
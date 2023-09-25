from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from models.games import Games, GameBaseSchema, GameCreateSchema, StatusChoices, GameRetrieveSchema
from .authentication import get_current_user
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("/", description="List of games added to play")
async def list_games(user: Annotated[dict, Depends(get_current_user)], db: Session = Depends(get_db)) -> list[GameRetrieveSchema]:
    games = db.query(Games).where(Games.owner_id==user['id'])
    return games

@router.post("/")
async def add_game(game: GameCreateSchema, user: Annotated[dict, Depends(get_current_user)], db: Session = Depends(get_db)) -> GameBaseSchema:
    db_game = Games(
        title=game.title,
        photo=game.photo,
        added_on=datetime.now(),
        buyed=False,
        owner_id=user['id'],
        status=StatusChoices.NOT_STARTED.value
    )
    db_game.save(db)
    return db_game

@router.delete("/{game_id}")
async def delete_game(game_id: int, user: Annotated[dict, Depends(get_current_user)], db: Session = Depends(get_db)) -> dict:
    game = db.query(Games).filter(Games.id == game_id).one_or_none()
    if game:
        db.delete(game)
        db.commit()
        return {"detail": "Game deleted"}
    raise HTTPException(status_code=404, detail="Game not found")
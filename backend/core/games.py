from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Request
from datetime import datetime
from models.games import Games, ListGameBaseSchema, GameBaseSchema, GameCreateSchema
from .authentication import get_current_user

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("/", response_model=ListGameBaseSchema, description="List of games added to play")
async def list_games(request: Request, user: Annotated[dict, Depends(get_current_user)]) -> ListGameBaseSchema:
    games = Games.select().where(Games.owner==user['id']).dicts()
    game_list = [GameBaseSchema(**game) for game in games]
    return ListGameBaseSchema(games=game_list)

@router.post("/")
async def add_game(request: Request, game: GameCreateSchema, user: Annotated[dict, Depends(get_current_user)]) -> GameBaseSchema:
    db_game = Games(
        title=game.title,
        photo=game.photo,
        added_on=datetime.now(),
        buyed=False,
        owner=user['id'],
        status=1
    )
    db_game.save()
    return GameBaseSchema(**db_game.to_dict())

@router.delete("/{game_id}")
async def delete_game(game_id: int, user: Annotated[dict, Depends(get_current_user)]) -> dict:
    game = Games.delete_by_id(game_id)
    if game:
        return {"detail": "Game deleted"}
    raise HTTPException(status_code=404, detail="Game not found")
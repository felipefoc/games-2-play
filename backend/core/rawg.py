
from fastapi import APIRouter, Header
from interface.rawg import Rawg

router = APIRouter(
    prefix="/rawg",
    tags=["external api's"]
)

@router.get("/{game_name}")
async def get_game_by_name(game_name):
    return Rawg().get_games(game_name)

@router.get("/game/{game_id}")
async def get_game_by_id(game_id):
    return Rawg().get_game(game_id)
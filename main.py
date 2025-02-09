import modal
import json
from fastapi import FastAPI


app = FastAPI()


def load_json_leaderboard():
    volume = modal.Volume.from_name("face-database")
    metadata = volume.read_file("metadata.json")
    db = list(metadata)[0]
    leaderboard = json.loads(db)
    return leaderboard


@app.get("/leaderboard")
async def get_leaderboard():
    return load_json_leaderboard()

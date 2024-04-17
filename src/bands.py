from src.generic import generate_uuid
from typing import List

class Band:
    def __init__(self, name: str, members: List[str]=None, genre: str=None, location_id: int=None, socials: List[str]=None):
        self.id = generate_uuid(),
        self.name = name
        self.members = members
        self.genre = genre
        self.location_id = location_id
        self.socials = socials
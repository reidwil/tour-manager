from src.generic import generate_uuid
from typing import List

import json

from dataclasses import dataclass


@dataclass
class Socials:
    instagram: str = None
    tiktok: str = None
    twitter: str = None
    bandcamp: str = None
    soundcloud: str = None
    youtube: str = None
    spotify: str = None


class Band:
    def __init__(
        self,
        name: str,
        members: List[str] = None,
        genre: str = None,
        location_id: int = None,
        socials: Socials = None,
    ):
        self.id = (generate_uuid(),)
        self.name = name
        self.members = members
        self.genre = genre
        self.location_id = location_id
        self.socials = socials

    def make_socials_dict(self):
        return json.dumps(self.socials.__dict__)

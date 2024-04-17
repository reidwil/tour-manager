from typing import List
from enum import Enum

from src.generic import generate_uuid

class TourStatus(Enum):
    PLANNING = "planning"
    ON_TOUR = "on_tour"
    FINISHED = "finished"

class Booking:
    def __init__(self, location_id: int, play_date: str, booking_date: str):
        self.location_id = location_id
        self.play_date = play_date
        self.booking_date = booking_date
        self.id = generate_uuid()

class Tour:
    def __init__(self, band_id: int, status: TourStatus, start_date: str, end_date: str, cities: List[str], bookings: List[Booking]):
        self.id = generate_uuid()
        self.band_id = band_id
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.cities = cities
        self.bookings = bookings



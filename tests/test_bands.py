from src.bands import Band


def test_bands():
    underoath = Band("underoath", genre="metal", location_id=15)
    fallout_boy = Band("fallout_boy", genre="metal", location_id=4)
    sixteenth_to_harlem = Band("sth", genre="ska", location_id=2)

    assert underoath.location_id == 15, "Underoath is not of location 15"
    assert fallout_boy.id is not None, "Fallout boy id is none!"
    assert sixteenth_to_harlem.genre != fallout_boy.genre, "Genre assertions failed"


if __name__ == "__main__":
    print("========================= STARTING TESTS =========================")
    print("\n\n\n")
    test_bands()

    print("========================= TEST PASSED =========================")

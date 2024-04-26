from flask import Flask, request, render_template_string, redirect, url_for, session
from src.bands import Band, Socials
from src.generic import format_social_media_links
from forms.intake import form_html as intake_form_html
from forms.landing_page import form_html as band_landing_html
from forms.route_tour import form_html as route_tour_html
from forms.browse_bands import form_html as browse_bands_html
from src.metros import load_metros
import csv
import json
import os
from dotenv import load_dotenv


app = Flask(__name__)
app.secret_key = "DEV"  # Needed for session management

load_dotenv()


@app.route("/")
def form():
    metros = load_metros()
    return render_template_string(intake_form_html, metros=metros)


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    members = (
        request.form.get("members").split(",") if request.form.get("members") else []
    )
    genre = request.form.get("genre")
    location_id = (
        int(request.form.get("location_id"))
        if request.form.get("location_id")
        else None
    )
    socials = Socials()
    socials.instagram = request.form.get("socials[instagram]")
    socials.tiktok = request.form.get("socials[tiktok]")
    socials.twitter = request.form.get("socials[twitter]")
    socials.bandcamp = request.form.get("socials[bandcamp]")
    socials.soundcloud = request.form.get("socials[soundcloud]")
    socials.youtube = request.form.get("socials[youtube]")
    socials.spotify = request.form.get("socials[spotify]")

    band = Band(name, members, genre, location_id, socials)

    # Writing to CSV file
    with open("db/bands.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                band.id,
                band.name,
                ", ".join(band.members),
                band.genre,
                band.location_id,
                band.make_socials_dict(),
            ]
        )

    # Store band details in session to retrieve later
    session["last_band"] = band.__dict__

    return redirect(url_for("band_created"))


@app.route("/landing-page")
def band_created():
    band = session.get("last_band", None)
    if not band:
        return redirect(url_for("form"))
    return render_template_string(band_landing_html, band=band)


@app.route("/browse-bands")
def browse_bands():
    bands = []
    try:
        with open("db/bands.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                socials_str = row[5] if len(row) > 5 else "{}"
                try:
                    socials = json.loads(socials_str)
                except json.JSONDecodeError:
                    socials = {}
                formatted_socials = format_social_media_links(socials)
                if row:  # make sure it's not an empty row
                    band = {
                        "id": row[0],
                        "name": row[1],
                        "members": row[2],
                        "genre": row[3],
                        "location_id": row[4],
                        "socials": formatted_socials,
                    }
                    bands.append(band)
    except FileNotFoundError:
        print("File not found. Make sure you have bands.csv in the db directory.")
    return render_template_string(browse_bands_html, bands=bands)


@app.route("/route-tour")
def route_tour():
    center_lat, center_lng = 39.8283, -98.5795
    zoom = 4
    map_type = "roadmap"
    api_key = os.environ.get("GOOGLE_API_KEY")
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={center_lat},{center_lng}&zoom={zoom}&size=600x300&maptype={map_type}&key={api_key}"
    return render_template_string(route_tour_html, map_url=map_url)


if __name__ == "__main__":
    app.run(debug=True)

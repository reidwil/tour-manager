from flask import Flask, request, render_template_string
from src.bands import Band
from forms.intake import form_html as intake_form_html
from src.metros import load_metros
import csv


app = Flask(__name__)

@app.route('/')
def form():
    metros = load_metros()
    return render_template_string(intake_form_html, metros=metros)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    members = request.form.get('members').split(',') if request.form.get('members') else []
    genre = request.form.get('genre')
    location_id = int(request.form.get('location_id')) if request.form.get('location_id') else None
    socials = request.form.get('socials').split(',') if request.form.get('socials') else []
    
    band = Band(name, members, genre, location_id, socials)
    
    # Writing to CSV file
    with open('db/bands.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([band.id, band.name, ', '.join(band.members), band.genre, band.location_id, ', '.join(band.socials)])
    
    print("New Band Created:")
    print(f"ID: {band.id}")
    print(f"Name: {band.name}")
    print(f"Members: {band.members}")
    print(f"Genre: {band.genre}")
    print(f"Location ID: {band.location_id}")
    print(f"Social Media Links: {band.socials}")
    
    return f"Band {band.name} created successfully!"

if __name__ == '__main__':
    app.run(debug=True)

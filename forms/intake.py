form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Band Submission Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"> <!-- Font Awesome for icons -->
    <style>
        body {
            background-color: #333; /* Dark background */
            color: #fff; /* Light text */
        }
        .container {
            padding-top: 20px;
        }
        .form-group {
            background-color: #555; /* Lighter boxes for inputs */
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        label {
            color: #ccc; /* Light grey label text */
        }
        .form-control {
            background-color: #777; /* Even lighter background for inputs */
            border: 1px solid #888;
            color: #fff; /* White text for input */
        }
        .btn-primary {
            background-color: #0062cc; /* Bootstrap primary blue */
            border-color: #005cbf;
        }
        .btn-primary:hover {
            background-color: #0056b3;
            border-color: #004a99;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Band Submission Form</h2>
        <form action="/submit" method="post">
            <div class="form-group">
                <label for="name">Band Name:</label>
                <input type="text" class="form-control" id="name" name="name">
            </div>
            <div class="form-group">
                <label for="members">Members (comma-separated):</label>
                <input type="text" class="form-control" id="members" name="members">
            </div>
            <div class="form-group">
                <label for="genre">Genre:</label>
                <input type="text" class="form-control" id="genre" name="genre">
            </div>
            <div class="form-group">
                <label for="location_id">Location (Major Metro):</label>
                <select class="form-control" id="location_id" name="location_id">
                    {% for id, name in metros %}
                    <option value="{{ id }}">{{ name }}</option>
                    {% endfor %}
                </select>
            </div>
            <!-- Social Media Links Section with icons -->
            <div class="form-group">
                <label><i class="fab fa-instagram icon"></i>Instagram:</label>
                <input type="text" class="form-control" name="socials[instagram]">
            </div>
            <div class="form-group">
                <label><i class="fab fa-tiktok icon"></i>TikTok:</label>
                <input type="text" class="form-control" name="socials[tiktok]">
            </div>
            <div class="form-group">
                <label><i class="fab fa-twitter icon"></i>Twitter:</label>
                <input type="text" class="form-control" name="socials[twitter]">
            </div>
            <div class="form-group">
                <label><i class="fab fa-bandcamp icon"></i>Bandcamp:</label>
                <input type="text" class="form-control" name="socials[bandcamp]">
            </div>
            <div class="form-group">
                <label><i class="fab fa-soundcloud icon"></i>SoundCloud:</label>
                <input type="text" class="form-control" name="socials[soundcloud]">
            </div>
            <div class="form-group">
                <label><i class="fab fa-youtube icon"></i>YouTube:</label>
                <input type="text" class="form-control" name="socials[youtube]">
            </div>
            <div class="form-group">
                <label><i class="fab fa-spotify icon"></i>Spotify:</label>
                <input type="text" class="form-control" name="socials[spotify]">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
"""

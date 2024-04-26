form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Band Created</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
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
        <h2>Welcome {{ band.name }}!</h2>
        <div class="form-group">
            <label>Name:</label>
            <p class="form-control">{{ band.name }}</p>
        </div>
        <div class="form-group">
            <label>Members:</label>
            <p class="form-control">{{ band.members | join(', ') }}</p>
        </div>
        <div class="form-group">
            <label>Genre:</label>
            <p class="form-control">{{ band.genre }}</p>
        </div>
        <div class="form-group">
            <label>Location ID:</label>
            <p class="form-control">{{ band.location_id }}</p>
        </div>
        <div class="form-group">
            <label>Social Media Links:</label>
            <p class="form-control">{{ band.socials | join(', ') }}</p>
        </div>
        <a href="/" class="btn btn-primary">Create Another Band</a>
        <a href="/route-tour" class="btn btn-primary">Route Tour</a>
        <a href="/browse-bands" class="btn btn-primary">Browse Bands</a>
    </div>
</body>
</html>
"""

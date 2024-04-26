form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Browse Bands</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            padding-top: 20px;
        }
        .band-container {
            background-color: #fff;
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
    <a href="/landing-page" class="btn btn-primary">Back to Band Details</a>
        <h1>Browse Bands</h1>
        {% for band in bands %}
        <div class="band-container">
            <h2>{{ band.name }}</h2>
            <p>Members: {{ band.members }}</p>
            <p>Genre: {{ band.genre }}</p>
            <p>Location ID: {{ band.location_id }}</p>
        <div>
            <strong>Social Media Links:</strong>
            <ul>
                {% for key, details in band.socials.items() %}
                    <li>
                        <i class="{{ details.icon }}"></i> {{ key }}: 
                        <a href="{{ details.url }}" target="_blank">{{ details.url }}</a>
                    </li>
                {% endfor %}
            </ul>
        </div>
        </div>
        {% else %}
        <p>No bands found.</p>
        {% endfor %}
    </div>
</body>
</html>
"""

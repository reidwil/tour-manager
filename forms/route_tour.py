form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Route Tour</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #333;
            color: #fff;
        }
        .container {
            padding-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Route Tour Map</h2>
        <div class="button-group">
            <a href="/landing-page" class="btn btn-primary">Back to Band Details</a>
            <a href="/browse-bands" class="btn btn-primary">Browse Bands</a>
        </div>
        <img src="{{ map_url }}" alt="Google Map of the United States" class="img-fluid" style="width: 800px; height: 400px;">
    </div>
</body>
</html>
"""

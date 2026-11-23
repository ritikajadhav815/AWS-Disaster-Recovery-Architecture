
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Disaster Recovery Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            text-align: center;
            padding: 80px 20px;
        }
        .container {
            background: white;
            max-width: 650px;
            margin: auto;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 {
            color: #1e3a8a;
        }
        .status {
            color: #15803d;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Disaster Recovery Application</h1>
        <p>Welcome to our Healthcare Technology DR Project.</p>
        <p class="status">Application Status: ONLINE</p>
        <p>Region: ap-southeast-2 (Sydney)</p>
        <p>Server: DR-Primary-Web-Server</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

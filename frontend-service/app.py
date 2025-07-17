import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # The only job of this function is to render the HTML template.
    # No API calls, no environment variable checks.
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

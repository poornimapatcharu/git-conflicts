import linux
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Application Running!"

if __name__ == "__main__":
    # Get port from OS environment variable
    port = int(os.environ.get("PORT", 1000))

    app.run(host="0.0.0.0", port=port)

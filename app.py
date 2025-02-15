from flask import Flask

app = Flask(__name__)

print("New change to trigger Jenkins assignment")

@app.route('/')
def home():
    return "Hello, Jenkins CD with Flask and Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

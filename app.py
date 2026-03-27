from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Jenkins + Kubernetes 🚀"

@app.route("/app")
def app_page():
    return "Hi Sankuri its app page 🚀"

@app.route("/menu")
def menu_page():
    return "This is Menu 🚀"

@app.route("/test")
def test_page():
    return "This is Test 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
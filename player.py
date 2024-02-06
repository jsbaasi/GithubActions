from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    print("Vulnerability")

app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)
import os
import json

jsonFile = open("myWebsites.json", "rw");
data = json.load(jsonFile);

print data["links_1"][0]["url"];

@app.route("/")
def homepage():
	return render_template('index.html', links_1=data["links_1"])

if __name__ == "__main__":
	app.run(debug=True)
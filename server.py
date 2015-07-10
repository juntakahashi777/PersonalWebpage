from flask import *
app = Flask(__name__)
import os
import json

@app.route("/delete")
def delete_url():
	jsonFile = open("myWebsites.json", "r");
	data = json.load(jsonFile);

	index = request.args.get('index');

	data["links_1"].pop(int(index)-1);
	jsonFile = open("myWebsites.json", "w");
	json.dump(data, jsonFile);
	jsonFile.close();

	return redirect(url_for('homepage'))

@app.route("/", methods=['GET', 'POST'])
def homepage():
	jsonFile = open("myWebsites.json", "r");
	data = json.load(jsonFile);

	if request.method == 'POST':
		new_url = request.form['url'];
		entry = {"url": new_url}
		data["links_1"].append(entry);
		with open("myWebsites.json", mode='w') as jsonFile:
			json.dump(data, jsonFile);
	
	jsonFile.close();
	return render_template('index.html', links_1=data["links_1"]);


if __name__ == "__main__":
	app.run(debug=True)
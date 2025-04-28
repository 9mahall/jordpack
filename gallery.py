from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def gallery():
	images = os.listdir('static/screenshots')
	out=[]
	for img in images:
		if img.lower().endswith(('png','jpg','jpeg','gif')):
			imgurl = url_for('static',filename=f'screenshots/{img}')
			out.append(imgurl)
	return render_template('gallary.html',out=out)

if __name__ == '__main__':
	app.run(debug=True)
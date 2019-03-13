from flask import Flask, render_template as render

app = Flask(__name__, static_folder="public", template_folder="views")

@app.route('/')
def index():
	return render("index.html")

if __name__ == "__main__":
	app.run(port=8000, debug=True)

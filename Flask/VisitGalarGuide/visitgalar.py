from flask import Flask, render_template
app = Flask(__name__)

static_url_path = '/static'
static_folder = 'static' 
template_folder = '/templates'


@app.route("/")
def index():

    title = "Visitor's Guide + Flask"
    return render_template('index.html', title=title)


if __name__ == "__main__":
    app.run(debug=True)

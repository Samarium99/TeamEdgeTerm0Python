from flask import Flask, render_template

app = Flask(__name__)
# # connects html to css
static_url_path = '/static'  # URL prefix for static files
static_folder = 'static'  # Path to your static folder (e.g., CSS)
template_folder = '/templates'  # Path to your HTML templates folder


@app.route("/")  #define routes, urls to specific functions
def index():
    #You can pass data to the template here
    title = "My Flask App"
    return render_template('index.html', title=title)


#Add similar routes for other HTML pages (e.g., about.html, contact.html)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/aboutme")

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
# # connects html to css
static_url_path = '/static'  # URL prefix for static files
static_folder = 'static'  # Path to your static folder (e.g., CSS)
template_folder = '/templates'  # Path to your HTML templates folder called "templates"


@app.route("/")  #define routes, urls to specific functions
def index():
    #You can pass data to the template here
    title = "| Sarah Mo | 2024-2025 Portfolio |"
    return render_template('index.html', title=title)

@app.route("/myprojects.html")
def myprojects():
    return render_template('myprojects.html')

@app.route("/contactme.html")
def contactme():
    return render_template('contactme.html')

@app.route("/contactmesubmitted.html", methods=["POST"])
def contactmesubmitted():
    # request.form[] holds the id from the form
    # the value from the form turned into a variable
    users_name = request.form['name'].strip().title()
    email = request.form['email'].strip()
    esubject = request.form['subject']
    emessage = request.form['emessage']

    store_user(users_name, email, esubject, emessage) # a separate function
    
    # print(name)
    return render_template('contactmesubmitted.html', 
                           users_name=users_name, email=email, esubject=esubject, emessage=emessage)
# https://developers.google.com/gmail/api/quickstart/python
#(google api)



# @app.route("/post_user", methods=['POST'])
# def post_user():
#     name = request.form('name-input')
#     email = request.form('email-input')
#     phone = request.form('phone-input')
#     password = request.form('pw-input')
    
#     store_user(name, email, phone, password) # a separate function

#     return render_template('post_user.html', name=name, email=email, phone=phone, password=password)












def store_user(users_name, email, esubject, emessage):
    conn = sqlite3.connect('./static/data/myapp.db')
    curs = conn.cursor()
    #(COMMENTED OUT BECAUSE NOT APPLICABLE FOR CURRENT SITUATION)
    # # Check if email exists
    # curs.execute("SELECT EXISTS(SELECT 1 FROM users WHERE email = ?)", (email,))
    # exists = curs.fetchone()[0]

    # if exists:
    #     # Handle duplicate email (e.g., raise an error or update existing record)
    #     print("Email already exists")
    # else:
    curs.execute("INSERT INTO users (users_name, email, esubject, emessage) VALUES((?),(?),(?),(?))",(users_name, email, esubject, emessage))

    conn.commit()
    conn.close()


# def get_all_users():
#     conn = sqlite3.connect('./static/data/activity_tracker.db')
#     curs = conn.cursor()
#     all_users = [] # will store them in a list
#     rows = curs.execute("SELECT * from users")  # returns as a list 

#     for row in rows:# loop through all the rows.
#         user = {'name' : row[0], 
#                 'email': row[1],
#                 'phone': row[2],
#                 }
#         all_users.append(user) # each user gets added as a dict.

#     conn.close()  # no commit() when just reading data
#     return all_users


if __name__ == "__main__":
    app.run(debug=True)

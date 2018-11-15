from flask import Flask
from flask import render_template, request, redirect, url_for
from database import *


app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_profile(id):
	cat= get_cat_by_id(id)
	return render_template("cat.html", cat=cat)

@app.route('/create', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['firstname']
        


        create_cat(name)        
        return redirect(url_for('catbook_home'))





if __name__ == '__main__':
   app.run(debug = True)

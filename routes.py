from flask import *
from functools import wraps
import sqlite3
import hashlib

app = Flask(__name__)

app.secret_key = ('abc')

DATABASE = '/home/Aussiroth/mysite/nica.db'
#DATABASE = 'nica.db'

app.config.from_object(__name__)


app.config.update(
	DEBUG=True,
)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
  @wraps(test)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return test(*args, **kwargs)
    else:
      flash('You need to login first.')
      return redirect(url_for('login'))
  return wrap

#view functions

@app.route('/')
def index():
    g.db = connect_db()
    cur = g.db.execute('SELECT * from stores')
    stores = [dict(email=row[0],sid=row[1],address=row[2].split("%"),name=row[3],hours=row[4].split("%"),examples=row[5],description=row[6],contact=row[7].split("%"),pictures=row[8],good=row[9],diabetes=row[10],hbp=row[11], repeat = (len((row[2]).split("%")))) for row in cur.fetchall()]
    g.db.close()
    return render_template('home.html', stores=stores)

@app.route('/browse', methods=['GET', 'POST'])
def browse():
    g.db = connect_db()
    cur = g.db.execute('SELECT * from stores')
    stores = [dict(email=row[0],sid=row[1],address=row[2].split("%"),name=row[3],hours=row[4].split("%"),examples=row[5],description=row[6],contact=row[7].split("%"),pictures=row[8],good=row[9],diabetes=row[10],hbp=row[11], repeat = (len((row[2]).split("%")))) for row in cur.fetchall()]
    g.db.close()
    return render_template('browse.html', stores=stores)

@app.route('/about', methods=['GET', 'POST'])
def about():
    g.db = connect_db()
    cur = g.db.execute('SELECT * from stores')
    stores = [dict(email=row[0],sid=row[1],address=row[2].split("%"),name=row[3],hours=row[4].split("%"),examples=row[5],description=row[6],contact=row[7].split("%"),pictures=row[8],good=row[9],diabetes=row[10],hbp=row[11], repeat = (len((row[2]).split("%")))) for row in cur.fetchall()]
    g.db.close()
    return render_template('about.html', stores=stores)


#login/logout/create user functions
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		g.db = connect_db()
		cur = g.db.execute('select username, password from users')
		users = [[row[0], row[1]] for row in cur.fetchall()]
		found = False
		curruser = request.form['username']
		currpass = request.form['password']
		for user in users:
			if user[0]==curruser:
				found = True
				hash = hashlib.sha1()
				hash.update(currpass)
				if user[1]==hash.hexdigest():
					session['logged_in'] = curruser
				else:
					error = "You entered the wrong password."
		if not found:
			error = "You entered a wrong username."
	return redirect(url_for('profile'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('profile'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    error = []
    if request.method == 'POST':
        g.db = connect_db()
        curruser = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        correct = True
        #VALIDATE IF BOTH PASSWORDS ENTERED MATCH
        if password1 != password2:
            error.append("The passwords you entered are not the same! Please reenter.")
            password1 = ""
            correct = False
        #VALIDATE IF USERNAME ALREADY USED
        cur = g.db.execute('select username from users')
        users = [row[0] for row in cur.fetchall()]
        if curruser in users:
            error.append("The username is already taken. Please choose another one.")
            curruser = ""
            correct = False
        if correct==True:
            session['logged_in'] = curruser
            hash = hashlib.sha1()
            hash.update(password1)
            g.db.execute('insert into users (username, password) values (?, ?)', [curruser, hash.hexdigest()])
            g.db.commit()
    return redirect(url_for('profile'))


############
############
############
#     PROFILE   STUFF      #
############
############

@app.route('/profile')
def profile():
    g.db = connect_db()
    cur = g.db.execute('SELECT * from stores')
    stores = [dict(email=row[0],sid=row[1],address=row[2].split("%"),name=row[3],hours=row[4].split("%"),examples=row[5],description=row[6],contact=row[7].split("%"),pictures=row[8],good=row[9],diabetes=row[10],hbp=row[11], repeat = (len((row[2]).split("%")))) for row in cur.fetchall()]
    if 'logged_in' in session:
        curruser = session['logged_in']
        try:
            cur = g.db.execute("SELECT health1, health2, health3 FROM health WHERE username='"+curruser+"'")
            health = [[row[0], row[1], row[2]] for row in cur.fetchall()]
            health = health[0]
            g.db.close()
            return render_template('profile.html', health1=health[0], health2=health[1], health3=health[2], stores=stores)
        except:
            g.db.close()
            return render_template('profile.html', stores=stores)
    else:
        g.db.close()
        return render_template('profile.html', stores=stores)

@app.route('/health', methods = ['GET', 'POST'])
def health():
	condition=[]
	curruser = session['logged_in']
	if request.method=='POST':
		try:
			test = request.form['checkbox1']
			condition.append(True)
		except:
			condition.append(False)
		try:
			test = request.form['checkbox2']
			condition.append(True)
		except:
			condition.append(False)
		try:
			test = request.form['checkbox3']
			condition.append(True)
		except:
			condition.append(False)
		g.db = connect_db()
		cur = g.db.execute('select username from health')
		users = [row[0] for row in cur.fetchall()]
		if curruser in users:
			g.db.execute('update health set health1=(?) where username="'+curruser+'"', [condition[0]])
			g.db.execute('update health set health2=(?) where username="'+curruser+'"', [condition[1]])
			g.db.execute('update health set health3=(?) where username="'+curruser+'"', [condition[2]])
		else:
			g.db.execute('insert into health (username, health1, health2, health3) values (?, ?, ?, ?)', [curruser, condition[0], condition[1], condition[2]])
		g.db.commit()
	return redirect(url_for('profile'))
'''
@app.route('/changeuser', methods = ['GET', 'POST'])
@login_required
def changeuser():
	error = ""
	if request.method == "POST":
		logged_user = session['logged_in']
		g.db = connect_db()
		curruser = request.form['username']
		#validate if username empty
		correct = True
		if curruser == "":
			error = "You did not enter any username!"
			correct = False
		else:
		#VALIDATE IF USERNAME ALREADY USED
			g.db = connect_db()
			cur = g.db.execute('select username from users')
			users = [row[0] for row in cur.fetchall()]
			if curruser in users:
				error = "The username is already taken. Please choose another one."
				curruser = ""
				correct = False
		if correct:
			g.db.execute('update users set username="'+curruser+'" where username="'+logged_user+'"')
			g.db.execute('update orders set name="'+curruser+'" where name="'+logged_user+'"')
			g.db.execute('update confirm set name="'+curruser+'" where name="'+logged_user+'"')
			g.db.commit()
			flash("Successfully changed your username.")
			session['username'] = curruser
			return redirect(url_for('profile'))
	return render_template('changeuser.html', error = error, logged = True)

@app.route('/changepass', methods = ['GET', 'POST'])
@login_required
def changepass():
    error = ""
    password1, password2 = "", ""
    if request.method == "POST":
        logged_user = session['logged_in']
        g.db = connect_db()
        currpass = request.form['currpass']
        password1 = request.form['password1']
        password2 = request.form['password2']
        #validate if any is empty
        correct = True
        if currpass == "":
            error = "You did not enter your current password!"
            correct = False
        elif password1 =="" or password2 == "":
            error = "You did not enter any info for your passwords"
            correct = False
        elif password1 != password2:
            error = "You did not re-type your password correctly."
            correct = False
        else:
        #VALIDATE IF PASSWORD IS CORRECT
            hash1 = hashlib.sha1()
            hash1.update(currpass)
            g.db = connect_db()
            cur = g.db.execute('select username, password from users')
            users = [[row[0], row[1]] for row in cur.fetchall()]
            for user in users:
                if user[0]==logged_user:
                    if user[1]!=hash1.hexdigest():
                        error = "You did not type your current password correctly. Please try again."
                        correct = False
        if correct:
            hash2 = hashlib.sha1()
            hash2.update(password1)
            g.db.execute('update users set password="'+hash2.hexdigest()+'" where password="'+hash1.hexdigest()+'"')
            g.db.commit()
            flash("Successfully changed your password.")
            return redirect(url_for('profile'))
    return render_template('changepass.html', error = error, logged = True, password1=password1)
'''


if __name__ == '__main__':
    app.run(debug=True)

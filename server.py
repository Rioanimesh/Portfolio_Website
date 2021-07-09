from flask import Flask, request, render_template, redirect, url_for, session, abort
from model import mydb, cursor, add, check, add_work, show_todos, delete_todo

app = Flask(__name__)

app.secret_key='anirio'

@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template('home.html')
    

@app.route('/login',methods=['POST','GET'])
def login():
	msg=''
	if request.method=='POST':
		user=request.form['username']
		password=request.form['password']
		session['name']=user
		if check(user,password):
			msg='You are successfully login !!'
			return redirect(url_for('todo'))
		else:
			msg='Invalid username or password'
			session.pop('name',None)
				

	return render_template('login_page.html',msg=msg)


@app.route('/new',methods=['POST','GET'])
def signup():
	msg=''
	error=False
	if 'name' not in session:
		if request.method=='POST':
			fullname=request.form['name']
			emailid=request.form['emailid']
			user=request.form['username']
			password=request.form['password']
			try:
				add(user, password, emailid, fullname)
				msg='You are successfully registered !!'
				session['name']=user
				return render_template('todo.html',msg=msg)
			
			except:
				msg='username already taken....'
				error=True
	else:
		msg='You are already logged in...'	
		return render_template('todo.html',msg=msg)		
		
	return render_template('create.html', msg=msg,error=error)


@app.route('/todo',methods=['GET','POST'])
def todo(user=None):
	msg2='login'
	persion=session['name']
	todos=show_todos(persion)
	if request.method=='POST':
		# work=request.form['work']
		if request.form.get("update_btn"):
			#do update
			pass
		if request.form.get("delete_btn"):
			#do delete
			delete_btn_id=request.form['delete_btn']
			msg2=delete_todo(delete_btn_id)
			# btn_press="press"

		if request.form.get("add_work_btn"):
			work=request.form['work']

			#persion=session['name']
			work_date='2021-12-23 09:43:12'
			msg2=add_work(work,work_date,persion)
		# work=None
			
		todos=show_todos(persion)

		return render_template('todo_main.html',msg2=msg2,todos=todos)

	return render_template('todo_main.html',msg2=msg2,todos=todos)

@app.route('/logout')
def logout():
	session.pop('name',None)
	return redirect(url_for('login'))


app.run(debug=True)



import mysql.connector
mydb=mysql.connector.connect(host="localhost",
	         user="root",
	         password="animesh",
	         database="todo_project")


cursor=mydb.cursor()

def add(a,b,c,d):
	qur="insert into todo(username, user_password, emailid, fullname) values(%s,%s,%s,%s)"
	data=(a,b,c,d)
	cursor.execute(qur,data)
	mydb.commit()

def check(u,p):
	try:
		cursor.execute("select user_password from todo where username=%s",(u,))
		result=cursor.fetchone()
		if result[0] == p:
			return True
		else:
			return False	
	except:
		return False		


def add_work(work,work_date,persion):
	msg=''
	try:
		qur="insert into todo_list(details,work_date,user_id) values(%s,%s,%s)"
		data=(work,work_date,persion)
		cursor.execute(qur,data)
		mydb.commit()
		msg='work added'
	except:
		msg='work not added'
	return msg		

def show_todos(persion):
	msg3=''
	try:
		cursor.execute("select details,work_date,workid from todo_list where user_id=%s",(persion,))
		result=cursor.fetchall()
	except:
		msg='error'
		return msg3
	return result	


def delete_todo(id):
	del_id=int(id)
	msg=''
	try:
		cursor.execute("delete from todo_list where workid=%s",(del_id,))
		mydb.commit()
		msg="delete successfully!!"
		return msg
	except:
		msg='error'
		return msg


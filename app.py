from flask import Flask,render_template,request,session
import mysql.connector
conn=mysql.connector.connect(host = 'localhost',user='root',password='SKVsreekumar@370',database='taskmanagement')
newcursor=conn.cursor()

#create a flask application

app = Flask(__name__)

user_dict={'admin':'admin','sreekumarv' : '12345'}

#define the route

@app.route('/')
def hello():
    return render_template('first.html')

@app.route('/homeone')
def homeone():
    return render_template('home.html') 

#---------------------------------------HOME--------------------------------DONE
@app.route('/home')
def home():
    return render_template('first.html') 
#................................................................................





#---------------------------------------REGISTER--------------------------------DONE
@app.route('/reg')
def regi():
    return render_template('register_cpy.html') 

@app.route('/register', methods=['POST'])
def reg():
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    user_name=request.form.get('user_name')
    password=request.form.get('pass')
    query="INSERT INTO REGISTER VALUES (%s,%s,%s,%s)"
    data=(first_name,last_name,user_name,password)
    newcursor.execute(query,data)
    conn.commit() 
    return render_template('first.html') 
#..................................................................................







#----------------------------------------LOG-IN------------------------------------DONE
@app.route('/login', methods=['POST'])
def login():
    username=request.form['username']
    pwd=request.form['password']
    if username not in user_dict:
        return render_template('login.html', msg='Invalid Username')
    elif user_dict[username]!=pwd:
        return render_template('login.html', msg='Invalid Password')
    else:
        return render_template('home.html',msg="Welcome "+username)
#..................................................................................





#---------------------------------------ADD TASK--------------------------------DONE
@app.route('/add')
def add():
    return render_template('addtask.html') 

@app.route('/addtask', methods=['POST'])
def addtask():
    id=request.form.get('id')
    task_name=request.form.get('title')
    task_det=request.form.get('task_det')
    status=request.form.get('satus')
    due_date=request.form.get('due_date')
    catagory=request.form.get('catagory')
    query="INSERT INTO TASK VALUES (%s,%s,%s,%s,%s,%s)"
    data=(id,task_name,task_det,status,due_date,catagory)
    newcursor.execute(query,data)
    conn.commit() 
    return render_template('home.html') 
#..................................................................................





#------------------------------------SEARCH-------------------------------------DONE
@app.route('/search')
def search():
    return render_template('search.html')  


@app.route('/searchres',methods=['POST'])
def searchres():
    tasktitle= request.form.get('title')
    query= "SELECT * FROM TASK WHERE title LIKE '%{}%'".format(tasktitle)
    newcursor.execute(query)
    data=newcursor.fetchall()
    if not data:
       return render_template('search.html',msg="Task not found")  
    else:
       return render_template('view-task.html',sqldata=data) 
#....................................................................................





#---------------------------------------VIEW ALL--------------------------------DONE   
@app.route('/view')
def view():
    query= "SELECT * FROM TASK"
    newcursor.execute(query)
    data= newcursor.fetchall()
    return render_template('view-task.html',sqldata=data)   
#....................................................................................





#---------------------------------------update---------------------------------------COMMING-SOON
@app.route('/up')
def up():
    return render_template('update.html') 

@app.route('/update', methods=['GET'])
def update():
    id=request.form.get('id')
    task_name=request.form.get('title')
    task_det=request.form.get('task_det')
    status=request.form.get('satus')
    due_date=request.form.get('due_date')
    catagory=request.form.get('catagory')
    query = "UPDATE task SET id=%s,title=%s,task_det=%s,satus=%s,due_date=%s,catagory=%s WHERE id="+id
    data=(id,task_name,task_det,status,due_date,catagory)
    newcursor.execute(query,data)
    conn.commit() 
    return render_template('view-task.html') 

#......................................................................................





#------------------------------------------DELETE--------------------------------------DONE
@app.route('/delete', methods=["POST"])
def delete():
    id=request.form['task_id']
    query= "DELETE FROM task WHERE id="+id
    newcursor.execute(query)
    data= newcursor.fetchall()
    conn.commit() 
    return render_template('home.html',sqldata=data)
#........................................................................................





#------------------------------------FILTER-------------------------------------DONE
@app.route('/filt')
def filt():
    return render_template('filter.html')  


@app.route('/filter',methods=['POST'])
def filter():
    taskfilter= request.form.get('catagory')
    query= "SELECT * FROM TASK WHERE catagory LIKE '%{}%'".format(taskfilter)
    newcursor.execute(query)
    data=newcursor.fetchall()
    if not data:
       return render_template('filter.html',msg="Task not found")  
    else:
       return render_template('view-task.html',sqldata=data) 
#....................................................................................
    



#------------------------------------CONDACT AND ABOUT-----------------------------------
@app.route('/condact')
def condact():
    return render_template('condact.html')  

@app.route('/about')
def about():
    return render_template('about.html')  
#....................................................................................





#run the flask app

if __name__=='__main__':
    app.run(debug = True)
 
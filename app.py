from flask import Flask , request,render_template, redirect,url_for
# to start app
myapp=Flask(__name__)

@myapp.route('/')
def halloworld():
    print(request)
    print(request['name'])
    return '<h1 style="color:purple">Hello in my first flask app</h1>'


@myapp.route('/profile/<name>/<track>/<int:id>')
def profile(name,track,id):
    return f'<h1 style="color:purple">Hello in my first flask app{name}{track}{id}</h1>'

@myapp.route('/custome_response')
def custome_response():
    return '<h1>Custom Response</h1>', 201


@myapp.route('/home/<username>')
def home(username):
    return render_template("home.html",username=username)


# ###################################Error page###########################
@myapp.errorhandler(404)
def notFoundPage(error):
    return render_template("notFoundPage.html")

# ###################################return object ###########################
@myapp.route('/admin')
def admin():
    admin={
        "name":"Mohammed",
        "age":28,
        "track":"Python_Track"
    }
    return render_template("admin.html", admin=admin)

# ###################################Connect to db ###########################
from flask_sqlalchemy import SQLAlchemy

myapp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db=SQLAlchemy(myapp)


class Blog(db.Model):
    __tablename__='Blogs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email= db.Column(db.String(100),unique=True, nullable=True)
    accepted = db.Column(db.Boolean, default=True)
   

    def __str__(self):
        return f"{self.name}"

#############################################################################
# home page

@myapp.route('/index')
def index():
    blogs=Blog.query.all()
    return render_template ("index.html", blogs=blogs)

# show page
@myapp.route('/show/<int:id>')
def show(id):
    blog= Blog.query.get_or_404(id)
    return render_template("show.html", blog=blog)

# delete page
@myapp.route('/<int:id>/delete')
def delete(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("index"))

  # create 
@myapp.route('/create', methods = ['GET', 'POST'])
def create():
   if request.method == 'POST':
         p=Blog() 
         p.name=request.form['name']
         p.email=request.form['email']
         db.session.add(p)
         db.session.commit()
         return redirect(url_for('index'))
   return render_template('create.html')

# update
@myapp.route('/<int:id>/update',methods = ['GET', 'POST'])
def update(id):
     blog = Blog.query.filter_by(id=id).first()

     if request.method == "POST":

        blog.name = request.form['name']
        blog.email = request.form['email']
        db.session.commit()
        
        return redirect(url_for('index'))
     if request.method == "GET":
      return render_template('update.html', blog=blog)

# conact us
@myapp.route('/contact')
def contact():
    return render_template('contact.html')

# about us
@myapp.route('/about')
def about():
    return render_template('about.html')


# to run app
myapp.run(debug=True)
if __name__=='__main__':
    myapp.run()

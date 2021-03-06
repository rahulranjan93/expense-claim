This repo has been setup using the tutorial :

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

To setup this repo, follow the below steps:<br />
$ git clone git@github.com:rahulranjan93/expense-claim.git<br />
$ cd expense-claim<br />
$ pip3 install -r requirements.txt<br />
<br />
To start the server, follow the below steps:<br />
$ virtualenv env<br />
$ source env/bin/activate<br />
$ flask run<br />
<br />
DB connection and update:
1. For connecting to database You should have the db connection string to connect to the db. Please ask repo contributors for that.
2. To connect to db run `export DATABASE_URL=<your db connection string>` in terminal
3. To make changes in schema follow below steps : <br/>
    a. Update schema in app/models.py <br/>
    b. Run `flask db migrate` <br/>
    c. Run `flask db upgrade` <br/>
4. This will change the database schema if you are connected to database


Usage
-------
$ curl -i -X POST -H "Content-Type: application/json" -d '{"email":"rahul.ranjan@plangrid.com",
	"name":"Rahul",
	"role":"747bd65b-a83b-4657-b475-54bca59bac0a",
	"team":"Plangrid",
	"password":"rahul"
}' http://127.0.0.1:5000/create
    
    employee added successfully


$ curl -u rahul.ranjan@plangrid.com:ranjan -i -X GET http://127.0.0.1:5000/resource
    
    {
      "data": "Hello, rahul.ranjan@plangrid.com!"
    }


$ curl -u rahul.ranjan@plangrid.com:ranjan -i -X GET http://127.0.0.1:5000/token
    
    {
      "duration": 600,
      "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc"
    }
    

$ curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc:x -i -X GET http://127.0.0.1:5000/resource
    
    {
      "data": "Hello, rahul.ranjan@plangrid.com!"
    }


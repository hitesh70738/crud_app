from application import app, db
from application.models import Players, Teams
# from application.forms import TaskForm
# from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_players = Players.query.all()
    output = ""
    for player in all_players:
        output +=  player.name + " " 
    return output

 
@app.route("/add/<name>")
def add(name):
    new_player = Players(name=name)
    db.session.add(new_player)
    db.session.commit()
    #all_players = Players(name='gareth')
    #db.session.add(all_players)
    #db.session.commit()
    return "Added new player"

@app.route('/read')
def read():
    all_players = Players.query.all()
    player_string = "-->"
    for player in all_players:
        player_string += " " + player.name
    return player_string

@app.route('/update/<name>')
def update(name):
    first_player = Players.query.first()
    first_player.name = name
    db.session.commit()
    return first_player.name    

@app.route('/delete/<int:id>')
def delete(id):
    first_player = Players.query.filter_by(id=id).first()
    db.session.delete(first_player)
    db.session.commit()
    return "Deleted player"


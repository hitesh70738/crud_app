from application import db 


#class Tasks(db.Model):
#    id = db.Column(db.Integer,primary_key=True)
#    task_name = db.Column(db.String(50), nullable=False)
#    task_completion = db.Column(db.Boolean(), nullable=False, default=False) 
#    task_description = db.Column(db.String(100), nullable=False)

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Team_name = db.Column(db.String(50), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)



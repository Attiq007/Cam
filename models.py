from app import db
from sqlalchemy import Column, Float, ForeignKey, Integer, Text, text
from sqlalchemy.orm import relationship
from datetime import datetime

class Register(db.Model):
	__tablename__ = 'register'
	id = db.Column(db.Integer, primary_key=True)
	serial_no = db.Column(db.String(50), unique=True, nullable=False)
	channel_count = db.Column(db.Integer, nullable=False)
	channel1 = db.Column(db.Integer, nullable=False)
	token = db.Column(db.String(50), nullable=False)
	last_created = db.Column(db.DateTime, nullable=False)
	last_updated = db.Column(db.DateTime, nullable=False)
	name = db.Column(db.String(50), nullable=False)
	device_type = db.Column(db.Integer, nullable=False)
	mac = db.Column(db.String(50), nullable=False)
	ip = db.Column(db.String(50), nullable=False)
	hardware = db.Column(db.String(50), nullable=False)
	software = db.Column(db.String(50), nullable=False)
	algorithm = db.Column(db.String(50), nullable=False)
	snapshots = db.relationship('Snapshot', backref='register', lazy=True)

class Snapshot(db.Model):
	__tablename__ = 'snapshot'
	id = db.Column(db.String(80), primary_key=True, nullable=False, autoincrement=False)
	vasid = db.Column(db.String(50), db.ForeignKey('register.serial_no'), nullable=False)
	channel = db.Column(db.Integer, nullable=False)
	last_created = db.Column(db.DateTime, nullable=False)
	last_updated = db.Column(db.DateTime, nullable=False)
	basics = db.relationship('Basic', backref='snapshot', lazy=True)
	faces = db.relationship('Face', backref='snapshot', lazy=True)
	bodys = db.relationship('Body', backref='snapshot', lazy=True)

class Basic(db.Model):
	__tablename__ = 'basic'
	id = db.Column(db.Integer, primary_key=True)
	snap_id = db.Column(db.String(80), db.ForeignKey('snapshot.id'), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	direction = db.Column(db.Integer, nullable=False)
	face_direction = db.Column(db.Integer, nullable=False)
	face_type = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.Integer, nullable=False)
	match_score = db.Column(db.Integer, nullable=False)
	mood = db.Column(db.Integer, nullable=False)
	start_time = db.Column(db.DateTime, nullable=False)
	track_length = db.Column(db.Integer, nullable=False)
	track_type = db.Column(db.Integer, nullable=False)

class Face(db.Model):
	__tablename__ = 'face'
	id = db.Column(db.Integer, primary_key=True)
	snap_id = db.Column(db.String(80), db.ForeignKey('snapshot.id'), nullable=False)
	data = db.Column(db.Text, nullable=False)
	face_score = db.Column(db.Float, nullable=False)
	filename = db.Column(db.String(100), nullable=False)
	type = db.Column(db.Integer, nullable=False)

class Body(db.Model):
	__tablename__ = 'body'
	id = db.Column(db.Integer, primary_key=True)
	snap_id = db.Column(db.String(80), db.ForeignKey('snapshot.id'), nullable=False)
	data = db.Column(db.Text, nullable=False)
	filename = db.Column(db.String(100), nullable=False)
from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(app)

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(20), nullable=False)
    localidad = db.Column(db.String(20), nullable=False)
    
    paquete = db.relationship('Paquete', backref='paquete', cascade="all, delete-orphan")
    repartidor = db.relationship('Repartidor', backref='repartidor', cascade="all, delete-orphan")
    transporte = db.relationship('Trasporte', backref='transporte', cascade="all, delete-orphan")

        
class Paquete(db.Model):
    __tablename__="paquete"
    id=db.Column(db.Integer, primary_key=True)
    numeroenvio=db.Column(db.Integer, nullable=False)
    peso=db.Column(db.Integer, nullable=False)
    nomdestinatario=db.Column(db.String(40), nullable=False)
    dirdestinatario=db.Column(db.String(30), nullable=False)
    entregado=db.Column(db.Integer, nullable=False)
    observaciones=db.Column(db.String(200), nullable=True)
    
    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    idtransporte=db.Column(db.Integer, db.ForeignKey('transporte.id'), nullable=False)
    idrepartidor=db.Column(db.Integer, db.ForeignKey('repartidor.id'), nullable=False)
    
class Repartidor(db.Model):
    __tablename__="repartidor"
    id=db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.Integer, nullable=False)
    nombre=db.Column(db.String(40), nullable=False)
    dni=db.Column(db.Integer, nullable=False)

    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
   
class Trasporte(db.Model):
    __tablename__="transporte"
    id=db.Column(db.Integer, primary_key=True)
    numerotransporte=db.Column(db.Integer, nullable=False)
    fechahorasalida=db.Column(db.DateTime, nullable=False)
    fechahorallegada=db.Column(db.DateTime, nullable=True)

    idsucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
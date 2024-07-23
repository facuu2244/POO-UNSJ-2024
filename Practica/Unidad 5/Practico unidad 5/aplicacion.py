import random
from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Sucursal, Paquete, Trasporte

@app.route('/')
def login():
    sucu=Sucursal.query.all()#Trae todas las sucursales de la DB
    return render_template('login.html', sucursales=sucu)

@app.route('/index', methods=["POST","GET"])
def index():
    #Se asignaran valores a las variables globales
    global sucursal_seleccionada, nombre_usuario
    if request.method=="POST":#Se ejecutara solo al iniciar secion
        sucursal_seleccionada=request.form["select"]
        
        nombre_usuario=request.form["nombre"]
        return render_template('index.html', nombre=nombre_usuario, hora=datetime.now().hour, sucursal=sucursal_seleccionada)
    
    elif sucursal_seleccionada!="": #Se ejecutara en las proximas llamadas al template
        return  render_template('index.html', nombre=nombre_usuario, hora=datetime.now().hour,sucursal=sucursal_seleccionada)
    
    else:#En caso de recibir el method=GET
        return render_template('login.html')

@app.route('/recepcion_paquete', methods=["POST", "GET"])
def recepcion():
    try:
        #Se registrara un paquete en caso de cumplir las condiciones
        if request.method=="POST" and request.form["peso"] and request.form["nomdestinatario"]and request.form["dirdestinatario"]:
            global sucursal_seleccionada
            
            #Se obtiene la id de la sucursal seleccionada y genera numero de envio
            sucursal=Sucursal.query.filter_by(provincia=sucursal_seleccionada).first()
            id_sucursal=sucursal.id
            num=random.randint(1000,2000)
            
            un_paquete=Paquete(numeroenvio=num, peso=request.form["peso"], nomdestinatario=request.form["nomdestinatario"], dirdestinatario=request.form["dirdestinatario"], entregado=0, observaciones=None, idsucursal=id_sucursal, idtransporte=0, idrepartidor=0)#Se crea un objeto paquete
            
            #Luego se agrega a la DB
            db.session.add(un_paquete)
            db.session.commit()
            #Vuelve a ejecutar el template con un mensaje de confimacion
            return render_template('recepcion_paquete.html', mensaje="Correcto")
        else:#Se ejecuta en el primer llamado al tempalate ya que los campos del formulario no existen aun
            return render_template('recepcion_paquete.html')
    except:#En caso de haber algun error se notificará
        return render_template('recepcion_paquete.html', mensaje="Error")
    
@app.route('/elegir_sucursal_destino')
def sucursal_destino():
    sucu=Sucursal.query.all()
    return render_template('sucursal_destino.html', sucursales=sucu)

@app.route('/registrar_salida', methods=["POST","GET"])
def salida():
    global sucursal_dest
    try:
        #Trae la lista de paquetes seleccionados del html
        seleccionados=request.form.getlist('item')
        if request.method=="POST" and seleccionados!=[]:
            paquetes_seleccionados=[]

            for num in seleccionados:
                un_paquete=Paquete.query.filter_by(numeroenvio=num).first()
                paquetes_seleccionados.append(un_paquete)
                
            #acualiza los paquetes sin repartidor asignado
            for paquete in paquetes_seleccionados:
                paquete.idrepartidor=1
                db.session.commit()

            paquetes=Paquete.query.filter_by(entregado=0).filter_by(idrepartidor=0)
            
            #Datos para el nuevo objeto transporte
            num=random.randint(100,200)
            salida=datetime.now()
            sucursal=Sucursal.query.filter_by(provincia=sucursal_dest).first()
            id_sucursal=sucursal.id
            
            un_transporte=Trasporte(numerotransporte=num, fechahorasalida=salida, fechahorallegada=None, idsucursal=id_sucursal)
            db.session.add(un_transporte)
            db.session.commit()
            
            return render_template('registrar_salida.html', paquetes=paquetes, mensaje="Correcto")
        
        elif request.method=="POST":#Primera entrada
            paquetes=Paquete.query.filter_by(entregado=0).filter_by(idrepartidor=0)
            sucursal_dest=request.form["select"]
            return render_template('registrar_salida.html', paquetes=paquetes, mensaje="")
    except:
        paquetes=Paquete.query.filter_by(entregado=0).filter_by(idrepartidor=0)
        return render_template('registrar_salida.html', paquetes=paquetes, mensaje="Error")
    
@app.route('/registrar_llegada', methods=["POST", "GET"])
def llegada():
    global sucursal_seleccionada
    sucursal=Sucursal.query.filter_by(provincia=sucursal_seleccionada).first()
    id_sucursal_seleccionada=sucursal.id
    try:
    
        seleccionados=request.form.getlist('item')
        if request.method=="POST" and seleccionados!=[]:
            transportes_seleccionados=[]
            #Se obtienen los obejetos de tipo transporte y se agregan a la lista
            for num in seleccionados:
                un_transporte=Trasporte.query.filter_by(numerotransporte=num).first()
                transportes_seleccionados.append(un_transporte)

            #acualiza los transportes agregando la hora de llegada
            for transporte in transportes_seleccionados:

                transporte.fechahorallegada=datetime.now()
                db.session.commit()

            transportes=Trasporte.query.filter_by(fechahorallegada=None).filter_by(idsucursal=id_sucursal_seleccionada)
            
            return render_template('registrar_llegada.html', transportes=transportes, mensaje="Correcto", sucursal=sucursal_seleccionada)
        
        else:#Primera entrada
            transportes=Trasporte.query.filter_by(fechahorallegada=None).filter_by(idsucursal=id_sucursal_seleccionada)
            return render_template('registrar_llegada.html', transportes=transportes, sucursal=sucursal_seleccionada)
        
    except:
       paquetes=Paquete.query.filter_by(entregado=0).filter_by(idrepartidor=0)
       return render_template('registrar_llegada.html', transportes=transportes, mensaje="Error", sucursal=sucursal_seleccionada)
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # paquetes=Paquete.query.all()
        # for paquete in paquetes:
        #     paquete.idrepartidor=0
        #     db.session.commit()

        # transportes=Trasporte.query.all()
        # for transporte in transportes:
        #     transporte.fechahorallegada=None
        #     db.session.commit()
        
        #Definicion de variables globales
        nombre_usuario, sucursal_seleccionada, sucursal_dest="", "",""
        app.run(debug=True)
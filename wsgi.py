from flask import Flask
import datetime
hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute
fecha = datetime.datetime.now().strftime("%d/%m/%Y")
exact_hora="La hora del dia de hoy es: " + str(hora) + ":" + str(minuto) + "hrs"+" De la fecha "+ str(fecha)
application = Flask(__name__)
@application.route("/")
def hello():
    return exact_hora

if __name__ == "__main__":
    application.run()
    

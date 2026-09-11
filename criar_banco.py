from sitedois import database, app
from sitedois.models import Usuario, Foto

with app.app_context():
    database.create_all()
from flask import Flask
from app.routes.users import users_bp
from app.routes.cities import cities_bp
from app.routes.countries import countries_bp

app = Flask(__name__)

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(cities_bp, url_prefix='/cities')
app.register_blueprint(countries_bp, url_prefix='/countries')

@app.route('/')
def home():
    return {'message': 'Welcome to my Airbnb API'}

if __name__ == '__main__':
    app.run(debug=True)

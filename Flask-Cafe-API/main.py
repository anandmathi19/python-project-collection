from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random_cafe():
    random_cafe = db.session.execute(
        db.select(Cafe).order_by(db.func.random())).scalar()

    cafe_dict = {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    }
    return jsonify(cafe=cafe_dict)

@app.route("/all", methods=["GET"])
def all_cafes():

     all_cafes = db.session.execute(db.select(Cafe)).scalars().all()

     cafes_list = []
     for cafe in all_cafes:
         cafe_dict = {
             "id": cafe.id,
             "name": cafe.name,
             "map_url": cafe.map_url,
             "img_url": cafe.img_url,
             "location": cafe.location,
             "seats": cafe.seats,
             "has_toilet": cafe.has_toilet,
             "has_wifi": cafe.has_wifi,
             "has_sockets": cafe.has_sockets,
             "can_take_calls": cafe.can_take_calls,
             "coffee_price": cafe.coffee_price,
         }
         cafes_list.append(cafe_dict)
     return jsonify(cafes=cafes_list)

@app.route("/search", methods=["GET"])
def search_cafe():

    loc = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()

    if not cafes:
        return jsonify(error={"Not Found": "Sorry, no cafes at that location."})

    cafes_list = []
    for cafe in cafes:
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        cafes_list.append(cafe_dict)
    return jsonify(cafes=cafes_list)



if __name__ == '__main__':
    app.run(debug=True)

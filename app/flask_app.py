from flask import Flask, render_template
from app.models.config import Config
from app.models.models import db, Tour
from app.models.utils import get_all_tours, get_tour

web = Flask(__name__)
web.config.from_object(Config)
db.init_app(app=web)

@web.before_request
def before_request():
    db.create_all()

@web.route("/")
def index():
    tours = get_all_tours()
    return render_template(template_name_or_list="index.html", tours=tours)

@web.route("/tour/<int:id>")
def tour_details(id: int):
    tour = get_tour(id)
    render_template(template_name_or_list="tour_details.html", tour=tour)


if __name__ == "__main__":
    print("Будь ласка, Запустіть main.py")
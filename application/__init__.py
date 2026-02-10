from flask import Flask

from application.extensions import db, ma
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    from application.blueprints.customer import customer_bp
    from application.blueprints.mechanic import mechanic_bp
    from application.blueprints.service_ticket import service_ticket_bp

    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(mechanic_bp, url_prefix="/mechanics")
    app.register_blueprint(service_ticket_bp, url_prefix="/service-tickets")

    with app.app_context():
        db.create_all()

    return app

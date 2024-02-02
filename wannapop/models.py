from . import db_manager as db
from .mixins import BaseMixin, SerializableMixin
from sqlalchemy.sql import func
from flask_login import UserMixin
from datetime import datetime

class Product(BaseMixin, SerializableMixin, db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    seller_id = db.Column(db.Integer) #db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created = db.Column(db.DateTime, server_default=func.now())
    updated = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Category(BaseMixin, SerializableMixin, db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)

class User(BaseMixin, SerializableMixin, UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    role = db.Column(db.String) 
    email_token = db.Column(db.String(255), nullable=True)
    verified = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.email

class BlockedUser(BaseMixin, SerializableMixin, db.Model):
    __tablename__ = "blocked_users"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    message = db.Column(db.String(255))
    created = db.Column(db.DateTime, default=datetime.utcnow)

class BannedProduct(BaseMixin, SerializableMixin, db.Model):
    __tablename__ = 'banned_products'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    reason = db.Column(db.String(255))
    created = db.Column(db.DateTime, default=datetime.utcnow)

class Order(BaseMixin, SerializableMixin, db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    offer = db.Column(db.Numeric(precision=10, scale=2), nullable=False)  # Ajusta según necesidad
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relaciones
    product = db.relationship("Product", backref=db.backref("orders", lazy=True))
    buyer = db.relationship("User", backref=db.backref("orders", lazy=True))

class ConfirmedOrder(BaseMixin, SerializableMixin, db.Model):
    __tablename__ = "confirmed_orders"
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relación
    order = db.relationship("Order", backref=db.backref("confirmation", uselist=False, lazy=True))

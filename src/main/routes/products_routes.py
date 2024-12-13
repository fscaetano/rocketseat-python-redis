from flask import Blueprint, jsonify

products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return jsonify({"msg": "product registered"})


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    return jsonify({"msg": f"product {product_name}"})

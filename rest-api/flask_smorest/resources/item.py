import uuid

from flask import Blueprint
from flask.views import MethodView
from flask_smorest import abort

from db import items

item_bp = Blueprint('item', __name__)

class Item(MethodView):
    @item_bp.route('/item/<int:item_id>', methods=['GET'])
    def get_item(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    @item_bp.route('/item/<int:item_id>', methods=['PUT'])
    def update_item(self, item_id):
        return f"Update item with id {item_id}"

    @item_bp.route('/item/<int:item_id>', methods=['DELETE'])
    def delete_item(self, item_id):
        # Logic to delete item with item_id
        return f"Delete item with id {item_id}"


item_list_bp = Blueprint('item_list', __name__)
class ItemList(MethodView):
    @item_list_bp.route('/item', methods=['GET'])
    def get_item_list(self):
        # Logic to retrieve list of items
        return "Get item list"

    @item_list_bp.route('/item', methods=['POST'])
    def create_item(self):
        # Logic to create a new item
        return "Create item"
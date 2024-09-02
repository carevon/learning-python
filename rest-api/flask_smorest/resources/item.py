from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint('item', __name__, description="Operations on items")

@blp.route('/item/<int:item_id>')
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            item = ItemModel.query.get_or_404(item_id)
            return item
        except KeyError:
            abort(404, message="Item not found")

    @jwt_required()
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id,**item_data)

        db.session.add(item)
        db.session.commit()
        return item

    @jwt_required()
    def delete(self, item_id):
        try:
            jwt = get_jwt()
            if not jwt["is_admin"]:
                abort(403, message="Admin privilege required.")
            
            item = ItemModel.query.get_or_404(item_id)
            db.session.delete(item)
            db.session.commit()
            return {"message": "Item deleted."}
        except KeyError:
            db.session.rollback()
            abort(404, message="Item not found")


@blp.route('/item')
class ItemList(MethodView):

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        items = ItemModel.query.all()
        return items

    @jwt_required(fresh=True)
    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):

        # Validation if item already exists
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while inserting the item.")

        return item, 201
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TagModel, StoreModel
from schemas import TagSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")


@blp.route("/store/<int:store_id>/tags")
class TagsInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        stores = StoreModel.query.get_or_404(store_id)
        return stores.tags

    @blp.arguments(TagSchema)
    @blp.response(201, TagSchema)
    def post(self, tag_data, store_id):
        if TagModel.query.filter_by(name=tag_data["name"], store_id=store_id).first():
            abort(400, message="Tag already exists in that store.")
        tag = TagModel(**tag_data, store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return tag
    

@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag
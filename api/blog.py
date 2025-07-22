from flask import Blueprint,jsonify,request
from api.database_access import blogs
from .extensions import db
bp=Blueprint('blogs',__name__,url_prefix='/posts')
@bp.route('/',methods=['GET'])
def index():
   blog=blogs(db)
   result=blog.get_blogs()
   return jsonify([{"id":element.id,"title":element.title,"content":element.content,
                    "category":element.category,"tags":element.tags,"cratedAt":element.createdAt,
                    "updatedAt":element.updatedAt} for element in result])
@bp.route('/',methods=['POST'])
def add():
   data=request.get_json()
   if not data:
        return jsonify({"error": "No se proporcionó JSON"}), 400
   blog=blogs(db)
   result,id=blog.add_blog(data['title'],data['content'],data['category'],data['tags'])
   if result:
      return jsonify({"message":f"Article added successfully with id:{id}"}),201
   else:
      return jsonify({"message":"Article not added","error":id}),400
@bp.route('/<int:id>',methods=['PUT'])
def update(id):
   blog=blogs(db)
   data=request.get_json()
   result=blog.update_blog(id,data['title'],data['content'],data['category'],data['tags'])
   if result:
      return jsonify({"message":f"Article updated successfully with id:{id}"}),200
   else:
      return jsonify({"message":"Article not updated"}),404
@bp.route('/<int:id>',methods=['DELETE'])
def delete(id):
   blog=blogs(db)
   result=blog.delete_blog(id)
   if result:
      return jsonify({"message":f"Article deleted successfully with id:{id}"}),204
   else:
      return jsonify({"message":"Article not deleted"}),404
@bp.route('/<int:id>',methods=['PATCH'])
def update_patch(id):  
   blog=blogs(db)
   data=request.get_json()
   result=blog.update_blog_patch(id,data)
   if result:return jsonify({"message":f"Article updated succesfully with id:{id}"}),200
   else:return jsonify({'message':'Article not updated'}),404
@bp.route('/<int:id>',methods=['GET'])
def get_blog(id):
   blog=blogs(db)
   article=blog.get_blog(id)
   if article is not None:
      return jsonify({"id":article.id,"title":article.title,'content':article.content,
                     'tags':article.tags,'createdAt':article.createdAt,'updatedAt':article.updatedAt}),200
   else:
      return jsonify({'message':'Article not found'}),404
from datetime import datetime
from .models import Blogs
from sqlalchemy.exc import IntegrityError,OperationalError,InvalidRequestError
class blogs:
    def __init__(self,db):
        self.db=db
    def get_blogs(self):
        return Blogs.query.all()
    def add_blog(self,title,content,category,tags):
        try:
            createdAt=datetime.now()
            updatedAt=datetime.now()
            newblog=Blogs(title=title,content=content,category=category,tags=tags,createdAt=createdAt,updatedAt=updatedAt)
            self.db.session.add(newblog)
            self.db.session.commit()
            return True,newblog.id
        except IntegrityError as error:
            return False,error
        except OperationalError as error:
            return False,error
        except InvalidRequestError as error:
            return False, error
    def get_blog(self,id):
        try:
            blog=Blogs.query.get_or_404(id)
            return blog
        except:
            return None
        
    def update_blog(self,id,title,content,category,tags):
        try:
            blog=Blogs.query.get_or_404(id)
            blog.title=title
            blog.content=content
            blog.category=category
            blog.tags=tags
            blog.updatedAt=datetime.now()
            self.db.session.commit()
            return True
        except:
            return False
    def delete_blog(self,id):
        try:
            blog=Blogs.query.get_or_404(id)
            self.db.session.delete(blog)
            self.db.session.commit()
            return True
        except:
            return False
    def update_blog_patch(self,id,data):
        try:
            blog=Blogs.query.get_or_404(id)
            if len(data)>0:
                blog.updatedAt=datetime.now()
                if 'title' in data:
                    blog.title=data['title']
                if 'content' in data:
                    blog.content=data['content']
                if 'category' in data:
                    blog.category=data['category']
                if 'tags' in data:
                    blog.tags=data['tags']
                self.db.session.commit()
                return True
            else:
                return False
        except:
            return False
    
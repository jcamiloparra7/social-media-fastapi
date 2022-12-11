from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randint


def get_post_by_id(id):
    for post in my_posts:
        if post['id'] == id:
            return post


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
     

app = FastAPI()


my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1, "published": False, "rating": 3},
            {"title": "title of post2", "content": "content of post 2", "id": 2, "published": True, "rating": 4}]


@app.get('/')
def root():
    return {"message": "Hello world"}
    

@app.get('/posts')
def get_posts():
    return {"data": my_posts}


@app.post('/posts')
def create_post(payload: Post = Body(...)):
    post_id = randint(0, 1000)
    post_dict = payload.dict()
    post_dict['id'] = post_id
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get('/posts/{id}')
def get_specific_post(id):
    post = get_post_by_id(int(id))
    return post
    
    
        

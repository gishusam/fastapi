from app import schemas
import pytest


def test_get_all_posts(authorized_client, test_post):
    res = authorized_client.get("/posts/")
    
    print(res.json())
    assert res.status_code == 200


def test_unauthorized_get_all_posts(client):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_get_one_posts(client):
    res = client.get("/posts/test_post[0].id")
    assert res.status_code == 401    

def test_get_one_posts_not_existing(authorized_client, test_post):
    res = authorized_client.get(f"/posts/8000")
    assert res.status_code == 404

def test_get_one_post(authorized_client,test_post):
    res = authorized_client.get(f"/posts/{test_post[0].id}")
    post = schemas.Postout(**res.json())
    assert post.Post.id == test_post[0].id
    assert post.Post.content == test_post[0].content
    assert res.status_code == 200  

@pytest.mark.parametrize("title,content,published",[
    ("Test Title","Test Content",True),
    ("Best food ","Honey pork",False),
    ("Best team in Euro","Spain is the best team in Euro 2020",True),
])  
def test_create_post(authorized_client,test_user,test_post,title,content,published):
    res = authorized_client.post("/posts/",json ={"title":title,"content":content,"published":published}) 
    created_post = schemas.Post(**res.json())
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user["id"]
    assert res.status_code == 201

def test_default_published_value(authorized_client,test_user,test_post):
    res = authorized_client.post("/posts/",json = {"title":"Test Title","content":"Test Content"})
    created_post = schemas.Post(**res.json())
    assert created_post.title == "Test Title"
    assert created_post.content == "Test Content"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']
    assert res.status_code == 201

def test_unauthorized_user_create_post(client):
    res = client.post("/posts/",json = {"title":"Test Title","content":"Test Content"})
    assert res.status_code == 401    

def test_unathorized_user_delete_post(client,test_post,test_user):
    res=client.delete("/posts/test_post[0].id")
    assert res.status_code == 401

def test_successful_delete_post(authorized_client,test_post):
    res = authorized_client.delete(f"/posts/{test_post[0].id}")
    assert res.status_code == 204

def test_delete_post_not_existing(authorized_client,test_post):
    res = authorized_client.delete(f"/posts/8000")
    assert res.status_code == 404  

def test_deleting_post_not_owned(authorized_client,test_post):
    res = authorized_client.delete(f"/posts/{test_post[3].id}")
    assert res.status_code == 403      

def test_update_post(authorized_client,test_post):
    data = {"title":"Updated Title","content":"Updated Content","id":test_post[0].id}
    res = authorized_client.put(f"/posts/{test_post[0].id}",json = data)   

    updated_post = schemas.Post(**res.json())
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]
    assert res.status_code == 200

def test_update_post_belonging_to_another_user(authorized_client,test_post):
    data = {"title":"Updated Title","content":"Updated Content","id":test_post[3].id}
    res = authorized_client.put(f"/posts/{test_post[3].id}",json = data)   
    assert res.status_code == 403


def test_unauthorized_update_post(client,test_post):
    data = {"title":"Updated Title","content":"Updated Content","id":test_post[0].id}
    res = client.put(f"/posts/{test_post[0].id}",json = data)   
    assert res.status_code == 401

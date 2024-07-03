import pytest
from app import models

@pytest.fixture()
def test_vote(test_post,test_user,session):
    new_vote = models.Vote(post_id = test_post[3].id, user_id = test_user['id'])
    session.add(new_vote)
    session.commit()

def test_vote_on_a_post(authorized_client,test_post):
    res = authorized_client.post(f"/votes/", json = {"post_id": test_post[3].id, "dir": 1})

    assert res.status_code == 404

def test_vote_on_a_post_already_voted(authorized_client,test_post,test_vote):
    res = authorized_client.post(f"/votes/", json = {"post_id": test_post[3].id, "dir": 1})
    assert res.status_code == 409       

# def test_delete_vote(authorized_client,test_post,test_vote):
    # res = authorized_client.delete(f"/votes/", json = {"post_id": test_post[3].id, "dir": 0})
    # assert res.status_code == 201   

def test_delete_vote(authorized_client, test_post, test_vote):
    post_id = test_post[3].id
    dir = 0
    res = authorized_client.delete(f"/votes/?post_id={post_id}&dir={dir}")
    assert res.status_code == 405

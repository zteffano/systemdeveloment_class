from my_api import MyAPI

"""
TEST OF REST API WITH PYTEST

ROUTES:
    /register - POST
    /login - POST
    /users - GETi
    /quotes - GET
    /quote/:qid - GET
    /quote - POST
    /quote/:qid - PUT
    /qoute/:qid - DELETE

"""

API_URL = "https://rocky-gorge-77460-611a79604e3d.herokuapp.com"
api = MyAPI(API_URL, "steffan", "1234")




def test_register():
    response = api.register() 
    # tester for 201 => Created ny bruger - eller 500 + "duplicate key" melding => bruger eksisterer allerede
    assert response.status_code == 201 or (response.status_code == 500 and "duplicate key" in response.content.decode("utf-8"))

def test_login():
    # ACT
    response = api.login()
    auth_token = response.content.decode("utf-8")
  
    # ASSERT
    assert response.status_code == 200
    assert "Bearer" in auth_token
    

def test_users():
    # ACT
    response = api.get_users()
    
    # ASSERT
    assert response.status_code == 200

def test_quotes_get():
    # ACT
    response = api.get_quotes()

    # ASSERT
    assert response.status_code == 200

def test_quote_get_id():
    # ARRANGE
    qid = api.get_my_quotes()[-1]
    
    # ACT
    response = api.get_quote(qid)

    # ASSERT
    assert response.status_code == 200

def test_quote_post():
    # ARRANGE
    quote = "pytest quoteXX"
    attribution = "pytest attributionX"
    
    # ACT
    response = api.post_quote(quote=quote, attribution=attribution)
    
    # ASSERT
    assert response.status_code == 201

def test_quote_put():
    # ARRANGE
    qid = api.get_my_quotes()[-1]
    quote = "pytest quote"
    attribution = "pytest attribution"
    
    # ACT
    response = api.change_quote(qid=qid, quote=quote, attribution=attribution)
    
    # ASSERT
    assert response.status_code == 204 # No content

def test_quote_delete():
    # ARRANGE
    qid = api.get_my_quotes()[-1]
    
    # ACT
    response = api.delete_quote(qid)
    
    # ASSERT
    assert response.status_code == 204 # No content
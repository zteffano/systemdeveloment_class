from my_api import MyAPI

"""
TEST AF REST API

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
    # Test login
    response = api.login()
    auth_token = response.content.decode("utf-8")

    assert response.status_code == 200
    assert "Bearer" in auth_token
    

def test_users():

    response = api.get_users()
    assert response.status_code == 200

def test_quotes_get():

    response = api.get_quotes()
    assert response.status_code == 200

def test_quote_get_id():
    qid = api.get_my_quotes()[-1]
    response = api.get_quote(qid)
    assert response.status_code == 200

def test_quote_post():
    quote = "pytest quoteXX"
    attribution = "pytest attributionX"
    response = api.post_quote(quote=quote, attribution=attribution)
    assert response.status_code == 201


def test_quote_put():
    qid = api.get_my_quotes()[-1]
    quote = "pytest quote"
    attribution = "pytest attribution"
    response = api.change_quote(qid=qid, quote=quote, attribution=attribution)
    assert response.status_code == 204 # No content

def test_quote_delete():
    qid = api.get_my_quotes()[-1]
    response = api.delete_quote(qid)
    assert response.status_code == 204 # No content


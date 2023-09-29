from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
import http.server
import socketserver
import threading


URL = "http://localhost:9999/index.html"

#med pytest.fixture, server moduler og threading kan håndtere jeg serveren der loader min index.html .

# Serveren
@pytest.fixture(scope='module') #The scope='module' ensures that the fixture is activated once per module (i.e., once per Python file) and not once per test function.
def server():
    PORT = 9999
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.start()
    yield  # før yield = setup fasen  - yield pauser så instruktionerne og lader mig køre alle test pga.(scope='module') og efter yield ("teardown fasen")
    httpd.shutdown()
    thread.join()

# Min Webdriver
@pytest.fixture
def driver():
    _driver = webdriver.Chrome() # brug webdriver.Firefox() hvis Firefox ønskes eller ligeledes ved de andre.
    yield _driver # pauser min driver og når testen er ovre , så fortsætter den til .quit (denne kører kun per funktion, da det er default scope)
    _driver.quit()


# Håndtere operationer i denne funktion, for at gøre det hele mere simpelt og testen mere læsbar
def do_operation(driver, operation, input=""):
    WebDriverWait(driver,5).until(EC.title_is("Rational Calculator")) # Tjekker at siden er loaded ved at kigge på title. Timeout er sat til 5.
    input_field = driver.find_element(By.ID, "input-field")
    operation_button = driver.find_element(By.ID, operation)
    current_value = driver.find_element(By.ID, "current-value")
    
    input_field.clear()
    input_field.send_keys(input)
    operation_button.click()
    sleep(0.2)
    return current_value.text


def test_site_load(server,driver): # server parameteren er for at pytest ved vores server "fixture" skal være aktiv før vi kører denne funktion
    driver.get(URL)
    WebDriverWait(driver,10).until(EC.title_is("Rational Calculator"))  # Tjekker at siden er loaded ved at kigge på title. Timeout er sat til 10
    assert driver.title == "Rational Calculator"


def test_formatting(server,driver):
    driver.get(URL)
    assert "-1/2" == do_operation(driver,"add","1/-2")
    assert "1/2" == do_operation(driver, "mul", "-1")
    assert "0" == do_operation(driver, "mul", "0")
    assert "-1/2" == do_operation(driver,"sub","1/2")
    assert "-2/1" == do_operation(driver,"invert") # invert på aktuel værdi, når der ingen 3 argument er givet



def test_add(server, driver):
    driver.get(URL)
    assert "1/2" == do_operation(driver,"add","1/2")
    assert "3/4" == do_operation(driver,"add","1/4")
    assert "5/4" == do_operation(driver,"add","1/2")

def test_sub(server, driver):
    driver.get(URL)
    assert "2/4" == do_operation(driver,"sub","2/4")
    assert "-1/4" == do_operation(driver,"sub","3/4")
    assert "3/4" == do_operation(driver, "sub", "2/-2")

def test_mul(server, driver):
    driver.get(URL)
    assert "-2/2" == do_operation(driver,"mul","-2/2")
    assert "-1/2" == do_operation(driver,"mul","1/2")
    assert "1/4" == do_operation(driver, "mul", "1/-2")

def test_div(server,driver):
    driver.get(URL)
    assert "1/2" == do_operation(driver,"div","1/2")
    assert "2/1" == do_operation(driver,"div","1/4")
    assert "2/1" == do_operation(driver,"div","1")

def test_invert(server,driver):
    assert "2/1" == do_operation(driver, "invert","1/2")
    assert "1/2" == do_operation(driver, "invert") # invert på aktuel værdi, når der ingen 3 argument er givet
    assert "-2/1" == do_operation(driver, "invert", "-1/2")

def test_reduce(server, driver):
    driver.get(URL)
    assert "1/2" == do_operation(driver, "reduce", "50/100")
    assert "-1/2" == do_operation(driver, "reduce", "-15000/30000")
    assert "2/7" == do_operation(driver, "reduce", "4/14")

def test_negate(server,driver):
    driver.get(URL)
    assert "-1/2" == do_operation(driver, "negate", "1/2")
    assert "1/2" == do_operation(driver, "negate") # negate på aktuel værdi, når der ingen 3 argument er givet (brug af default i do_operation)
    assert "4/4" == do_operation(driver, "negate", "4/-4")
    assert "4/4" == do_operation(driver, "negate", "-4/4")

def test_clear(server,driver):
    driver.get(URL)
    assert "1/2" == do_operation(driver, "add", "1/2")
    assert "" == do_operation(driver, "clear")


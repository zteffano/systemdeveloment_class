from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

"""HTML:
    <h1>A Rational Calculator!</h1>

    <h3>Rational Calculator V0.9</h3>
    <div class="calc-container">
        <input type="text" id="input-field"/>
        <button id="add">+</button>
        <button id="sub">-</button>
        <button id="mul">*</button>
        <button id="div">/</button>
        <button id="invert">^</button>
        <button id="reduce">=></button>
        <button id="negate">NEG</button>
        <button id="clear">C</button>
        <!-- <button id="test">TEST FORMAT</button> -->
    </div>
    <div id="current-value"></div>
"""


#driver = webdriver.Chrome()
# start a server at this URL:
URL = "http://localhost:9999/index.html"
"""
# start server:
import http.server
import socketserver
import threading
def test_start_server():
    PORT = 9999
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.start()
""" 



"""ELEMENTS
input_field = driver.find_element(By.ID, "input-field")
add_button = driver.find_element(By.ID, "add")
sub_button = driver.find_element(By.ID, "sub")
mul_button = driver.find_element(By.ID, "mul")
div_button = driver.find_element(By.ID, "div")
invert_button = driver.find_element(By.ID, "invert")
reduce_button = driver.find_element(By.ID, "reduce")
negate_button = driver.find_element(By.ID, "negate")
clear_button = driver.find_element(By.ID, "clear")
current_value = driver.find_element(By.ID, "current-value")

"""
SLEEP_TIME = 0.3

def get_driver(browser="chrome"):
    if browser.lower() == "firefox":
        return webdriver.Firefox()

    return webdriver.Chrome()

    

def test_site_load():
    driver = get_driver()
    driver.get(URL)
    sleep(2) # longer sleep time to see the page
    assert driver.title == "Rational Calculator"
    print(driver.title)
    driver.quit()

def test_add():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    add_button = driver.find_element(By.ID, "add")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("1/2")
    sleep(SLEEP_TIME)
    add_button.click()
    sleep(SLEEP_TIME)
    input_field.clear()
    input_field.send_keys("1/4")
    add_button.click()
    assert current_value.text == "3/4"
    sleep(SLEEP_TIME)
    add_button.click()
    sleep(SLEEP_TIME)
    assert current_value.text == "5/4"

def test_sub():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    sub_button = driver.find_element(By.ID, "sub")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("1/2")
    sleep(SLEEP_TIME)  
    sub_button.click()
    sleep(SLEEP_TIME)
    input_field.clear()
    input_field.send_keys("1/4")
    sub_button.click()
    assert current_value.text == "1/4"


def test_mult():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    mul_button = driver.find_element(By.ID, "mul")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("1/2")
    sleep(SLEEP_TIME)  
    mul_button.click()
    sleep(SLEEP_TIME)
    input_field.clear()
    input_field.send_keys("1/4")
    mul_button.click()
    assert current_value.text == "1/8"
    sleep(SLEEP_TIME)
    input_field.clear()
    input_field.send_keys("-1/4")
    mul_button.click()
    assert current_value.text == "1/-8"


def test_div():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    div_button = driver.find_element(By.ID, "div")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("1/2")
    sleep(SLEEP_TIME)
    div_button.click()
    sleep(SLEEP_TIME)
    input_field.clear()
    input_field.send_keys("1/4")
    div_button.click()
    assert current_value.text == "2/1"
    sleep(SLEEP_TIME)
    div_button.click()
    assert current_value.text == "1/4"


def test_invert():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    invert_button = driver.find_element(By.ID, "invert")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("1/2")
    sleep(SLEEP_TIME)
    invert_button.click()
    assert current_value.text == "2/1"


def test_reduce():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    reduce_button = driver.find_element(By.ID, "reduce")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("2/4")
    sleep(SLEEP_TIME)
    reduce_button.click()
    assert current_value.text == "1/2"

def test_negate():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    negate_button = driver.find_element(By.ID, "negate")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("1/2")
    sleep(SLEEP_TIME)
    negate_button.click()
    assert current_value.text == "-1/2"
    sleep(SLEEP_TIME)
    negate_button.click()
    assert current_value.text == "1/2"

def test_clear():
    driver = get_driver()
    driver.get(URL)
    input_field = driver.find_element(By.ID, "input-field")
    clear_button = driver.find_element(By.ID, "clear")
    current_value = driver.find_element(By.ID, "current-value")
    input_field.clear()
    input_field.send_keys("1/2")
    sleep(SLEEP_TIME)
    clear_button.click()
    assert current_value.text == ""






    
    


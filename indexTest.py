# imports
from selenium import webdriver
import time;
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# set driver
browser = webdriver.Edge()
browser.get('http://127.0.0.1:5500/index.html')
# functions
elementOne = browser.find_element(By.ID, "element-one")
elementTwo = browser.find_element(By.ID, "element-two")
elementThree = browser.find_element(By.ID, "element-three")
elementFour = browser.find_element(By.ID, "element-four")
def test1():
    act = ActionChains(browser)
    act.double_click(on_element=elementOne)
    act.perform() 
    assert 'animation' in elementOne.get_attribute('class')
    browser.save_screenshot("feladat1.png")
    print('sikeres!')

def test2():
    act = ActionChains(browser)
    act.move_to_element(elementTwo).perform()
    
    assert "box-shadow: 5px 10px #888;" in elementTwo.get_attribute('style')
    browser.save_screenshot("feladat2.png")
    print("Sikeres!")

def test3():
    elementThree.click();
    assert "background-color: green;" in elementThree.get_attribute('style')
    browser.save_screenshot("feladat3.png")
    print("Sikeres!")

def test4():
    act = ActionChains(browser)
    act.move_to_element(elementFour).perform()
    browser.save_screenshot("feladat4.png")
    print("Sikeres!")


    

     

# test1: dupla kattintás után szerepel-e az "animation" classs
test1()
time.sleep(5)
# ha rámegy az egér, utána létezik-e box-shadow
test2()
time.sleep(5)
# kattintás után eltűnik-e
test3()
time.sleep(5)
# kattintás után a háttere zöld lesz-e
test4()
time.sleep(5)
# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)

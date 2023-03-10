import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def log_in():
    test_webdriver.get("https://www.facebook.com/messages/t")
    email_field = test_webdriver.find_element(By.ID, "email")
    email_field.send_keys("my_email")  # change
    passwd_field = test_webdriver.find_element(By.ID, "pass")
    passwd_field.send_keys("my_password")  # change
    passwd_field.submit()


def send_messages_to_all_people(people, message):
    for person in people:
        search_person = test_webdriver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/label/input")
        search_person.send_keys(person)
        time.sleep(3)
        search_person.send_keys(Keys.DOWN)
        search_person.send_keys(Keys.DOWN)
        search_person.send_keys(Keys.RETURN)
        time.sleep(5)
        send_message(message)


def send_message(message):
    text_field = test_webdriver.find_element(By.XPATH,
                                             "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p")
    text_field.send_keys(message)
    text_field.send_keys(Keys.RETURN)


if __name__ == '__main__':
    test_webdriver = webdriver.Chrome()
    log_in()
    time.sleep(15)
    people = ["Jan Kowalski"]  # change
    message = "Hello world"  # change
    send_messages_to_all_people(people, message)
    test_webdriver.quit()

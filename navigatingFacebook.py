#!/usr/bin/env python3
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def test_search():
    driver = webdriver.Firefox()
    driver.get("https://www.google.fr/")
    driver.find_element_by_name("q").send_keys("Facebook")
    driver.find_element_by_name("btnK").submit()
    time.sleep(5)
    driver.find_element_by_partial_link_text('Facebook - Connexion ou inscription').click()
    driver.find_element_by_name("email").send_keys("denozi.j@gmail.com")
    driver.find_element_by_name("pass").send_keys("")
    driver.find_element_by_id("u_0_2").submit()



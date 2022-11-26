import unittest
import requests
from flask import Flask, flash, redirect, render_template, request, session,url_for
from config import Config
from models import db, pacientes
from cs50 import SQL
db = SQL("sqlite:///florenceTest.db")

class TestUrls(unittest.TestCase):
    def test_list_mpaciente_false(self):
        url = "http://127.0.0.1:5000/mpacientes/"
        r = requests.get(url, verify=False, timeout=2)
        result= r.status_code
        self.assertEqual(result, 404)

    def test_list_mpaciente_true(self):
        url = "http://127.0.0.1:5000/mpacientes/a"
        r = requests.get(url, verify=False, timeout=2)
        result= r.status_code
        self.assertEqual(result, 200)

class TestCrud(unittest.TestCase):
    def test_list_insert_false(self):
        result = db.execute("Select * from users where id = 564654")
        self.assertEqual(result, [])
    
    def test_list_insert_true(self):
        result = db.execute("Select * from users")
        result = (type(result))
        self.assertEqual(result,type(list()))

if __name__ == '__main__':
    unittest.main()

import sqlite3

from flask import flash, url_for
from werkzeug.utils import redirect


class FDatBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def AddInfo(self, email, password):
        try:
            self.__cur.execute("INSERT INTO maininfo VALUES(NULL, ?, ?)", (email, password))
            self.__db.commit()

        except sqlite3.Error:
            flash("Error. Please, try again")
            return redirect(url_for("register"))

        return True

    def Check(self, email):
        try:
            res = self.__cur.execute(f"SELECT id FROM maininfo WHERE email = {email}")
            if res:
                return email
        except sqlite3.Error:
            flash("Error. Please, try again")
            return redirect(url_for("main_page"))

    def CheckPass(self, password, email):
        try:
            res1 = self.__cur.execute(f"SELECT id FROM maininfo WHERE email = {email}")
            res2 = self.__cur.execute(f"SELECT id FROM maininfo WHERE password = {password}")
            if res1 and res2:
                return True
            else:
                return False
        except sqlite3.Error:
            flash("Error. Please, try again")
            return redirect(url_for("main_page"))

    def GetPersonalStocks(self, id: int) -> object:
        try:
            self.__cur.execute(f"SELECT symbol FROM account WHERE id = {id}")
            stocks: list = self.__cur.fetchall()
            if stocks:
                return stocks
        except sqlite3.Error:
            flash("Error. Please, try again")
            return redirect(url_for("main_page"))

    def GetBalance(self, id):
        try:
            balance = self.__cur.execute(f"SELECT cash FROM maininfo WHERE id = {id}")
            if balance:
                return balance
        except sqlite3.Error:
            flash("Error. Please, try again")
            return redirect(url_for("main_page"))

    def GetId(self, email):
        try:
            id = self.__cur.execute(f"SELECT id FROM maininfo WHERE email = {email}")
            if id:
                return id
        except sqlite3.Error:
            flash("Error. Please, try again")
            return redirect(url_for("main_page"))

    def GetStocks(self):
        try:
            res = self.__cur.execute(f"SELECT symbol FROM stock")
            return res
        except sqlite3.Error:
            flash("Error. Please, try again")
            return redirect(url_for("main_page"))


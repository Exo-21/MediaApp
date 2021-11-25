import bcrypt
from db.db_manager import DbManager
from PyQt5.QtCore import QDate, QDateTime


class DataManager:

    @staticmethod
    def login(username, password):
        return DbManager.login(username, password)

    @staticmethod
    def register(email, username, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return DbManager.register(email, username, hashed, salt)

    @staticmethod
    def addReview(title, date, review, userId):
        date = QDateTime(date).toPyDateTime()
        return DbManager.addReview(title, date, review, userId)

    @staticmethod
    def loadReviews():
        return DbManager.loadReviews()

    @staticmethod
    def removeReview(reviewId):
        DbManager.removeReview(reviewId)

    @staticmethod
    def editReview(reviewId, title, date, review):
        date = QDateTime(date).toPyDateTime()
        return DbManager.editReview(reviewId, title, date, review)

    @staticmethod
    def isUserSignedIn(userId, token):
        return DbManager.isUserSignedIn(userId, token)
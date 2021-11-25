import pymongo
import secrets
import bcrypt

client = pymongo.MongoClient(
        "mongodb+srv://exo25:kecske@media.cypna.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

class DbManager:

    @staticmethod
    def login(username, password):
        user = db.user.find_one({'username': username})
        if user:
            hashed = bcrypt.hashpw(password.encode('utf-8'), user['salt'])
            if hashed == user['password']:
                token = secrets.token_hex(16)
                user['token'] = token
                db.user.save(user)
                return user
            else:
                return None
        else:
            return None

    @staticmethod
    def register(email, username, password, salt):
        return db.user.insert_one({'username': username,
                                        'password': password,
                                        'salt': salt,
                                        'token': '',
                                        'email': email})

    @staticmethod
    def addReview(title, date, review, userId):
        return db.review.insert_one({'title': title,
                                   'date': date,
                                   'review': review,
                                   'userId': userId})

    @staticmethod
    def loadReviews():
        return db.review.find({})

    @staticmethod
    def removeReview(reviewId):
        db.review.delete_one({'_id': reviewId})

    @staticmethod
    def editReview(reviewId, title, date, review):
        reviewObj = db.review.find_one({'_id': reviewId})
        if reviewObj:
            reviewObj['title'] = title
            reviewObj['date'] = date
            reviewObj['review'] = review
            db.review.save(reviewObj)
            return reviewObj
        else:
            return None

    @staticmethod
    def isUserSignedIn(userId, token):
        user = db.user.find_one(
            {
                '_id': userId,
                'token': token
            }
        )
        if user:
            return True
        else:
            return False

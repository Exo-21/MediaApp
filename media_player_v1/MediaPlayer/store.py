class Store:
    currentUser = None

    @staticmethod
    def setUser(user):
        Store.currentUser = user


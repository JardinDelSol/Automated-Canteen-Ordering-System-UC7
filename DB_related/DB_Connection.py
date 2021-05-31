import pandas as pd


def getDB():
    df = pd.read_csv("DB_related/tempDB.csv", index_col=0)
    return df


class BalanceSearchRequest:
    def __init__(self, userID):
        self.userID = userID


class ReloadRequest(BalanceSearchRequest):
    def __init__(self, userID, amount=0):
        self.userID = userID
        self.amount = amount

    def update(self, amount=0):
        self.amount = amount


class MONEY:
    def __init__(self):
        self.amount = None

    def create(self, amount):
        self.amount = amount

    def update(self, amount):
        self.amount += amount


class BalanceCheckConnection:
    def __init__(self, BSrequest, money):
        self.BSrequest = BSrequest
        self.money = money

    def event(self):
        self.getBalance()

    def getBalance(self):
        try:
            df = getDB()
            userID = self.BSrequest.userID
            try:
                amount = df[df["UserID"] == userID]["Balance"].values[0]
                self.money.create(amount)
            except:
                self.money.create(0)
        except:
            self.money.create(0)


class ReloadConnection:
    def __init__(self, Request, money):
        self.Request = Request
        self.money = money

    def event(self):
        self.reloadBalance()

    def reloadBalance(self):
        try:
            df = getDB()
            userID = self.Request.userID
            amount = self.Request.amount
            if amount <= 0:
                self.money.update(0)
            else:
                try:
                    newBalance = (
                        df[df["UserID"] == userID]["Balance"].values[0] + amount
                    )
                    df.loc[df.UserID == userID, "Balance"] = newBalance
                    df.to_csv("DB_related/tempDB.csv")
                    self.money.update(amount)
                except:
                    self.money.update(0)
        except:
            self.money.update(0)

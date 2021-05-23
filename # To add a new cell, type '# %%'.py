# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
df = pd.read_csv("tempDB.csv")
df.head()


# %%
def getDB():
    df = pd.read_csv("tempDB.csv")
    df.head()
    return df


# %%
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
        print("Amount set: {}".format(self.amount))

    def update(self, amount):
        print("Before: {}".format(self.amount))
        self.amount += amount
        print("After: {}".format(self.amount))


# %%
class BalanceCheckConnection:
    def __init__(self, BSrequest, money):
        self.BSrequest = BSrequest
        self.money = money

    def event():
        self.getBalance()

    def getBalance(self):
        df = getDB()
        userID = self.BSrequest.userID
        amount = df[df["UserID"] == userID]["Balance"].values[0]
        self.money.create(amount)


# %%
class ReloadConnection:
    def __init__(self, Rrequest, money):
        self.Rrequest = Rrequest
        self.money = money

    def event(self):
        self.reloadBalance()

    def reloadBalance(self):
        df = getDB()
        userID = self.Rrequest.userID
        amount = self.Rrequest.amount
        # print("userID = {} amount = {}".format(userID, amount))
        newBalance = df[df["UserID"] == userID]["Balance"].values[0] + amount
        df[df["UserID"] == userID] = newBalance
        # print(newBalance)
        self.money.update(amount)


# %%
bcrequest = BalanceSearchRequest("a")
rrequest = ReloadRequest("a", 500)

money = MONEY()
bcconnection = BalanceCheckConnection(bcrequest, money)

bcconnection.getBalance()

rrconnection = ReloadConnection(rrequest, money)

rrconnection.reloadBalance()

rrequest.update(1500)

rrconnection.reloadBalance()


# %%
rrconnection.event()


# %%

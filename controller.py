import db_related.db_connection as connection
import UI


class Controller:
    def __init__(self, userID):
        self.userID = userID
        self.money = connection.MONEY()
        self.balanceRequest = connection.BalanceSearchRequest(userID)
        self.reloadRequest = connection.ReloadRequest(userID)
        self.blanceConnection = connection.BalanceCheckConnection(self.balanceRequest, self.money)
        self.reloadConnection = connection.ReloadConnection(self.reloadRequest, self.money)
        self.InterfacePage = UI.UIMaker(UI.root,self.money)
    
    def getBalanceRequest(self, userID: str):
        self.balanceConnection.

    def 

        


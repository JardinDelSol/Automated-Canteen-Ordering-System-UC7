import DB_related.DB_Connection as connection
import interface as UI


class Controller:
    def __init__(self, userID):
        self.userID = userID
        self.money = connection.MONEY()
        self.balanceRequest = connection.BalanceSearchRequest(userID)
        self.reloadRequest = connection.ReloadRequest(userID)
        self.balanceConnection = connection.BalanceCheckConnection(
            self.balanceRequest, self.money
        )
        self.reloadConnection = connection.ReloadConnection(
            self.reloadRequest, self.money
        )

        self.Page=UI.InterfacePage(self, self.money)
        self.UIMaker=UI.UIMaker(self.Page)
        

    def getBalanceRequest(self):
        print("a")
        self.balanceConnection.event()
        self.UIMaker.event()
        self.Page.event()
        # UI 업데이트 된 금액 출력

    def getReloadAmount(self, amount):
        self.reloadRequest.update(amount)
        self.reloadConnection.event()
        self.UIMaker.event()
        self.Page.event()
        # UI


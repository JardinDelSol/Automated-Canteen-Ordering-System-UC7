import DB_related.DB_Connection as connection
import UI


class Controller:
    def __init__(self, userID):
        self.userID = userID
        self.money = connection.MONEY()
        self.balanceRequest = connection.BalanceSearchRequest(userID)
        self.reloadRequest = connection.ReloadRequest(userID)
        self.blanceConnection = connection.BalanceCheckConnection(
            self.balanceRequest, self.money
        )
        self.reloadConnection = connection.ReloadConnection(
            self.reloadRequest, self.money
        )
        self.InterfacePage = UI.UIMaker(self, self.money, UI.tk.Tk())
        self.InterfacePage.mainloop()

    def getBalanceRequest(self):
        self.blanceConnection.event()
        # self.InterfacePage.event()
        # UI 업데이트 된 금액 출력

    def getReloadAmount(self, amount):
        self.reloadRequest.update(amount)
        self.reloadConnection.event()
        # self.InterfacePage.event()
        # UI


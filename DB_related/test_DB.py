# import DB_related.DB_Connection as DB_Connection
from DB_Connection import *


def test_most_plausible():
    users = ["a", "b", "c", "d", "e"]
    for i in users:
        df = getDB()
        money = MONEY()
        bsr = BalanceSearchRequest(i)
        bcc = BalanceCheckConnection(bsr, money)
        bcc.event()
        assert money.amount == df[df["UserID"] == i]["Balance"].values[0]
        before = money.amount
        reload = 500
        rr = ReloadRequest(i, reload)
        rc = ReloadConnection(rr, money)
        rc.event()
        df = getDB()
        assert before + reload == df[df["UserID"] == i]["Balance"].values[0]


# 사용자가 없는 사용자인 경우
def test_not_plausible():
    users = ["f", "g", "h", "i", "j"]
    for i in users:
        df = getDB()
        money = MONEY()
        bsr = BalanceSearchRequest(i)
        bcc = BalanceCheckConnection(bsr, money)
        bcc.event()
        assert money.amount == 0
        before = money.amount
        reload = 500
        rr = ReloadRequest(i, reload)
        rc = ReloadConnection(rr, money)
        rc.event()
        assert money.amount == 0


#


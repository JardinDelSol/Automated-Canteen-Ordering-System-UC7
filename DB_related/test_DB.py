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


# 다양한 금액에 대하여 테스트
# 입력 가능한 금액과 불가능한 금액(음수) 및 00000과 같은 경우에 대한 테스트
def test_different_amounts():
    amounts = [100, -100, 200, 300, 000000, 9, -1, 0, 3]
    for reload in amounts:
        df = getDB()
        money = MONEY()
        bsr = BalanceSearchRequest("a")
        bcc = BalanceCheckConnection(bsr, money)
        bcc.event()
        assert money.amount == df[df["UserID"] == "a"]["Balance"].values[0]
        before = money.amount
        rr = ReloadRequest("a", reload)
        rc = ReloadConnection(rr, money)
        rc.event()
        df = getDB()
        if reload >= 0:
            assert before + reload == df[df["UserID"] == "a"]["Balance"].values[0]
        else:
            assert before == df[df["UserID"] == "a"]["Balance"].values[0]


# DB가 존재하지 않는 경우(잘못된 connection을 생성한 경우)
def test_no_DB():
    users = ["f", "g", "h", "i", "j"]
    for i in users:
        df = pd.DataFrame(columns=["a"])
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

# import DB_related.DB_Connection as DB_Connection
from DB_Connection import *


def test_balance_check_connection():
    df = getDB()
    for i in range(5):
        money = MONEY()
        bsr = BalanceSearchRequest(str(i))
        bcc = BalanceCheckConnection(bsr, money)
        bcc.event()
        assert money.amount == df[df["UserID"] == str(i)]["Balance"].values[0]

import DB_related.DB_Connection as connection
import UI
from controller import *


def main():
    controller = Controller(userID="temp")
    controller.getBalanceRequest()


if __name__ == "__main__":
    main()


from controller import *


def main():
    # controller = Controller(userID="a")
    # controller.Page.start()
     
    controller = Controller(userID="a")
    controller.Page.test_flg=2
    controller.Page.start()
    controller.Page.test("100000")
    print(controller.Page.input)
    
    
   # controller = Controller(userID="a")
 #   controller.Page.start()
    # ----initial money setup


if __name__ == "__main__":
    main()
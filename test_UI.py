# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:39:36 2021

@author: 정훈석
"""
from controller import *
def test_interface_input():
    #테스트 케이스 종류
    # 정상입력 // 숫자가 아닌 입력 // 음수 입력 // 소수입력
    data_put=["1000","123","0","2000","3000","&","ㅁㄴㅇ","12asd","","-1234","0","1235.023","134.0"]
    data_in=[1000,123,0,2000,3000,0,0,0,0,0,0,0,0]
    
    controller = Controller(userID="a")
    controller.Page.test_flg=2
    controller.Page.start()
    
    print(controller.Page.input)
    for i in range(len(data_put)):
        money_before=controller.money.amount
        
        controller.Page.test(data_put[i])
        #입력한 값이 제대로 input에 들어가는 지 확인
        assert controller.Page.input==data_in[i]
        
        money_after=money_before+data_in[i]
        
        #input에 들어간 값이 제대로 더해지는 확인
        assert controller.money.amount==money_after
        
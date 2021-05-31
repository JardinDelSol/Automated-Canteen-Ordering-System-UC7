# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import tkinter as tk
import re

class InterfacePage(tk.Frame):
    def __init__(self,controller,money):
        self.root=tk.Tk()
        super().__init__(self.root)
        self.controller=controller
        self.input = 0
        self.money = money
        
        self.test_flg=0 #테스트용 flg 0이면 정상작동 1이면 테스트용 2이면 아무것도 수행안함
        
        self.label = tk.Label(self)
        self.label.config(text="현재 금액 = " + str(self.money.amount))
        
        self.inputtext= tk.StringVar()
        self.inputtext.set("0")
        
        self.entry = tk.Entry(self,textvariable=self.inputtext)
        
        self.button = tk.Button(self)
        self.button["text"] = "입력"
        self.button["command"] = self.enterAmount
        
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        
        self.flg=1

    
        
    def enterAmount(self):
        ##########
        p=re.compile('[0-9]+$')
        m=p.match(self.entry.get())
        if m:
            print("Yes")
            self.input = int(self.entry.get())
        else:
            self.input = 0
        
        self.label.config(text="충전 금액 = " + str(self.input))
        self.flg=0
        
        if(self.test_flg==1):
            print(self.input)
            self.controller.getReloadAmount(self.input)
        elif(self.test_flg==0):
            print(self.input)
            self.controller.getReloadAmount(self.input)

    def display(self):
         while(self.flg):
             self.update_idletasks()
             self.update()
         self.flg=1
         print("OK")
         
    def start(self):
        self.controller.getBalanceRequest()
        
    def event(self,test_flg=0):
        if(self.test_flg==0):
            self.display()

    def test(self,input_text): 
        self.test_flg=1
        self.inputtext.set(input_text)
        self.button.invoke()

        
        

class UIMaker:
    def __init__(self, Page:InterfacePage):
        self.Page = Page
        self.setPage()
        
    def setPage(self):
        self.Page.root.geometry("300x500+100+100")
        self.Page.root.resizable(False, False)
        self.Page.pack()
        self.Page.label.pack(side="top")
        self.Page.entry.pack()
        self.Page.button.pack(side="top")
        self.Page.quit.pack(side="bottom")

    def render(self):
        self.Page.label.config(text="현재 금액 = " + str(self.Page.money.amount))
        
    def event(self):
        self.render()


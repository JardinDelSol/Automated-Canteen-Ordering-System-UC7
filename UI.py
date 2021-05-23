# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import tkinter as tk


class UIMaker(tk.Frame):
    def __init__(self, controller, money, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x500+100+100")
        self.master.resizable(False, False)
        self.pack()
        self.money = money
        self.controller = controller
        self.input = 0
        self.render()

    def render(self):

        self.label = tk.Label(self)
        self.controller.getBalanceRequest()
        self.label.config(text="현재 금액 = " + str(self.money.amount))
        self.label.pack(side="top")
        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self)
        self.button["text"] = "입력"
        self.button["command"] = self.enterAmount
        self.button.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def enterAmount(self):
        self.input = int(self.entry.get())
        self.controller.getReloadAmount(self.input)
        self.label.config(text="충전 금액 = " + str(self.money.amount))
        

    def event(self):
        self.render()


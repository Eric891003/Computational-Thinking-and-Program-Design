# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bVd9_9KIPJWzT3SirLLplP5vJdVtOmgi
"""

# 聊天機器人自我介紹
print("哈囉。我是Zyxo 64。我是一個聊天機器人。") 
print("我喜歡動物，也喜歡聊食物。")

# 取得使用者名字
name = input("你叫什麼名字?: ")

# 打招呼
print("你好", name, "很高興認識你")

# 從使用者取得今年年份
 year = input("我記不太清楚日期。今年是幾年?: ")
 print("好的，我覺得沒錯。謝謝!")

 # 請使用者猜年齡
 myage = input("你能猜出我的年齡嗎? - 輸入一個數字: ")
 print("沒錯，你猜對了。我", myage)

 # 計算聊天機器人滿100歲的年份
 myage = int(myage)
 nyears = 100 - myage
 print("我再", nyears, "年就滿100歲了。")
 print("到時候是", int(year) + nyears) # 將今年年份轉換為整數

# 食物話題
 print("我喜歡巧克力，也喜歡嘗試各種新食物。")
 food = input("你呢。你最喜歡的食物是什麼?: ") 
 print("我也喜歡", food)
 question = "你多久吃一次" + food + "?: " 
 howoften = input(question) 
 print("真有趣。不知道這樣對健康好不好!")



# 關於心情的對話
feeling = input("你今天覺得如何?; ") 
print("為什麼你現在覺得", feeling, "呢?") 
reason = input("請告訴我: ") 
print("我知道了。謝謝分享。")

# 道別
print("今天事情真多!") 
print("我累到無法繼續聊天了，之後再聊。")
print("再見", name, "我喜歡跟你聊天!")


#!/usr/bin/python3
import random
wron = 0
righ=0
while True:
 
 key= random.choice(range(4))
 
 a = random.choice(range(100))
 b = random.choice(range(100))    
# 难度随机

 if key == 0:
  an =  a + b 
  print ('\n')
  print (a,"+",b)
  ian = input ("答案:" )
   
  # 加法出题模块
  
 if key == 1:
      while  b > a:         
                   a = random.choice(range(100))
                   b = random.choice(range(100))   
      an = a - b 
      print ('\n')
      print (a,"-",b )
      ian = input ("答案:" ) 
 
              
  # 减法出题模块
 if key == 2:
      an = a * b
      
      print ('\n')
      print (a,"x",b )
      ian= input ("答案:" )

      #乘法出题模块
 
 if key == 3:
   while  b > a:         
                   a = random.choice(range(100))
                   b = random.choice(range(100))   
   try:
      dan = a*b

      an = dan/b
   except ZeroDivisionError:
      while b == 0:
         b = random.choice(range(100))
         dan = a*b
         an = dan/b


   an=int(an)
   print('\n')
   print (dan,"÷",b )
   ian= input ("答案:" )

 an = str(an)   
 if an == ian :
    print ("正确")
    righ = righ+1
    print("正确题数：",righ)
    print("错误题数:",wron)
 else:
    print ("错误")
    print ("答案:",an)
    wron =wron+1
    print("正确题数：",righ)
    print("错误题数:",wron)
    
    # 答案比对

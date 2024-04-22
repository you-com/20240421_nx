import itertools




n,k = list(map(int,input().split())
"""           
n = 2
k = 2
"""

def action(s):
 tt = False
 for i in range(len(s)):
   if i + k <= len(s):
     t = True
     #k個連続で続くかの確認
     for j in range(k-1):
       #2連続の数字が同じじゃない時
       if s[i + j] != s[i + j + 1]:
         t = False
         break
     if t:
       tt = True
       break
 return tt


#乱数の作成
l = ['0', '1']
all = list(itertools.product(l, repeat = n-1))
all_len = len(all)


anser = 1
#nとkの値が同じ場合　1個
if n != k:
 anser_list = []
 for x in all:
   s = str(1) + "".join(x)
   if action(s):
     anser_list.append(s)
     #print(s)
 anser = len(anser_list)




#print(anser,all_len)
print(1 - (anser / all_len))


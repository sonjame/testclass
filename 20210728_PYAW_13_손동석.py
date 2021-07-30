# 001
x = ''
if bool(x): 
    print('Yes') 
else:
    print('No')  

# 답은c                  # x = ''은 빈 문자열이어서 빈문자열은 NO를 나타냅니다.

# 002
x = ' ' 
if bool(x):
    print('Yes') 
else:
    print('No')

# 답은c                  # 공백만있는 문자열은 NO를 나타냅니다.

# 003
x = []
if bool(x):
    print('Yes')
else:
    print('No')

# 답은a                 #빈리스트는 NO를 나타냅니다. 
 
# 004
x = [1, 2, 3]
if bool(x):
    print('Yes')
else:
    print('No')

#답은b                 #값이있는 리스트는 Yes를 나타냅니다.

# 005
x = '' 
if not bool(x):
    print('Yes') 
else: 
    print('No')

#답은a                #비어있는 문자열은 False를 나타내는데 if문을 보면 not bool(x)라고 입력되어 있어 Yes를 나타냅니다.

# 006
x = 'print("Python")' 
eval(x) 

#답은 Python         #eval() 함수으로 인해서 매개변수 문자열 print("Python")으로 출력 되어서 Python으로 출력됩니다.

# 007

x = input("Enter an expression: ") 
print(eval(x))

#답은C               #eval() 함수으로 print(input("Enter an expreaaion:"))로 나오게 됩니다.
                     #여기서 45*2를 input() 함수를 입력하면 90이 출력됩다.

# 008

x = print("Python 3", end='') 
print(" is Good")
exec(x)

#답은a              #exec() 함수는 문자열로 인식된 문을 인수 받아 컴파일 역할을 합니다. 그래서 Python 3 is Good 여기서
                    #end '' 는 문자끝을 나타냅니다. 즉 Python 3중 3으로 문자를 더이상 나타내지 않는다는 뜻을 나타냅니다.

# 009

a = ['a', 'b', 'c', 'A', 'B']  
print(max(a)) 

#답은d             #max()는 여기서 최대값을 출력합니다. 여기서 아스키코드를 이용하여 a = 97 b = 98 c = 99 A = 65 B = 66로 나타내기 때문에 c로 출력이 됩니다.

# 010

a = ['a', 'b', 'c', 'A', 'B'] 
print(min(a))

#답은b            #min()는 최소값을 나타냅니다. 위에서 똑같이 아스키코드를 이용하여 A를 출력합니다.

# 011

a = ['a', 'b', 'c', '1', '2', 'A', 'B'] 
print(max(a))

#답은a           #max()는 최대값을 나타냅니다. 위에서 똑같이 아스키코드를 이용하여 a를 출력합니다.

# 012

a = ['a', 'b', 'c', '1', '2', 'A', 'B']
print(min(a))

#답은c          #min()는 최소값을 나타냅니다. 아스키코드와 1, 2를 비교하여 최소값은 1을 출력합니다.

# 013

a = [1, 2, 3] 
print(sum(a))

#답은d        #sum()은 총합을 나타냅니다. 1+2+3은 6이기 때문에 6을 출력합니다.

# 014

a = list(range(0,10,3)) #range(시작숫자, 종료숫자, step)를 나타냅니다. 즉 0, 3, 6, 9를 나타냅니다.
print(sum(a))

#답은c                  #sum() 함수를 이용하여 0+3+6+9는 18이기 때문에 18로 출력합니다.

# 015


a = list(range(10,-10,3)) #range(시작숫자, 종료숫자, step)를 나타냅니다. 그런데 10부터 3씩 증가를 해야하는데 종료숫자가 -10을 나타내기 때문에 나타낼수가 없습니다.
print(sum(a))

#답은b                    #0을 나타냅니다.

# 016

a = list(range(-10,5,2)) #range(시작숫자, 종료숫자, step)를 나타냅니다. -10, -8, -6, -4, -2, 0, 2, 4
print(sum(a))

#답은a                   #-10 + -8 + -6 + -4 + -2 + 0 + 2 + 4으로 -24가 나옵니다.

# 017

x = [5, 4, 3, 2, 1]        
y = x.copy()            #copy() 함수로 [5, 4, 3, 2, 1]로 복사됩니다.
x[0] = 6 
print(y)                

#답은C                  #[5, 4, 3, 2, 1] 출력합니다.

# 018

import copy 
x = [5, 4, 3, 2, 1] 
y = copy.copy(x)      #copy() 함수로 [5, 4, 3, 2, 1]로 복사됩니다.
x.append(6)           #append()로 6이 추가되어 [6, 5, 4, 3, 2, 1]로 입력됩니다.
print(y[0])     

#답은a                #[6, 5, 4, 3, 2, 1]으로 추력됩니다.

# 019

import keyword 
print(keyword.iskeyword('Is'))

#답은d                #IS는 False으로 출력됩니다.

# 020

import keyword 
print(keyword.iskeyword('for'))

#답은a                #for는 True으로 출력됩니다.
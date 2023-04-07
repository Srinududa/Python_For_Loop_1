N = "query"
for i in N:
    print(N[0])
result==>>
q
q
q
q
q


a = "python"
for i in a:
    print(i)
result==>>
p
y
t
h
o
n



N = 7
for i in range(1,N+1):
    print(i)
result==>>
1
2
3
4
5
6
7



N = 8
sum = 0
for i in range(1, N+1):
    sum = sum + i
    avg = float(sum/N)
print(avg)
result==>>
4.5




N = 3
for i in range(1, N+1):
    cube = i**3
    print(cube)
result==>>
1
8
27


N = 3
8
11
25
for i in range(N):
    number = int(input())
    print(number)
result==>>
8
11
25




N = 4
number = 0
for i in range(N, N+10):
    number = i+1
    print(number)
result==>>
5
6
7
8
9
10
11
12
13
14

a = 3
2
3
7
product = 1
for i in range(a):
    number = int(input())
    product = product*number
print(product)
result==>>
42



a = 2
b = 3
for i in range(a):
    print("* "*b)
result==>>
* * * 
* * * 



a = 4
for i in range(1, a+1):
    print("* "*i)
result==>>
* 
* * 
* * * 
* * * * 




a = 3
8
11
25
sum = 0
for i in range(a):
    number = int(input())
    sum = sum + number
print(sum)
result==>>
44




a = "python"
len_of_a = len(a)
b = ""
for i in range(1, len_of_a):
    b = b + "-" + a[i]
c = a[0]    
print(c+b)




a = 4
number = 0
for i in range(a):
    number = str(i+1) * a
    print(number)
result==>>
1111
2222
3333
4444




M = 3
N = 4
for i in range (M):
    print("*"*N)
result==>>
****
****
****


N = 4
number = 0
for i in range (N):
    number = i+1
    print("*"*number)
result===>>
*
**
***
****




N = 6
number = 1
for i in range(1, N+1):
    print((str(number)+" ")*i)
    number = i+1
result==>>
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 


N = 4
number = 0
for i in range (1, N):
    print("* "*i)
    number = number+1
print("+ "*N)
Result==>> 
* 
* * 
* * * 
+ + + + 



N = 4
number = 1
for i in range(1, N+1):
    number = str(i)*i
    print(number)
for i in range(1, N+1):
    number = str(i)*i
    print(number)
result==>>
1
22
333
4444
1
22
333
4444 


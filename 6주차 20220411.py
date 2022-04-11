'''
전체 : ehllo
일부 : x가 가리키는 정보
'''
'''
import time

for x in "hello":
    #print(x)
    #타임모듈의 sleep()기능 실행
    time.sleep(1)
    print('단지 반복에 사용')
'''
#문제
'''
자신의 영문 이름을 입력받아
아래와 같이 출력되도록 프로그램
해봅시다.
입력 : mosungpil
출력 : m-o-s-u-n-g-p-i-l
'''
'''
name = input('영문이름입력:')

for x in name[0:-1]:
    print(x+"-", end= "")

print(name[-1])
'''
'''
import time
'''
#전체 : 리스트
'''
for a in [1,2,3,4,5]:
    print(a)
    time.sleep(1)
'''
#문제 #시험 문제
'''
리스트안에 들어있는 자연수 중에서
홀수의 갯수와, 짝수의 갯수를 출력하는
프로그램을 완성해 봅시다.
(짝수란 2로 나누었을때 나머지가 0이 되는 수를 말합니다.)
'''
#range(1,101)
#범위 표현하기
'''
for x in range(0,10,1):
    print(x)
'''
'''
#범위를 리스트로 바꾸기

a= list(range(0,10))
print(a)
for x in a:
    print(x)

print('a의 인덱스 3번 요소:',a[3])

'''

#구구단
'''
import time
for outN in range(4):
    for inN in range(6):
        print(f"{outN}x{inN}=")
        time.sleep(1)
'''
'''
1. 구구단의 결과가 출력되도록 위 코드를 수정해 봅시다.(3*4=12)

2. 아래와 같이 출력되는 구구단 프로그램을 해봅시다
1x1=1 | 2x1=2 | 3x1=3  | 
1x2=2 | 2x2=4 | 3x2=6  |
1x3=3 | 2x3=6 | 3x3=9  |
1x4=4 | 2x4=8 | 3x4=12 |
'''

#1번
'''
import time
for outN in range(4):
    for inN in range(6):
        print(f"{outN}x{inN}=",outN*inN)
        time.sleep(1)
'''

#2번
import time
for outN in range(1,4):
    
    for inN in range(5):
        
        print(f"{outN}x{inN}=",outN*inN,'|')

'''
2022_03_14
2주차 수업
'''
'''
print('hello');
print("hello");
#문자열로 나뉠땐 따움표, 쌍따움표 둘다 사용

print( "He' s name is 철수"  )
print( 'he said "I am ok!" ')
print( "He said \"I am OK!\"")
#따움표를 쓰고 싶을땐 문자열 나뉠때 쌍다움표, 쌍따움표를 쓰고싶으면 문자열 따움표
#그것도 귀찬다면 쓰고싶은 단어에 역슬러쉬 사용
'''

#print("a" *10)
#1개의 문자를 여러번 곱해서 쓸때

'''
print("=" *25)
print('He said "Python is Easy"')
print("34256곱하기2365는", 34256*2365, '입니다' )
#문자열과 숫자를 같이 쓸때에는 ,를 써서 구분 짓는다.
print("=" *25)
'''
'''
print("A")
print("B")
'''
'''
#\n은 new line을 의미
print("A\nBC\nDEF")
'''

#====문자열 슬라이싱(slice)=====
#print("Hello"[0])
#print("Hello"[1])
#print("Hello"[-1]) #-는 뒤에서부터 시작 
#print("Helo"[0:3]) #0<=범위 <3 까지 출력

'''
a=input() #a는 입력된 숫자를 가르킴
print(a) #a가 가리키는 것을 출력
'''

'''
b="2022년 3월 14일"
print(b)
'''

'''
b=input("오늘날짜입력:");
print(b[0:4])
print(b[4:6])
print(b[6:8])
#0:4 < 0부터시작 4미만 시작
'''
'''
b=input("태어난연도입력:");

#b가 문자열인지 숫자 인지 알아보기
#print( type(b) ) 

#나이 출력하기
#문자를 숫자로 바꿔줍니다.
print('당신의 한국나이는',2022-int(b)+1,'살 입니다')
print('만으로는', 2022-int(b),'살 입니다')
#시험문제 꼭 외울것
'''
'''
a= 1333; #a가 1333을 가리킴
a= 123; #a가 123을 가리킴

#a가 가리키는 것에 100을 더한 값을 a가 가리킴
a=a+100
print(a) #현재 a는 223을 가리킴, 그 값을 출력

a-=3; #a가 가리키는 값에서 3을 뺌, 그리고 그값 가리킴
a+=3; #a가 가리키는 값에 3을 더함, 그리고 그값 가리킴
'''
'''
b=100
#b가 가리키는 값을 4배함, 그리고 그 값 가리키기
b*=4;
'''

'''
a=100;
b=2;
c=2

print( a+b*c) #예상되는 결과값 : 104
print( (a+b)*c) #예상되는 결과값 : 204
'''

'''
#내가 푼거
a=input() 
b=input()
#괄호 안에 숫자를 입력 문자를 쓰고 싶으면 "" 넣으면됨

print(int(a)+int(b))
print(int(a)*int(b))
print(int(a)-int(b))
#int=숫자로 변환 시켜줌
'''

'''
a = int(input("첫번째 숫자 입력:"))
'''
'''
#위에것을 기입하여 푼것

a=int(input()) 
b=int(input())
print(a+b)
print(a*b)
print(a-b)
'''

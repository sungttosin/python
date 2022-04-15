''' 
a = "200" 

#a가 가리키는 자료의 종류를 출력 
print (type(a)) 
#a가 가리키는 자료를 정수로 변환후 
#a가 그 값을 가리킴 
a = int(a) 

#문자열 "3.14"를 실수숫자로 바꾼 후 
#b가 가리키도록 하는 코드 작성 
b = float("3.14"); 
print( type(b)) 
#정수 3을 실수로 바꾸면 어떻게 되 까요? 
c = float(3) print(c) 
#정수 3은 실수 3.0으로 바뀝니다 
''' 
''' 
BMI (body measure index) /체질량 지수 
bmi는 몸무게(kg)를 키(미터)의 제곱값으로 나눈 숫자 
''' 
#문제 
''' 
키와 몸무게를 입력으로 받아,
bmi값을 출력해주는 프로그램을 작성해 봅시다. 
a = float (input("키 cm")); 
b = float (input("몸무게 kg")); 
bmi = b/((a*0.01)**2) 
print (bmi) #print는 기본적으로 줄바꿈을 실행함
print("hello") 
print("python") 
#줄바꿈 하지 않을 경우 end를 활용합니다. 
print("hello",end=""); 
print("python"); 
#end 를 이용하여 끝에 문자 추가 가능 
print("hello", end=":"); 
print("python"); 
#콤마는 스페이스 키로 구분되어 출력됩니다. 
print("a","b","c") 
#sep는 구분 기호를 바꿀 수 있습니다 
print("010","1111","1234", sep="_") 
#문자열 format 지정하기 
#format의 의미는 형식 (구조 , 틀) 
#f는 이문자열이 형식을 갖춘 문자열 임을 의미 
print(f' I am {27}years old') 
#공간 10칸 확보하기,오른쪽 정렬 
print(f' I am {27:10}years old') 
#가운데 정렬하여 출력하기 
print(f' I am {27:^10}years old') 
#자리 확보할 때 비 공간을 특정 문자로 채우기 
print(f' I am {27:=^10}years old') 
#소수점 길이 지정하기(마지막 f는float을 의미) 
print(f' PI is {3.141592:=^10.2f}') 
#변수값을 형식에 맞춰 출력하기 
weight = 65 height = 177.5 
print(f"몸뭄게는 {weight:^10}kg, \ 키는 {height:^10.2f}cm 입나다") 
print(f"몸무게는 {weight:^10}kg, \ 키는 {height:^10.2f}cm 입니다") 
a = 10 b = 20 print (a, b) c, d = 30, 40 
print (c) print (d) 
#가리키는대상을 찾아 들어가보면 아무것도 없음 
e = None; 
a = 100; 
b = 200; 
print (a, b) 
#변수 e를 이용하여 a와 b가 가리키는 값을 서로 바꾸는 코드를 작성해 봅시다. 
''' 
#코드 작성 
a = 100; 
b = 200; 
e = b; 
b = a; 
a = e; 
print(a, b) 
#"객체" 이해하기 
''' 
일상생활속에서 존재하는 물건을 '사물' 소프트웨어 
속에서 존재하는 것을 '객체' 라고 부릅니다. 
'''
'''
인간이라는 사물은 age, name, weight와 같은 어떤 값을 갖고, 
eat(), run(), sleep() 와 같은 행동을 한다. 
즉, 사물이란는 것은 '값들'과 '행동들'로 규정하여 바라보겠다는 뜻이다. 
이때 행동과 관련된것 에는 ()를넣어준다. 
ex) eat(), run(), sleep() 
''' 
#자동차라는 것을 어떤 값과, 행동으로 정의해 봅시다.
#값:name, 탑승인원... 
#행동: 가속하기(), 감속하기(), 문열기()
...

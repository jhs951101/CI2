def Calculate(x,y):  #구구단 수행 함수
    swap=0
    if x>y:  #첫번째 숫자가 더 클 경우 Swapping (입력 순서 자유)
        swap=x
        x=y
        y=swap
    
    i=1  #i: 구구단을 수행하기 위한 변수(1~9)
    while x<=y:  #구구단을 수행하는 부분
        while i<=9:
            print(x," * ",i," = ",x*i)
            i=i+1
        x=x+1
        i=1


print("어서오거라!! 구구단 출력 프로그램이다...")  #프로그램 시작을 알림

one=1  #one, two: 입력받을 두 정수
two=1  #처음에는 one과 two를 1로 해줘야 프로그램이 진행됨
while one>0 and two>0:  #두 수가 양수일 동안 수행
    a = input("첫 번째 숫자를 입력하거라... : ")
    one = int(a)
    b = input("두 번째 숫자를 입력하거라... : ")
    two = int(b)  #숫자 입력 받기
    
    if one>0 and two>0:
        Calculate(one,two)  #구구단 수행

print("프로그램이 종료되었다...")  
print("수고했다!! 어서 가보거라...")  #음수 입력 시 출력 후 프로그램 종료
print ('hello world')

# 함수를 만들어 봅시다 함수는 def
def hello():
    print('함수 안에서 헬로 월드')

def hello2(msg):
    print('받은 메시지를 함수 안에서 출력')
    print(f'받은 메시지: {msg}')
    # {}  중괄호 안에는 변수를 넣을 수 있음 : 앞에 f 붙였을 때

# 출력하지 않고 값만 출력할 때는 return 을 씀 ^^^^^ 는 해당 위치에서 오류가 났다는 뜻

def add(num1, num2):
    print(num1 + num2)

def add2(num1, num2):
    return(num1 + num2)

# 함수를 불러야 함수 안에 있는 것이 나옴 : 함수를 불러서 사용
hello()
hello2('눈이 아프다')
hello2(2)
add(5, 3)
# return으로 던진 값을 임시로 저장 result
result = add2(5, 8)
hello2(result)
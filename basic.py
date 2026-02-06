# print("hello world") 

# 파이썬은 코드를 위에서부터 아래로 읽는다

# a=2
# b=3
# c=a+bs
# print(c)
# 이런 코드를 작성했다고 했을 때, c는 5가 될 것이지만
# 만약 c 변수 다음에 a와 b의 값을 변경해도, 파이썬의 코드 처리 순서 때문에 c는 여전히 5로 출력이 된다.
# snake case를 써야 댐 ex. my_age (myAge는 camel case, js에서 많이 씀)

# 변수 
# my_name = "ye eun"
# print(my_name)
# dead = True 

# 변수가 필요한 이유: 
# 1. 프로그램에 데이터를 넣으려고 
# 2. 인간이 이해할 수 있는 이름으로 데이터에 접근하려고

# my_name = "ye eun"
# age= 22
# dead = False
# print("hello my name is ", my_name)
# print("and i'm", age, " years old")


# functions
# 코드를 재사용할 수 있게 해 줌

# def say_hello(): 
#     print("hello how r u?")

# def say_bye():
#     print("bye")
    
# say_hello()

# def == define, 즉 함수를 정의하다라는 뜻이 됨 functions도 기능, 작동하다의 뜻을 가짐
# 함수를 호출하려면 함수 이름 뒤에 괄호를 붙여야 함
# 파이썬에서는 공백이 아주 중요함. 들여써 줘야 어떤 것 안에 들어가있는 코드라는 걸 파이썬이 알아차릴 수 있음
# 다른 언어들이 중괄호로 하는 것들을 파이썬에서는 공백으로 처리함

# def say_hello(user_name, user_age): #say_hello가 값을 받음, 이를 파라미터
#     print("hello", user_name)
#     print("you are", user_age, "years old")
    
# say_hello("yeeun", 22) #얘는 argument


# def tax_calculator(money):
#     print (money * 0.35)
    
# tax_calculator(15000000000)

# def say_hello(user_name="anonymous"): #user_name에 기본값 넣기
#     print("hello", user_name)
    
# say_hello("yeeun")
# say_hello()

# def plus(a=0, b=0):
#     print(a+b)
    
# def minus(a=0, b=0):
#     print(a-b)
    
# def multiplication(a=0, b=0):
#     print(a*b)
    
# def division(a=0, b=1):
#     print(a/b)
    
# def power(a=0, b=0):
#     print(a**b)
    
# plus(3, 4)
# minus(3, 4)
# multiplication(3, 4)
# division()
# power(3, 4)


# return

# def tax_calculator(money):
#     return money * 0.35
    
# def pay_tax(tax):
#     print("thank you for paying", tax)
    
# pay_tax(tax_calculator(15000000000))

# 함수 바깥으로 값을 저장하고 싶을 때 사용하는 것이 return
# return은 함수를 끝내버린다


# my_name = "yeeun"
# my_age= 22
# my_color_eyes="brown"

# print(f"hello im {my_name}, 
# i have {my_age} years in the earth, {my_color_eyes} is my eye color")
# f == format, 변수와 문자열을 같이 사용할 수 있다

def make_juice(fruit):
    return f"{fruit}+cup..."

def add_ice(juice):
    return f"{juice}+ice"

def add_sugar(iced_juice):
    return f"{iced_juice}+sugar"

juice = make_juice("apple")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)




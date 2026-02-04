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

def say_hello(): 
    print("hello how r u?")

def say_bye():
    print("bye")
    
say_hello()

# def == define, 즉 함수를 정의하다라는 뜻이 됨 functions도 기능, 작동하다의 뜻을 가짐
# 함수를 호출하려면 함수 이름 뒤에 괄호를 붙여야 함
# 파이썬에서는 공백이 아주 중요함. 들여써 줘야 어떤 것 안에 들어가있는 코드라는 걸 파이썬이 알아차릴 수 있음
# 다른 언어들이 중괄호로 하는 것들을 파이썬에서는 공백으로 처리함


# 키워드 def는 함수 정의를 시작합니다. 함수 이름과 괄호로 싸인 형식 매개변수들의 목록이 뒤따릅니다. 함수의 바디를 형성하는 문장들이 다음 줄에서 시작되고, 반드시 들여쓰기 되어야 합니다
# 함수 바디의 첫 번째 문장은 선택적으로 문자열 리터럴이 될 수 있습니다; 이 문자열 리터럴은 함수의 도큐멘테이션 문자열, 즉 독스트링 (docstring) 입니다.
# * 독스트링(docstring)은 함수 시작 부분에서 함수 인터페이스를 설명하는 문자열 *
# 작성하는 코드에 독스트링을 첨부하는 것은 좋은 관습입니다, 그러니 버릇을 들이는 것이 좋습니다
# 파이썬의 함수는 return 문은 함수로부터 값을 갖고 복귀하게 만듭니다. 표현식 인자 없는 return 은 None을 돌려줍니다.


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# fib(2000)

# 자바스크립트처럼 함수 인자값의 기본값을 '='로 설정할 수 있다.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        # in을 통해 if문의 조건을 나열할 수 있다.
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            # 자바스크립트의 throw와 비슷한 개념
            raise ValueError('invalid user response')
        print(reminder)

# user_ask_response = ask_ok("Do you want to continue? (y/n): ")
# if user_ask_response:
#     print("You chose to continue.")
# else:
#     print("You chose to stop.")

# L의 기본값으로 설정된 빈 배열은 함수를 호출할 때마다 공유된다. 여러번 호출한 경우 L의 아이템이 여러개가 된다.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# 만약 기본값이 공유되는걸 원치 않는다면 아래처럼 함수를 선언해야 한다.
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
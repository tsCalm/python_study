
"""
"패킹(packing)"과 "언패킹(unpacking)"은 파이썬에서 시퀀스(리스트, 튜플 등)의 요소들을 다루는 과정을 가리키는 용어입니다.

패킹(Packing): 여러 개의 값을 하나의 변수에 묶어서 할당하는 과정을 말합니다. 예를 들어, 튜플은 여러 개의 값을 하나의 튜플로 묶어서 선언할 수 있습니다.

python
Copy code
point = 3, 5  # 튜플 패킹
위의 코드에서 3과 5는 패킹되어 (3, 5)라는 튜플로 할당됩니다.

언패킹(Unpacking): 패킹된 변수나 시퀀스의 요소들을 개별 변수로 분리하는 과정을 말합니다. 예를 들어, 튜플의 값을 개별 변수로 할당하거나 리스트의 요소를 개별 변수에 할당할 때 언패킹을 사용합니다.

python
Copy code
x, y = point  # 언패킹
위의 코드에서 point는 (3, 5)로 패킹된 튜플이며, x와 y에 대해 언패킹되어 각각 3과 5로 할당됩니다.

언패킹은 패킹된 시퀀스의 요소들을 개별적으로 접근하거나 변수들 간의 값을 교환하는 등의 다양한 상황에서 유용하게 사용됩니다.
"""


def http_error(status):
  match status:
      case 400:
          return "Bad request"
      case 404:
          return "Not found"
      case 418:
          return "I'm a teapot"
      #the “variable name” _ acts as a wildcard and never fails to match
      case _:
          return "Something's wrong with the internet"


# http_status_result = http_error(400)
# print(http_status_result)

"""
일반적으로 알고 있는 switch case문과 유사하다.
편리하다고 느낀점은 _를 활용하여 생각하지 못한 case까지 쉽게 컨트롤할 수 있는 점이다.
"""

class Point:
  def __init__(self, x: int, y: int):
      self.x = x
      self.y = y

def where_is(point):
  match point:
    # 파이썬은 case문에 아래처럼 if문으로 guard를 걸 수 있다.
    case Point(x=x, y=y) if x == y:
        print(f"Y=X at {x}")
    case Point(x=0, y=y):
        print(f"Y={y}")
    case Point(x=x, y=0):
        print(f"X={x}")
    case Point():
        print("Somewhere else")
    case _:
        print("Not a point")

# 예제 실행
p1 = Point(0, 0)
p2 = Point(0, 5)
p3 = Point(10, 0)
p4 = Point(2, 3)
p5 = "Not a point"

where_is(p1)  # Origin
where_is(p2)  # Y=5
where_is(p3)  # X=10
where_is(p4)  # Somewhere else
where_is(p5)  # Not a point
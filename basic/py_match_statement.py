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


temp = http_error(400)
print(temp)

"""
일반적으로 알고 있는 switch case문과 유사하다.
편리하다고 느낀점은 _를 활용하여 생각하지 못한 case까지 쉽게 컨트롤할 수 있는 점이다.
"""
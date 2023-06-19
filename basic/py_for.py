words = ['cat', 'window', 'defenestrate']

for w in words:
  print(w, len(w))

  """
  len() : 문자열 길이를 리턴해주는 함수
  """

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
temp= users.copy()
for user, status in users.copy().items():
  if status == 'inactive':
      del users[user]

print(users, temp)

"""
copy() : 오브젝트를 복사
items() : 오브젝트의 프로퍼티값을 리턴
users대신 users.copy()를 사용한 이유는 for문에서 users 오브젝트의 프로퍼티를 제거하고 있다.
이 경우 반복문이의 예기치 못한 오류가 발생할 확률이 있기 때문에 users 오브젝트의 초기값을 복사해서 반복문을 돌리고 원본 users 오브젝트를 변경한다.
"""


active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# print(users.copy().items() == users) True , 내부값이 완전히 같은 경우 True, js의 경우 참조타입은 주소값으로 비교하는데 파이썬은 그렇지 않은 것으로 추정된다.
# print(users.copy() == active_users) => False

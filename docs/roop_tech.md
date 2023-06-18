## enumerate

```
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```

자바스크립트의 Object.entries()와 유사하다.
키,벨류로 이뤄진 튜플 리스트를 리턴한다.

## zip(배열, 배열)

```
questions = ['name', 'quest', 'favorite color','abc']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
```

첫 인자로 들어간 배열의 값이 q값이된다.
길이가 더 짧은 배열을 기준으로 print 함수가 실행된다.

## reversed(배열)

```
for i in reversed(range(1, 10, 2)):
    print(i)
```

배열 요소의 순서를 거꾸로 뒤집는다.

## sorted(배열)

```
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
```

배열의 요소를 순서대로 정렬한다.

## set(배열)

```
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
```

배열 요소의 중복을 제거한다.

## 배열 요소에서 원하는 값만 추출하여 새로운 배열 만들기

```
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
```

자바스크립트의 !와 파이썬의 not은 거의 유사한것으로 추정
math.isnan는 자바스크립트의 Math.isNan과 유사한것으로 추정

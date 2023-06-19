for i in range(5):
  print(i)


"""
시퀀스(Sequence)는 값들의 순서가 정해진 모음을 의미합니다. 시퀀스는 문자열, 리스트, 튜플 등과 같은 데이터 타입을 말합니다. 
시퀀스는 각 요소가 순서대로 나열되어 있으며, 각 요소에는 인덱스가 할당되어 있어 특정 위치에 있는 요소를 참조할 수 있습니다.

이터레이트(Iterate)는 반복적으로 실행되는 작업을 의미합니다. 
예를 들어, 반복문을 사용하여 시퀀스의 각 요소에 접근하고 처리하는 것은 이터레이션 작업입니다. 
이터레이션은 시퀀스의 첫 번째 요소부터 마지막 요소까지 순차적으로 진행됩니다.

위 예제에서 range(5)는 0부터 4까지의 숫자 시퀀스를 생성합니다. 
for 문을 사용하여 이 시퀀스를 이터레이트하면, i 변수에는 각 숫자가 순차적으로 할당되고 print(i) 문장이 실행됩니다. 
따라서 위 예제는 0부터 4까지의 숫자를 출력하는 것입니다.
"""

list_val_1= list(range(5, 10)) #[5, 6, 7, 8, 9]

list_val_2= list(range(0, 10, 3)) #[0, 3, 6, 9]

list_val_3= list(range(-10, -100, -30)) #[-10, -40, -70]


"""
range(5) : 5보다 작은 수열
range(5, 10) : 5보다 크고 10보다 수열
range(0, 10, 3) : 0에서 시작 +3씩 더한 값들 중 10보다 작은 값

보통 range함수의 3번째 파라메터를 step이라고 부른다.
"""

chars = ['Mary', 'had', 'a', 'little', 'lamb']
for char in range(len(chars)):
  print(char, chars[char])

for idx, val in enumerate(chars):
  print(idx, val)


# range(len(chars))를 사용하는 대신 일반적으로 enumerate()많이 사용한다. 자바스크립트의 Object.entries()와 유사한 기능인 키,벨류를 갖는 튜플 리스트를 리턴한다.

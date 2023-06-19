val_squares = [1, 4, 9, 16, 25]
print(val_squares)
print(val_squares[0]) # 배열의 첫번째 요소
print(val_squares[-1]) # 배열의 마지막 요소
print(val_squares[-3:]) # 끝에서 3번째 요소부터 마지막

val_clone_squares = val_squares[:] # 배열의 요소 값이 완전히 같은 새로운 배열을 반환

val_squares.append(113)

# val_squares 배열에 113을 추가했지만 val_clone_squares 배열에는 113이 추가되지 않는다.
print(val_clone_squares)

val_list_concat = val_squares + [36, 49, 64, 81, 100] # 자바스크립트 concat과 유사
print(val_list_concat)

val_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
val_letters[2:5] = ['C', 'D', 'E']
# now remove them
val_letters[2:5] = []
# clear the list by replacing all the elements with an empty list
val_letters[:] = []

print(val_letters)
print(len(val_letters))

val_a = ['a', 'b', 'c']
val_n = [1, 2, 3]
val_x = [val_a, val_n] # 중첩배열

print(val_x[0][1]) # 중첩배열의 첫 배열, 두번째 요소 리턴

# escape
val_string= 'spam eggs'  # return 'spam eggs'
val_string_escape= 'doesn\'t'  # return "doesn't"
val_double = "doesn't"  # return "doesn't"
val_single_double = '"Yes," they said.' # return '"Yes," they said.'
val_dobule_escape= "\"Yes,\" they said." # return '"Yes," they said.'

print(val_string)
print(val_string_escape)
print(val_double)
print(val_single_double)
print(val_dobule_escape)

"""
1. 싱글쿼터 문자열로 사용하고 싶은 경우 '\'를 싱글쿼터 앞에 삽입
2. 이스케이프를 사용하지 않고 싱글쿼터를 나타내고 싶은 경우 더블쿼터로 감싼 후 싱글쿼터 사용
3. 더블쿼터를 문자열로 사용하고 싶은 경우 싱글쿼터로 감싼 후 더블쿼터 사용
4. 더블쿼터 내에서 더블쿼터를 문자열로 사용하고 싶은 경우 '\'를 더블쿼터 앞에 삽입
"""

val_newline= 'C:\some\name' # \n의 경우 newline으로 인식하기 때문에 2줄로 출력된다.
val_raw_string ="" r'C:\some\name' # 문자열 앞에 r을 붙일 경우 '\n'을 문자로 인식한다.

print(val_newline)
print(val_raw_string)

# \문자를 붙이지 않으면 문자열 리터럴이 출력되기 전 newline이 생긴 후 출력된다.
print("""\
Usage: thingy -n [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

val_multiply= 3 * 'un' + 'ium' # 문자열을 사용한 곱셈 가능
print(val_multiply)

val_two_string= 'Py' 'thon' # 두 문자열을 나열하면 파이썬은 자동으로 문자열을 합친다.
print(val_two_string)

val_string_multi_line = (
  'Put several strings within parentheses '
  'to have them joined together.'
)
print(val_string_multi_line)

val_prefix = 'py'

# print(val_prefix 'thon') -> 변수에 담긴 문자열을 자동으로 병합하지 않는 변수와 문자열을 병합하고 싶은 경우 + 를 활용해야한다.

val_string_list = 'Python'

print(
  val_string_list[0], # 문자열의 첫번째 문자
  val_string_list[1], # 문자열의 두번째 문자
  val_string_list[-1], # 문자열의 마지막 문자
  val_string_list[-2] # 문자열의 마지막 전 문자
)

print(val_string_list[:2]) # 0 (included) to 2 (excluded)
print(val_string_list[2:5]) # 2 (included) to 5 (excluded) 
print(val_string_list[-2:]) # the second-last (included) to the end

val_string_const = 'test'
# 에러 -> 파이썬에서 문자열은 불변이다. 문자열을 바꾸고 싶은 경우 새로운 문자열을 생성해야한다.
#val_string_const[0] = 'T'
val_new_string_const = 'T' + val_string_const[1:]
print(val_new_string_const)

val_len = 'supercalifragilisticexpialidocious'
print(len(val_len)) # len() 문자열의 길이를 반환


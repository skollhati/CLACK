s1 = [4,99,2,6,7,13,88,76]
s2 = [6,88,13,4,99,2,7]
from collections import Counter
import re
s3 = 'abcdea'
s4 = 'cookoie'
s1_char_count = set(sorted(Counter(list(s3)).items()))
s2_char_count = set(sorted(Counter(list(s4)).items()))
t = [1,2]



from collections import Counter
import re

def char_count_check(s1,s2):
    s1_char_count = list(Counter(list(s1)).items())
    s2_char_count = list(Counter(list(s2)).items())
    for idx,count_item in enumerate(s1_char_count):
        try:
            if s2_char_count[idx][0] != count_item[0]:
                return False
            if s2_char_count[idx][1] < count_item[1]:
                return False
        except IndexError as e:
            return False
    return True

def find_match(s2):
    for idx,char in enumerate(s2):
        tmp_idx = idx
        for sub_i in range(idx+1, len(s2)) :
            if char == s2[sub_i]:
                if(sub_i - tmp_idx) == 1:
                    tmp_idx = sub_i
                else:
                    return False
            else:
                break
    return True

def find_match2(s2):
    for idx,char in enumerate(s2):
        del_char = ''
        for sub_idx in range(idx+1,len(s2)):
            if s2[sub_idx] == char:
                if del_char != '':
                    return False
            else:
                del_char = char

    return True



def find_match3(s1,s2):
    tmp =list()
    a = 0
    for idx,char in enumerate(s1):
        if char in tmp:
            continue
        for sub_idx in range(idx+a,len(s2)):
            if s2[sub_idx] in tmp:
                return False
            if s2[sub_idx] != char:
                a=sub_idx-idx-1
                break
        tmp.append(char)
    return True


def solution(s1, s2):

    if char_count_check(s1, s2) and find_match3(s1,s2):
            return True
    else:
        return False

print(solution('cookie','coookieeo'))
import re

def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    A = {}
    B = {}

    set_A = set()
    set_B = set()

    for i in range(len(str1)-1):
        # 문자만 있는지 검사(현재 문자와 소문자를 제외한 문자가 같은지 비교)
        if str1[i:i+2] == re.sub(r"[^a-z]","",str1[i:i+2]):
            # 집합 만들기 + 딕셔너리에 중복 표시하기
            A.setdefault(str1[i:i+2], 0)
            A[str1[i:i+2]] += 1
            set_A.add(str1[i:i+2])

    for i in range(len(str2)-1):
        if str2[i:i+2] == re.sub(r"[^a-z]","",str2[i:i+2]):
            B.setdefault(str2[i:i+2], 0)
            B[str2[i:i+2]] += 1
            set_B.add(str2[i:i+2])

    # print(A,B)
    
    # 둘 다 공집합인 경우
    if len(A) == 0 and len(B) == 0: 
        return 65536

    # 교집합 합집합 구하기
    union = set(set_A | set_B)
    intersection = set(set_A & set_B)
    union_cnt = 0
    intersection_cnt = 0
    
    for x in union:
        # 합집합의 원소가 교집합에 없으면 원소가 있는 집합의 중복 수를 넣기
        if x not in A:
            union_cnt += B[x]
            continue
        if x not in B:
            union_cnt += A[x]
            continue
        # 합집합의 원소가 교집합에 있을 경우 둘 중 큰 중복 값 넣기
        union_cnt += max(A[x], B[x])
    for x in intersection:
        # 원소의 중복 값 중 작은 것 넣기
        intersection_cnt += min(A[x], B[x])


    return int((intersection_cnt/union_cnt) * 65536)
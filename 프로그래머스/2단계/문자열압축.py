def solution(s):
    len_s = len(s)
    # 나올 수 있는 길이들을 저장하는 리스트
    answer = []
    # 새로 만든 문자열
    result = ""
    
    if len_s == 1:
        return 1

    # 자를 수 있는 최대 단위는 문자열 길이의 반
    for n in range(1, len_s//2 + 1):
        # 문자열이 반복되는 개수
        cnt = 1
        # 현재 반복할 문자열
        prev = s[:n]

        for i in range(n, len_s, n):
            # 부분 문자열이 같으면 cnt 증가
            if prev == s[i:i+n]:
                cnt += 1
            else:
                # 부분 문자열 중복이 없었을 경우
                if cnt == 1:
                    cnt = ""
                
                result = result + str(cnt) + prev
                prev = s[i:i+n]
                cnt = 1

        # 마지막 문자열 처리
        if cnt == 1:
            cnt = ""
        result += str(cnt) + prev
        answer.append(len(result))
        result = ""
        
    return min(answer)

def solution(participant, completion):

    hash_dict = {}

    for i in participant:
        if i in hash_dict:
            hash_dict[i] += 1
        else:
            hash_dict[i] = 1
 
    for i in completion:
        hash_dict[i] -= 1

    result = dict(map(reversed, hash_dict.items()))
    return result[1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# lst = ['a', 'b', 'c', 'd']
# temp = {}

# for i in lst :
#     temp[i] = 1

# print(temp)

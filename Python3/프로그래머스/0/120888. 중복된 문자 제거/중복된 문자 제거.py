def solution(my_string):
    answer = []
    
    # 문자열을 한 글자씩 꺼내며 반복합니다.
    for char in my_string:
        # 만약 answer 리스트에 현재 글자가 없다면 (처음 등장한 글자라면)
        if char not in answer:
            answer.append(char) # 리스트에 추가합니다.
            
    # 리스트에 모인 글자들을 하나의 문자열로 합쳐서 반환합니다.
    return ''.join(answer)
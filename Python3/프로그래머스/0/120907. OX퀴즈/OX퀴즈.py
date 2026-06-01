def solution(quiz):
    answer = []
    
    for q in quiz:
        # 공백을 기준으로 수식을 분리합니다.
        # 예: "3 - 4 = -3" -> ['3', '-', '4', '=', '-3']
        parts = q.split()
        
        X = int(parts[0])
        op = parts[1]
        Y = int(parts[2])
        Z = int(parts[4]) # parts[3]은 '=' 기호입니다.
        
        # 연산자에 따라 실제 계산을 수행합니다.
        if op == '+':
            real_result = X + Y
        elif op == '-':
            real_result = X - Y
            
        # 실제 계산 결과와 수식의 결과(Z)를 비교합니다.
        if real_result == Z:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer
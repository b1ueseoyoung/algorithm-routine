def solution(id_pw, db):
    # id_pw를 통째로 db에서 찾았을 때 완벽히 일치하는 데이터가 있다면 바로 로그인!
    if id_pw in db:
        return "login"
        
    # 완벽히 일치하는 게 없다면, 아이디만이라도 일치하는 사람이 있는지 찾으러 갑니다.
    for member in db:
        if member[0] == id_pw[0]: # member[0]은 db의 아이디, id_pw[0]은 입력된 아이디
            return "wrong pw"     # 위에서 [아이디, pw] 통째로 일치하는건 걸렀으니, 여기 걸리면 비번만 틀린 것!
            
    # 위의 검사를 다 통과하고도 함수가 안 끝났다면 아이디조차 없는 것입니다.
    return "fail"
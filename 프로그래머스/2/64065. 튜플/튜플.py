# "{{20,111},{111}}"
# → ['20,111', '111']
def unpack(s):
    s = s[1:len(s) - 1]
    s = s.replace("},", "}|")
    s = s.replace("}", "")
    s = s.replace("{", "")
    s = s.split("|")
    return s

def solution(s):
    answer = []
    checkHash = {}
    
    # 길이로 오름차순 정렬 ['111', '20,111']
    s = sorted(unpack(s), key=len)

    for i in range(len(s)):
        for c in s[i].split(","):
            if c not in checkHash:
                checkHash[c] = True
                answer.append(int(c))
            
    return answer
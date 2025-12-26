MAX_N = 5

class Test:
    def __init__(self, code, score):
        self.code = code
        self.score = score
    
    def __str__(self):
        return f'{self.code} {self.score}'

test_scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    test_scores.append(Test(codename, int(score)))

test_scores.sort(key=lambda x: x.score)

print(test_scores[0])

```python
def solution(n, horizontal):
    answer = [[None for i in range(n)] for i in range(n)]
    # cur = (0, 0)
    stage = 1
    order = 1
    answer[0][0] = order

    while answer[n-1][0] is None or answer[0][n-1] is None:
        stage += 1

        for _ in range(2):
            
            for move in range(stage):
                if horizontal:
                    answer[stage][move] = order + 1
                else:
                    answer[move][stage] = order + 1
                order += 1

            horisontal = not horisontal
                    
                
                
```
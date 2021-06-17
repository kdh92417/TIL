# Time Conversion

- https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

## Solve

```python
def timeConversion(s):
    # Write your code here
    time_type = s[-2:]
    hour = int(s[:2])
    
    if time_type == "AM":
        hour = (hour + 12) % 12
    elif time_type == "PM":
        if hour != 12:    
            hour = hour + 12
    return str(hour).zfill(2) + s[2:-2]
```

- 리스트 슬라이싱을 이용하여 AM / PM을 구분하여 계산하였다.
- `zfill()` 내장함수를 이용하여 0을 채웠다.
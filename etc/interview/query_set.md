# 쿼리셋 문제

주어진 모델에서 아버지가 `고길동` 이고 아들의 나이가 10살 이상인 객체를 조회하는 쿼리셋을 작성하는 문제

<br>

## 모델

```python
# models.py
from django.db import models

class Father(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fathers'

class Children(models.Model):
    father = models.ForeignKey(Father, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age  = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'children'
```

의 모델일 때, 아버지의 이름이 `고길동` 이고 아이의 나이가 10살 이상인 객체를 조회하는 쿼리셋

<br>

## 쿼리셋

```python
# 첫번째 방법 : Q를 이용한 방법 
ch = Children.objects.filter(Q(father__name="고길동") & Q(age__gt=10))

# 두번쨰 방법 : select_related를 이용한 방법
ch = Children.objects.select_related('father').filter(Q(father__name="고길동") & Q(age__gt=10))

# 세번째 방법 : prefetch_related를 이용한 방법
ch = Father.objects.prefetch_related('children_set').filter(name='고길동')
ch[0].children_set.filter(age__gt=10)
```

첫번째 두번째는 SQL문이 똑같다.

```sql
SELECT `children`.`id`, `children`.`father_id`, `children`.`name`, `children`.`age` 
FROM `children` 
INNER JOIN `fathers`
ON (`children`.`father_id` = `fathers`.`id`) 
WHERE (`fathers`.`name` = 고길동 AND `children`.`age` > 10)
```

prefetch_related문은 두번의 쿼리를 날리기 떄문에 성능이 좋지않다.

```sql
SELECT `fathers`.`id`, `fathers`.`name` 
FROM `fathers` 
WHERE `fathers`.`name` = 고길동

SELECT `children`.`id`, `children`.`father_id`, `children`.`name`, `children`.`age` 
FROM `children` 
WHERE (`children`.`father_id` = 1 AND `children`.`age` > 10)
```
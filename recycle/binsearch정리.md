# binsearch

> 정렬되어 있는 n개의 원소 중 특정 값을 O(log n) 시간에 찾는 알고리즘

## lower_bound - binsearch의 응용
> 정럴된 n개의 원소 중 특정 값 ***이상***이 처음 나타나는 위치를 찾는다

## upper_bound - binsearch의 응용
> 정렬된 n개의 원소 중 특정 값보다 ***큰*** 값이 처음 나타나는 위치를 찾는다

<br>
<br>

```python
def lower_bound(nums, target):
    
    a, b = 0, len(nums)
    
    while a < b:  #left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = (a + b) // 2
        
        if nums[mid] < target:
            a = mid + 1
        else:
            b = mid
    
    return b
```

```python
def upper_bound(nums, target):

    a, b = 0, len(nums)

    while a < b:  #left와 right가 만나는 지점이 target값 보다 큰 값이 처음 나오는 위치
        mid = (a + b) // 2

        if nums[mid] <= target:
            a = mid + 1
        else:
            b = mid 

    return b
```
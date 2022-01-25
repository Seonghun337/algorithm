n = int(input())

#n의 소인수 구하는 시간복잡도 = O(n)
#O(n^2)

cnt2 = 0
cnt5 = 0

for i in range(2,n+1):
    tmp = i
    cnt = 0
    while tmp % 2 == 0:
        tmp = tmp // 2
        cnt = cnt + 1
    cnt2 = cnt2 + cnt

    tmp = i
    cnt = 0
    while tmp % 5 == 0:
        tmp = tmp // 5
        cnt = cnt + 1
    cnt5 = cnt5 + cnt
    
print(min(cnt2,cnt5))
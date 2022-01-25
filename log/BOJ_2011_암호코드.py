while 1:
    nums = list(input())
    n = len(nums)

    dp = [1 for _ in range(n)]
    prev_cnt = 1
    cnt = 1

    if n == 0 or nums[0] == '0':
        print(0)
    else:
        dp[0] = 1
        for i in range(1,n):
            # print(dp,nums)
            if nums[i] == '0' and not (nums[i-1] == '1' or nums[i-1] == '2'):
                if nums[i-2] in ['1','2']:
                    dp[i] = dp[i-1] - dp[i-2]
                    dp[i-1] = dp[i-1] - dp[i-2]
                    continue
                else:
                    print(0)
                    break
            elif nums[i] == '0' and i>1 and nums[i-2] in ['1','2']:
                dp[i] = dp[i-2]
                dp[i-1] = dp[i-2]
                continue
            elif nums[i] == '0':
                dp[i] = dp[i-1]
                continue

            num_2 = int(nums[i-1] + nums[i])
            if 10 <= num_2 <= 26 and not (num_2 == 10 or num_2 == 20):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        else:
            # print(dp)
            print(dp[-1] % 1000000) 

    # 25는 2,5 25로 해석 가능
    # 251은 25해석과 동일 횟수
    # 2511은 25로 만들수 있는거 * 1,1 11
    # 25114는 2511로 만들수 있는거 + 251로 만들 수 있는거
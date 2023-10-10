from collections import defaultdict
def coupon_code(coupon: str, k: int):

    cnt = defaultdict(lambda :0)
    sum = 0
    i = 0
    j = k
    w = coupon[i:j]
    max_sum = sum
    while j <= len(coupon):
        if i == 0:
            for c in w:
                cnt[c] += 1
            for c, v in cnt.items():
                sum += (ord(c) - ord('a') + 1) ** v

        else:
            added = coupon[j-1]
            removed = coupon[i-1]
            sum_added = (ord(added) - ord('a') + 1) ** (cnt[added]+1) - (ord(added) - ord('a') + 1) ** (cnt[added])
            cnt[added] += 1
            sum_removed = (ord(removed) - ord('a') + 1) ** (cnt[removed]-1) - (ord(removed) - ord('a') + 1) ** (cnt[removed])
            cnt[removed] -= 1
            sum += sum_added + sum_removed

        i+= 1
        j+= 1
        print(sum)
        print(cnt)
        max_sum = max(max_sum, sum)
    return max_sum
    # return 0

# print(ord('a')-ord('a'))

if __name__ == '__main__':
    res = coupon_code('bcaa', 3)
    print(res)
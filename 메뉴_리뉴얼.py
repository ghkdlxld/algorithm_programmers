from itertools import combinations

def solution(orders, course):
    def make_course(num):
        course_lst = []
        for order in orders:
            course_lst.append(list(combinations(order, num)))

        cnt = {}
        for menus in course_lst:
            for menu in menus:
                menu = tuple(sorted(menu))
                try:
                    cnt[menu] += 1
                except:
                    cnt[menu] = 1
        cnt = sorted(cnt.items(), key=lambda item: item[1], reverse=True)

        big = []
        for idx in range(len(cnt)-1):
            if cnt[idx][1] > 1:
                big.append(''.join(cnt[idx][0]))
            if cnt[idx][1] != cnt[idx+1][1]:
                break

        return big

    ans = []
    for c in course:
        x = make_course(c)
        ans.extend(x)

    return sorted(ans)

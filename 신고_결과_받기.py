def solution(id_list, report, k):
    def mail(to):
        for i in range(len(id_list)):
            if link[to][i] == 1:
                ans[i] += 1

    ans = [0] * len(id_list)
    link = [[0] * len(id_list) for _ in range(len(id_list))]
    for ppl in report:
        link[id_list.index(ppl.split()[1])][id_list.index(ppl.split()[0])] = 1  # to from
    for i in range(len(id_list)):
        if sum(link[i]) >= k:
            mail(i)
    return ans
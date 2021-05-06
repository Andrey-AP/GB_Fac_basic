ls = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_ls = [ls[ind] for ind in range(len(ls)) if not (ls[ind] in ls[:ind-1]) and not (ls[ind] in ls[ind+1:])]
print(res_ls)

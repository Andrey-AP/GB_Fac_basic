# n = 5159
# # st_num = str(n)
# # ls = list(st_num)
# # ls.sort(reverse=True)
# st_num = int(''.join(sorted(str(n),reverse=True)))
# print(st_num)

# __________________________________Задачка про членов клуба__________________________________________

# ls = [(45, 12), (55, 21), (19, -2), (104, 20)]
# res_ls = []
# # for elem in ls:
# #     res_ls.append('Senior' if elem[0] >= 55 and elem[1] > 7 else 'Open')
#
#
# res_ls = ['Senior' if elem[0] >= 55 and elem[1] > 7 else 'Open' for elem in ls]
# print(res_ls)
# _____________________________________________________________________________________________________

# -------------------------------------Сумма 2-х минимальных-----------------------
# ls = [5, 8, 12, 18, 22]
#
# return sum(sorted(numbers)[:2])
#
#
# print(ls[-1].sort(reverse=True)+ls.sort(reverse=True)[-2])

# --------------------------------------------------------------------------
# st1="aretheyhere"
# st2="yestheyarehere"
# st3=set(st1+st2)
# print(''.join(sorted(set(st1+st2))))

# ---------------------Camel Case-----------------------------------------------
# st1 = "the-stealth-warrior"
# st=st1.replace('-','_')
# ls = st.split('_')
# out_st = str(ls[0])
# for i in range(1, len(ls)):
#     out_st = out_st + str(ls[i]).capitalize()

# ------------------------------------------------------------------------------------------------

# integer = 55
# res_ls = [i for i in range(2, integer//2+1) if integer % i == 0]
# print(res_ls if len(res_ls) else f'{integer} is prime')
# ---------------------------------------------------------------------------------------------
# x = 26
# print(26 ** 0.5)
# print(x ** 0.5 % 1)
# print(int(abs(x ** 0.5) % 1 * 100))
#-----------------------------разложить список по шаблону (xxx) xxx-xxxx ------------------------------
# n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(f'{n[1]}{n[2]}')
# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
#-----------------------------------------------------------------------------------------
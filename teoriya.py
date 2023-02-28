# user_list = [1, 2, 3, 5, 8, 15, 23, 38]

# Старый способ как бы я сделал

# result_list = list()
# for i in user_list:
#     if i % 2 == 0:
#         result_list.append((i, i**2))
#
# print(result_list)


# Но мы теперь изучили lambda выражения

# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# res = select(int, user_list)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)


# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)


# data = '15 156 96 3 5 8 34 34'
# print(data)
#
# # data = data.split()
# # print(data)
#
# data = list(map(int, data.split()))
# print(data)










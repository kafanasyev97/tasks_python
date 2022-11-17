def is_prime(number):
    if number == 0 or number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

def need_func(total):
    if isinstance(total, dict):
        total = total.items()
    return [value for index, value in enumerate(total) if is_prime(index)]


# Этот код другого человека, сохраню на всякий случай для себя

# def is_prime(i_num):
#     k = 0
#     for i in range(2, i_num // 2 + 1):
#         if i_num % i == 0:
#             k = k + 1
#     if k == 0:
#         return True
#     else:
#         return False
#
# def crypto(checking_list):
#     return [v for i, v in enumerate(checking_list) if i >= 2 and is_prime(i)]
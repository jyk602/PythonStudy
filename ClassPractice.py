'''
# 10/30
yk_list = []
for i in range(1, 12):
    # print(i)
    yk_list.append(i+2)
print('1st', yk_list)
# ----------------------
yk_list2 = range(1, 11)
print('2nd', list(yk_list2))
# ----------------------
yk_list3 = []
for i in range(1, 11):
    # print(i)
    if i % 2 == 1:
        yk_list3.append(i)
    else:
        continue
print('3rd', yk_list3)
# ----------------------
for i in yk_list3:
    print(i)
# ----------------------
yk_dict = {}
for i, v in enumerate(yk_list2):
    key = i + 1
    value = v + 1
    # print('key, value', key, value)
    yk_dict[key] = value
print('yk_dict: ', yk_dict)
print('len(yk_dict): ', len(yk_dict))
for k, v in yk_dict.items():
    print('yk_dict.items(): ', k, v)


print(__name__)
'''
'''
# ----------------------
yk_listfor = []
for i in range(1,11):
    yk_listfor.append(i)
print('yk_list4 for : ', yk_listfor)
# ----------------------
yk_listfor = []
yk_listfor2 = []
for i in range(1,11):
    if i % 2 == 0 :
        yk_listfor.append(i)
    else :
        yk_listfor2.append(i)
print('yk_list4 for even : ', yk_listfor)
print('yk_list4 for odd : ', yk_listfor2)

# ----------------------
yk_listwhile = []
x = 1
while x < 11:
    yk_listwhile.append(x)
    x += 1
print('yk_list4 while : ', yk_listwhile)
'''
# ----------------------
# yk_dict = {} # key : int, value = int
# for i in range(1,11):
#     key = i + 100
#     value = i
#     yk_dict[key] = value
#
# print('yk_dict', yk_dict)
#
# for f,v in yk_dict.items():
#     print('key: ', f, ' value :', v)
# ----------------------

def yk_createdict(x):
    yk_dict2 = {}  # key : int, value = int

    for i in range(x):
        key = i + 100
        value = i + 1
        yk_dict2[key] = value

    print('yk_dict2', yk_dict2)
    return yk_dict2


yk_createdict(5000)

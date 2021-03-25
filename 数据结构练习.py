# -*- coding: utf-8 -*-
import copy

demo1_list = [{"key": 1}, {"key": 2}, {"key": 3}]
demo2_list = [{"key": 3}, {"key": 44}, {"key": 3}, {"key": 4}]
# 期望值:[{'key': 1}, {'key': 2}, {'key': 44}, {'key': 3}, {'key': 4}]
demo3_list = []
for item in demo1_list:
    if item not in demo2_list:
        demo3_list.append(item)
    else:
        demo2_list.pop(demo2_list.index(item))
demo3_list.extend(demo2_list)
print(demo3_list)

demo4_list = [{"key": 1}, {"key": 2}, {"key": 3}, {"key": 3}, {"key": 13}]
demo5_list = [{"key": 3}, {"key": 44}, {"key": 3}, {"key": 3}, {"key": 4}, {"key": 13}]
# 期望值：[{'key': 1}, {'key': 2}, {'key': 3}, {'key': 44}, {'key': 4}]
out_list = []
demo5_list.reverse()
for i in demo4_list:
    if i not in demo5_list:
        out_list.append(i)
    else:
        demo5_list.remove(i)
demo5_list.reverse()
out_list.extend(demo5_list)
print(out_list)

demo10_list = {"key1": 123, "key2": 555, "key4": 4, "aa1": 13, "key11": 3131}
demo11_list = {"key1": 1234, "key2": 3, "key3": 4, "key5": 555, "key15": 555}
# 期望值out_dict={"key1":123,"key2":3,"key3":4,"key5":555,"key11":3131,"key15":555}
def sort_data(key_name):
    return int(key_name.split("key")[1])

tmp_dict={}
for use_dict in [demo10_list,demo11_list]:
    for key,value in use_dict.items():
        if not key.startswith("key") or not key.split("key")[1].isdecimal():
            continue
        if key not in tmp_dict.keys():
            tmp_dict[key]=value
            continue
        if tmp_dict[key]>value:
            tmp_dict[key]=value
out_list={key:tmp_dict[key] for key in sorted(tmp_dict,key=sort_data)}
print(out_list)

demo7_list = [1,3,4,5,"a","31",{"666":"31"},{3:3}]
demo8_list = [1,3,4,5,"cc","555"]
# 期望值[1,3,4,5,31,555,666]
demo7_list.extend(demo8_list)
tmp_list=[]
for item in demo7_list:
    if isinstance(item,int):
        tmp_list.append(item)
    elif isinstance(item,str) and item.isdecimal():
        tmp_list.append(int(item))
    elif isinstance(item,dict):
        for key in item.keys():
            if isinstance(key,int):
                tmp_list.append(key)
            elif isinstance(key,str) and key.isdecimal():
                tmp_list.append(int(key))
demo_set=set(tmp_list)
print(sorted(demo_set))


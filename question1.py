string=input().split()       #green apple is good for health
updated_list=[]
for each_item in string:
    if each_item.startswith('a'):
        updated_list.append("****")
    else:
        updated_list.append(each_item)
print(' '.join(updated_list))

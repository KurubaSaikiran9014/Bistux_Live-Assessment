input_string=input().split()    #this is a sample string for test
first_letters=[]
for each in input_string:
    first_letters.append(each[0])
updated_list=[]
for each_letter in sorted(set(first_letters)):
    sub_list=[]
    for each_item in input_string:
        if each_item[0]==each_letter:
            sub_list.append(each_item)
    print(sub_list)

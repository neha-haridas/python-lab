list1=[2,3,4]
list2=[1,3,5]
j=[x for x in list1 if x in list2]
if j != 0:
    print("same elements are",j)
else:
    print("no same elements ")
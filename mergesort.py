#merge sort
def sort_lists(list1,list2):
    newlist=[]
    while True:
        if list1==[]:
            newlist.extend(list2)
            break
        if list2==[]:
            newlist.extend(list1)
            break
        if list1[0]<list2[0]:
            newlist.append(list1.pop(0))
        else:
            newlist.append(list2.pop(0))
    return newlist
#returns nested new list - expect to get nested list only
def mergelist(lst):
    newlist=[]
    while True:
        if lst==[]:
            return newlist
        list1=lst.pop(0)
        if lst==[]:
            list2=[]
        else:
            list2=lst.pop(0)
        newlist.append(sort_lists(list1,list2))

lst=[8,1,23,3,7,9,9,10,0,4,2]
mylist=[[x] for x in lst]
while len(mylist)!=1:
    mylist=mergelist(mylist)

print (mylist)



    

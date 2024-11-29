def find_mak(lst):
    if len(lst)==0:
        return None
    max_item=lst[0]
    for item in lst:
        if  item> max_item:
            max_item=item
    return max_item


# if we do not return anything by default python return None
primes=[1,2,3,5,7,11,19,21,23,44]
tpl=(3,2,24,12)

#print(max(primes))
#print(11 in primes)

"""def find_item(li,x):
    for item in li:
        if x==item:
            return True
    print("Could not find ", x)
    return False

print(find_item(tpl,3))
print(tpl[0])"""

def my_function(a,b,c=0): #parameter
    result=a*3+b*2+c
    return result

a,b,c=20,30,10

#print(my_function(a,b,c)) # positional argument
#print(my_function(b=20,a=30,c=10)) # positional argument
#print(my_function(b=20,a=30)) # positional argument

def selection_sort(li):
    n=len(li)
    for i in range(n-1):
        min_item=100
        min_index=-1
        for j in range(i,n):
            if li[j]<min_item:
                min_item=li[j]
                min_index=j
        li[min_index]=li[i]
        li[i]=min_item
    return li

num=[21,3,5,2,7,5,7,12]
print(num)
print(selection_sort(num))


def a(lst):
    b = set()
    
    for value in lst:
        b.add(value)
    
    return len(b)

list1 = [1,2,3,4,2,3,5,6,7,10,8,8]
answer = a (list1)
print("Number of unique values:", answer)
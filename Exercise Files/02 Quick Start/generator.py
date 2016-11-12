theitem = 'myitem' 
thelist = ['myitem', 'youritem', 'ouritem', 'myitem'] 
def twice_1(lst, item): 
    return lst.count(item) > 1 
def twice_2(lst, item): 
    return (item in lst and item in lst[lst.index(item)+1:]) 
def twice_3(lst, item): 
    count = 0 
    for x in lst: 
        if x==item: 
            count=count + 1 
            return count 
def twice_4(lst, item): 
    try: 
        lst.remove(item) 
        lst.remove(item)
    except: return False 
    return True

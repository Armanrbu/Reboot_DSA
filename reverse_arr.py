# if we want to reverse full array

def func(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    func(arr,left+1,right-1)

def recursivearr(arr):
    func(arr,0,len(arr)-1)
    return arr

a = recursivearr(arr= [1,2,3,4,7,9,0])

print(a)


# Q5. Write a program in Python for finding that one number from an array of 100 numbers(with values ranging from 1 to 99) which is duplicate.

def function(nums,k ):
    d={}
    for i,e in enumerate(nums):
        if e in d:
            if i - d.get(e)<= k:
                return True
        d[e]=i
    return False
if __name__ =="__main__":
    nums=[5,5,4,3,2,1,5,1,]
    k=100

    if function(nums,k):
        print("yes there is duplicate")
    else:
        print("no there r no duplicates") 
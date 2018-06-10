


def reveArr(arr , start , end):
    while start<end:
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start +=1;
        end = end - 1;


def leftRotate(arr , d):
    reveArr(arr ,0 , d-1);
    reveArr(arr, d ,len(arr)-1);
    reveArr(arr , 0 , len(arr)-1);

def printArr(arr):
    for i in range(0 , len(arr)):
        print(arr[i],end=" ");
    print("");

arr = [1, 2, 3, 4, 5, 6, 7];
leftRotate(arr , 2);
printArr(arr);
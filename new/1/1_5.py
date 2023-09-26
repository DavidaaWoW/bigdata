def makeDict(A, B):
    dict = {}
    for i, b in enumerate(B):
        if(len(A) <= i):
            break
        if(b in dict):
            dict[b] += A[i]
        else:
            dict[b] = A[i]
    return dict

def main():
    A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    print (makeDict(A, B))

main()
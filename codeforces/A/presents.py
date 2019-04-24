#136A implementation

'''n = int(input())
presents = input().split()
friends = [0] * n

for i in range(n):
    friends[int(presents[i]) - 1] = i + 1

for i in friends:
    print(i)'''


#Editorial
n = int(input())
presents = list(map(int, input().split()))

for i in range(n):
    print(presents.index(i + 1) + 1)
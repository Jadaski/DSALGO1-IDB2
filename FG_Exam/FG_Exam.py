x= [1, 2, 3, 4, 5]
y= []
z= []

print("x= [1, 2, 3, 4, 5]")
print("y= []")
print("z= []")

y.append(x.pop())
y.append(x.pop())
print("y =" , y )

z.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.sort()
print("z =" , z )

print("------------------------------")

X = [1, 2, 21, 33, 45, 65, 12]

print("X = [1, 2, 21, 33, 45, 65, 12]")
print("Insertion Sort Algorithm in descending order")

for i in range(1, len(X)):
    key = X[i]
    j = i-1
    while j >= 0 and key > X[j]:
        X[j + 1] = X[j]
        j -= 1
    X[j + 1] = key

print(X)

print("Selection Sort Algorithm in ascending order")

for i in range(len(X)):
    min_idx = i
    for j in range(i+1, len(X)):
        if X[min_idx] > X[j]:
            min_idx = j
    X[i], X[min_idx] = X[min_idx], X[i]

print(X)
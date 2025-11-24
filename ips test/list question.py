n = int(input("enter the list size: "))
a = []
for i in range(n):
    a.append(int(input()))
s = 0
c = 0
for i in a:
    if i % 2 == 0:
        s += i
    else:
        c += 1
list1 = a[:]
list2 = a[:]
list2.append(s)
list3 = a[:]
list3.insert(1, c)
list4 = list3[:3]

print("Original List:", list1)
print("List after appending sum of even numbers:", list2)
print("List after inserting count of odd numbers at index 1:", list3)
list3.pop()
print("List after removing last element:", list3)
print("First 3 elements:", list4)
total = sum(a)
print("total is:", total)
avg = total / len(a)
print("Average:", avg)

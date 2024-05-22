
output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 5, 3, 2, 3]
d = [2]
e = [3]
new_output = []
new_output.append(a)
new_output.append(b)
new_output.append(c)
d.append(e)  # Append e to d before appending d
c.append(d)  # Append d to c before appending c
new_output.append(c)
print(new_output)

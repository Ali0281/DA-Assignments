in1_count = int(input())
in1 = [int(x) for x in input().split()]
in2_count = int(input())
in2 = [int(x) for x in input().split()]
i, j = 0, 0
while i < len(in1) and j < len(in2):
    if in1[i] == in2[j]:
        i, j = i + 1, j + 1
    elif in1[i] > in2[j]:
        if j + 1 < len(in2):
            in2[j + 1] += in2[j]
            in2_count, j = in2_count - 1, j + 1
        else:
            print(-1)
            quit()
    elif in1[i] < in2[j]:
        if i + 1 < len(in1):
            in1[i + 1] += in1[i]
            in1_count, i = in1_count - 1, i + 1
        else:
            print(-1)
            quit()

if in1_count == in2_count:
    print(in1_count)
else:
    print(-1)

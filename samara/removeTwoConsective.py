numbers = [1,6,4,4,4,5,5,4,6]


i = 1
count = 0
stack = []
for i in range(len(numbers)):
        # If stack is not empty and the current element is smaller than the
        # element at the index stored on the top of the stack.

        print("before:", stack)
        if stack and numbers[i] == stack[-1]:
            stack.pop()  # Pop the index from the stack.
            count+=1
        else:
            # result[index] = arr[i]  # The current element is the next smaller element for the popped index.
        # print("after:", stack)
            stack.append(numbers[i])  # Push the current index to the stack.
print(stack)
print(count)
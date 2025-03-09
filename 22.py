stack = []
n =  3



# start_for_close = n


# for i in range(2*n):
#     s=""
#     open_parentheses = 0
#     closed_parentheses = 0
#     for j in range(2*n):
#         if s=="":
#             s+="("
#         elif open_parentheses>closed_parentheses:
#             s+=")"
        
              

#     print(s)

res = []

def backtrack(open_parentheses, closed_parentheses):
    if open_parentheses == closed_parentheses == n:
        res.append("".join(stack))
        return
    
    if open_parentheses < n:
        stack.append("(")
        backtrack(open_parentheses+1, closed_parentheses)
        stack.pop()

    if closed_parentheses < open_parentheses:
        stack.append(")")
        backtrack(open_parentheses, closed_parentheses+1)
        stack.pop()


backtrack(0, 0)
print(res)    
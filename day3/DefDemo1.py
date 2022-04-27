# 自訂函數篇
# 加法涵式
def add(x, y):
    sum = x + y
    return sum

def div(x, y):
    temp = x / y
    return temp

def max(x, y):
    maxValue = x if x > y else y;
    return maxValue

# -------------------------
# 主程式
# -------------------------
a, b = 10, 20
result = add(a, b)
print(result)
result = div(a, b)
print(result)
result = max(a, b)
print(result)



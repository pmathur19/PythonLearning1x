# Exception
# abnormal event during the execution program, But ut can handled

# Error - specific code ->  1 gb -> 1.2 gb ? StackOverFlow
# 10 , 12 - Error -> It very diffcult to overcome Stack
# MemoryError - Error -> Restart, retry

# Java -> Python in java it is try and catch, while in python it is try and except

print("Insert the Card")

try:
    a = 10 / 0
except Exception as e:
    print("XX Error due to 10/0")

print("Take the Card")
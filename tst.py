

while True:
    nums = input("number: ")
    try:
        nums = float(int(nums))
        break
    except:
        pass
    
total = 0
for i, num in enumerate(str(nums), 1):
    total += num ** i
    
if total == nums:
    print("Disarium number")
else:
    print("not Disarium number")

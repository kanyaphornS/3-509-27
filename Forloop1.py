print("ตารางแม่สูตรคูณ")
number = int(input("พิมพ์เลขแม่สูตรคูณที่ต้องการ: "))
print(f"ตารางแม่สูตรคูณของ {number}:")
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
  

f = open("C:/Users/Rajdeep Ray\Desktop\Captaincy  Specialist              .txt", "r+", encoding="utf-8")

print(f.encoding)
print(f.closed)
print(f.buffer)
print(f.mode)
print(f.readable())
print(f.writable())

f.close()
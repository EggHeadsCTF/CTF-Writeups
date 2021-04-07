flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
x = ""
for i in range(0, len(flag)):
    x += chr(ord(flag[i]) >> 8)
    x += chr(int(bin(ord(flag[i]))[-8:], 2))
print(x)
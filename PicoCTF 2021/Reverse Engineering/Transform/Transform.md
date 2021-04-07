>I wonder what this really is...
```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```
This code means for every letter in flag, there are those 8 bits shifted to the left and then added to the ascii of the next letter. So 8 bits in front and in the back. To reverse this, just do the opposite. 

```python
flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"
x = ""
for i in range(0, len(flag)):
    x += chr(ord(flag[i]) >> 8) # Shift back to the right the 8 bits, first letter
    x += chr(int(bin(ord(flag[i]))[-8:], 2)) # Remove those 8 at the beginning and convert binary to ascii, second letter
# Now we have two sets of letters per each iteration
print(x)
```

> picoCTF{16_bits_inst34d_of_8_0ddcd97a}
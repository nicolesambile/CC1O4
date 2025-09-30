s = "hello world"

#O(1) access
print("first char:", s[0])

#O(n) traversal
for c in s:
 print ( c, end="")

#O(n) concatenation
s2_nbs = s + "!!!"
print("concatenation:", s2_nbs)

#O(n) substring search
print("contains world?", "world" in s)

letters='abcdefghijklmnopqrstuvwxyz'
keys='qwertyuiopasdfghjklzxcvbnm' #keyboard layout
d={letters[i]:keys[i] for i in range(len(letters))}
s=raw_input()
print ''.join(d[letter] for letter in s)

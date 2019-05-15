import unicodedata
for i in range(0x10ffff):
    try:
        n=unicodedata.name(chr(i))
        if len(n)> 5:print(i,'>>>',chr(i),'>>>',n,'a')
    except Exception:
        pass

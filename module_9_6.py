def all_variants(text):
    m = len(text)
    if m != 0:
     for i in range(len(text)):
        m += -1
        yield text[i]
     else:
         for j in range(len(text)):
             if j < len(text) - 1:
                 yield text[j : j+2]
             else:
                 yield text

a = all_variants("abc")
for i in a:
    print(i)




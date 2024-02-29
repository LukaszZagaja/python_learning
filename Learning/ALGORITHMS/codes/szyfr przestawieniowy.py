def kodowanie(tekst):
    txt_list = list(tekst)
    for i in range(0, len(tekst)-1, 2): # start, stop, step
        txt_list[i], txt_list[i+1] = txt_list[i+1], txt_list[i]
    return ''.join(txt_list)



txt = "Text"
print(kodowanie(txt))
from re import I


list1 = ["C","N","O","Z","AA","AL","AM","AX","AY","BJ","BK","BV","BW","CH","CI","CT","CU","DF","DG","DR","DS","ED","EE","EP","EQ","FB","FC","FE"]
x = input(str("บรรทัด = "))
opt = input(str("Min or Max = "))
guia1 = 0
if opt == "Min":
    for i in list1:
        
        if guia1 == 0:
            print("=MIN("+i+x+":",end=" ")
            guia1 +=1
        if guia1 == 1 :
            print(i+x+")")
            guia1 = 0
    
if opt == "Max":
    for i in list1:
        
        if guia1 == 0:
            print("=MAX("+i+x+":",end=" ")
            guia1 +=1
        if guia1 == 1 :
            print(i+x+")")
            guia1 = 0
    

        
    

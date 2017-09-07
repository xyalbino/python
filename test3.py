def fibs():
    a=0
    b=1
    while True:
        yield b

if __name__=='__main__':
    
    t=1
    for each in fibs():
        if t>10:
            break
        print(each)
        t+=1
    
    
    

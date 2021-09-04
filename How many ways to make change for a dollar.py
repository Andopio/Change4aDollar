Userin=input
Num = 0
for half in range (3):
    for quart in range(5):
        for dime in range(11):
            for nickel in range(21):
                for penny in range(101):
        
        
        
        
                  if 50*half + 25*quart + 10*dime + 5*nickel + 1*penny == 100:
                      if Userin=='y':
                          print('Q=',quart,'D=',dime,'H=',half,'N=',nickel,'P=',penny)
                      Num+=1    
                  
print('\nThere are {} ways to make change for a dollar'.format(Num))                    
         
        
        
        
        
        
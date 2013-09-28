def detect_triangle(a, b, c): 
    if (  a*a == (b*b + c*c) or b*b == (a*a + c*c) or c*c == (a*a + b*b )):
        vuong = 1 #bien kiem tra tam giac can
    else :
        vuong = 0
    if (a==b or a==c or b==c):
        can = 1 #bien kiem tra tam giac can
    else :
        can = 0
        
    if( a<=0 or b<=0 or c<=0 or a> 10**38 or b >  10**38 or c>10 **38 ):
        return -1 # kiem tra dữ liệu không hợp lệ
        
    elif( a+b < c or b+c < a or a+c < b):
        return 0 # không phải 3 cạnh của tam giác
    elif( a==b and b==c ):
        return 1 # kiem tra tam giác đều
    elif( vuong == 1 and can == 1):
        return 2 # kiem tra tam giác vuông cân
    elif( vuong == 1 and can == 0 ) :
        return 3 # kiem tra tam giác vuông
    elif ( vuong == 0 and can == 1):
        return 4 # kiem tra tam giac cân
    else :
        return 5 # kiem tra tam giác thường

               

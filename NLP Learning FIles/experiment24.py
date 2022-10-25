def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if num1<(num2+num3) and num2<(num1+num3) and num3<(num1+num2):
        return success
    else:
        return failure
        
num1=3
num2=4
num3=5
print(form_triangle(num1, num2, num3))
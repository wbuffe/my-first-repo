def calculator():
    num1=float(input("請輸入第一個數字"))
    num2=float(input("請輸入第二個數字"))
    operation= input("請輸入運算符號(+ - * / )")

    if operation =='+':
        print(f"結果：{num1 + num2}")
    elif operation == '-':
        print(f"結果：{num1 - num2}")
    elif operation == '*':    
        print(f"結果：{num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"結果：{num1 / num2}")
        else:
            print("錯誤：不能除以0") 
    else:
        print("無效的運算符號")           


calculator()
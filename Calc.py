
def Operacao(n1,n2):
    
    esc = input("1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão ")
    
    if esc == '1':
        return n1 + n2
    elif esc == '2':
        return n1 - n2
    elif esc == '3':
        return n1 * n2
    elif esc == '4':
        return n1 / n2
    else:
        print("Operação incorreta")
        Operacao(n1, n2)
            


def Num1():
    
    n1 = float(input("Digite o numero 1"))
    
    if(n1 <= 0) or not float(n1):
        print("Digite um numero 1 valido ")
        print("\n")
        Num1()
    else: 
        return n1
      
        

def Num2():
    
    n2 = float(input("Digite o numero 2"))
    
    if(n2 <= 0) or not float(n2):
        print("Digite um numero 2 valido ")
        print("\n")
        Num1()
    else:  
        return n2
     
    

def main():
    
    print("*******Bem vindo a calculadora: escolha uma operação para começar**********")
    print("\n")
    
    n1 = Num1()
    
    n2 = Num2()
    
    print(n2)
    
    resultado = Operacao(n1, n2)
    print("Resultado da operação:", resultado)
main()

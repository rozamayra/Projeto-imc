# Welcome to JDoodle!
#
# You can execute code here in 88 languages. Right now you’re in the Python3 IDE.
#
#  1. Click the orange Execute button ️▶ to execute the sample code below and see how it works.
#  2. Want help writing or debugging code? Type a query into JDroid on the right hand side ---------------->
#  3. Try the menu buttons on the left. Save your file, share code with friends and open saved projects.
#
# Want to change languages? Try the search bar up the top.

x=10
y=25
z=x+y

print ("sum of x+y =", z)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

if __name__ == "__main__":
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificar_imc(imc)}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

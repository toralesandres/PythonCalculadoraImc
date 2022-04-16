#calculadora de imc, con peso y altura

def calcularImc(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def pedirImc():
    peso = float(input('Ingrese su peso en kg'));
    alturaEnCm = int(input('Ingrese su altura en cm'));
    alturaEnMetros = alturaEnCm /100;

    imc = calcularImc(peso, alturaEnMetros)
    if imc <= 19:
        print('estado de delgadez');
    if imc >= 20 and imc <=26:
        print('peso normal');
    if imc >= 26 and imc <=30:
        print('estado de sobrepeso');
    if imc >=30:
        print('estado de obesidad');
    print('si IMC es de: ' + str(imc));

pedirImc();

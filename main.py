peso = int(input('Ingrese su peso en kg'));
alturaEnCm = int(input('Ingrese su altura en cm'));
alturaEnMetros = alturaEnCm /100;
imc = peso / (alturaEnMetros * alturaEnMetros);


if imc <= 19:
    print('estado de delgadez');
if imc >= 20 and imc <=26:
    print('peso normal');
if imc >= 26 and imc <=30:
    print('estado de sobrepeso');
if imc >=30:
    print('estado de obesidad');



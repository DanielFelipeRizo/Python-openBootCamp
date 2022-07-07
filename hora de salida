from datetime import time, datetime, timedelta


def saberHoraSalida(entrada=1):
    hora = datetime.now().time()
    tdHora = timedelta(hours=hora.hour, minutes=hora.minute, seconds=hora.second)

    horaSalida = time(hour=19, minute=00, second=00)
    tdHoraSalida = timedelta(hours=horaSalida.hour, minutes=horaSalida.minute, seconds=horaSalida.second)
    diferenciaHoras = tdHoraSalida - tdHora

    while entrada == 1:
        entrada = int(input('ingrese el numero 1 para saber su hora de salida: '))


        if (tdHora < tdHoraSalida):
            print('Faltan ', diferenciaHoras, ' para salir')

        else:
            print('Ya puedes ir a casa')


saberHoraSalida()

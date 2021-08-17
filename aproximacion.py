from math import *

def puntofijo():
    print('Método del punto fijo: x=g(x)');
    x=float(input('Ingresa valor inicial(X0): '));
    tolerancia=float(input('Máxima tolerancia permitida: '));
    N=int(input('Numero maximo de iteraciones: '));
    f=input('Ingrese la función g(x): ');
    er=100;
    i=1;
    print('#iteracion\t g(f(x))\t\t error estimado')
    while(i<=N and er>=tolerancia):
        temp=x; x=eval(f);
        er=abs((x-temp));
        print("%d\t\t%.12f\t%.12f"%(i,x,er));
        i+=1;
    print("\n La solucion mas aproximada es %s con un error estimado inferior a %s."%(x,tolerancia));

puntofijo()
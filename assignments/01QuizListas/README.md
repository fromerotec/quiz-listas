![Tec de Monterrey](../../images/logotecmty.png)
# Suma dos listas por posición
## Tema: Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Desarrolla un programa que permita realizar la suma elemento a elemento de dos listas de números enteros y con la misma cantidad de elementos.

## Entrada
Un número entero que indica cuántos elementos tendrá cada lista. El número debe ser mayor a 0.
Posteriormente el ingreso de los números enteros correspondientes a los elementos de las dos listas. Por ejemplo, si en la primera entrada se ingresa un 5, después del 5 se reciben 10 números más (uno en cada renglón) 5 para conformar cada lista.


## Salida
Si el número inicial ingresado es 0 o menor, deberá desplegar el mensaje "Error"
Una lista donde los elementos corresponde a la suma de los elementos de las dos listas de acuerdo con su posición, es decir los elementos de la posición 0 de las dos listas se suman y se ponen en la posición 0 de la lista resultado y así consecutivamente para todos los datos de la lista.


## Ejemplo de ejecución del programa
### Entrada
```
>>> 2
>>> 5
>>> 3
>>> 4
>>> 2
```
### Salida
```
[9, 5]
```
### Entrada
```
>>> -3
```
### Salida
```
Error
````


**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.

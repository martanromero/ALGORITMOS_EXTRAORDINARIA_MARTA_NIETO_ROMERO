# ALGORITMOS_EXTRAORDINARIA_MARTA_NIETO_ROMERO
Link del repositorio: https://github.com/martanromero/ALGORITMOS_EXTRAORDINARIA_MARTA_NIETO_ROMERO.git 
¿Qué es el método Bubble Sort?

Bubble Sort, o Ordenamiento Burbuja, es un sencillo algoritmo de ordenación que funciona comparando cada par de elementos adyacentes en una lista y, si están en el orden incorrecto, los intercambia. Este proceso se repite hasta que no se necesiten más intercambios, lo que significa que la lista está ordenada.

¿Cómo funciona?

El algoritmo de Bubble Sort funciona de la siguiente manera:

Se comparan los dos primeros elementos de la lista. Si el primer elemento es mayor que el segundo, se intercambian.
Luego se comparan el segundo y el tercer elemento. Si el segundo elemento es mayor que el tercero, se intercambian.
Este proceso continúa hasta que se comparan y, si es necesario, se intercambian todos los pares de elementos adyacentes.
Después de la primera pasada, el elemento más grande se habrá "burbujeado" hasta el final de la lista.
El proceso se repite para los restantes elementos de la lista, excluyendo el último elemento en cada iteración porque ya está en su lugar correcto.
El algoritmo continúa hasta que en una pasada completa no se realicen intercambios, lo que indica que la lista está ordenada.
¿En qué casos es conveniente utilizar Bubble Sort?

Bubble Sort es conveniente para listas pequeñas o cuando se necesita un algoritmo simple de entender y fácil de implementar. Sin embargo, no es adecuado para listas grandes debido a su ineficiencia; tiene una complejidad temporal de 
𝑂
(
𝑛
2
)
O(n 
2
 ), donde 
𝑛
n es el número de elementos en la lista.

Ejemplo Conceptual:

Para demostrar el método de Bubble Sort, vamos a ordenar la lista [29, 10, 14, 37, 13].

Primera Pasada:

Comparar 29 y 10: 10 es menor, se intercambian → [10, 29, 14, 37, 13]
Comparar 29 y 14: 14 es menor, se intercambian → [10, 14, 29, 37, 13]
Comparar 29 y 37: no se intercambian → [10, 14, 29, 37, 13]
Comparar 37 y 13: 13 es menor, se intercambian → [10, 14, 29, 13, 37]
Al final de la primera pasada, el mayor elemento (37) está en su posición correcta.

Segunda Pasada:

Comparar 10 y 14: no se intercambian → [10, 14, 29, 13, 37]
Comparar 14 y 29: no se intercambian → [10, 14, 29, 13, 37]
Comparar 29 y 13: 13 es menor, se intercambian → [10, 14, 13, 29, 37]
Al final de la segunda pasada, el segundo mayor elemento (29) está en su posición correcta.

Tercera Pasada:

Comparar 10 y 14: no se intercambian → [10, 14, 13, 29, 37]
Comparar 14 y 13: 13 es menor, se intercambian → [10, 13, 14, 29, 37]
Al final de la tercera pasada, el tercer mayor elemento (14) está en su posición correcta.

Cuarta Pasada:

Comparar 10 y 13: no se intercambian → [10, 13, 14, 29, 37]
Al final de la cuarta pasada, la lista está completamente ordenada.

La lista ordenada es: [10, 13, 14, 29, 37]

Este proceso demuestra cómo Bubble Sort ordena una lista a través de comparaciones e intercambios sucesivos hasta que toda la lista está en orden ascendente.

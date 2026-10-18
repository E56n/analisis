# Volumen III: Análisis funcional y álgebras de operadores

**Autor de la edición:** Eder Said Martinez Ramirez.  
**Autor de las lecturas originales:** Miguel Ángel Valencia Bucio.

El volumen desarrolla las 37 lecturas de Análisis Matemático 3 en seis partes y 18 capítulos. Incluye los 194 ejercicios originales, con todos sus incisos y soluciones, y cuatro ejercicios complementarios. Los enunciados que necesitan hipótesis adicionales se corrigen expresamente, con explicación o contraejemplo. Las referencias, los créditos de adaptación y los resultados externos de panorama se identifican en el texto.

## Archivos

- `main.tex`: documento principal; `main.pdf`: edición compilada.
- `capitulos/`: desarrollo de los 18 capítulos.
- `presentacion.tex`, `notacion.tex`, `cobertura.tex` y `referencias.tex`: presentación, notación, correspondencia con las lecturas y bibliografía.
- `editorial/cobertura.json`: inventario general y procedencia de las 37 lecturas; los otros archivos de cobertura detallan ejercicios, incisos y correcciones.
- `editorial/verificacion.json`: comprobaciones de la edición final.

## Compilación

Se requieren XeLaTeX, `latexmk` y `makeindex`, con los paquetes declarados en `main.tex`. Desde esta carpeta:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

La configuración de índice está en `indice.ist`; el estilo editorial y los recursos visuales están incluidos. El producto interno se toma lineal en el primer argumento. Las etiquetas de ejercicios originales siguen el patrón `ej:v3-lXX-N`, independiente de su número editorial.

Las notas de Egor Maximenko y la presentación de Gerardo Ramos Vázquez se acreditan junto a sus adaptaciones y en la bibliografía. Los teoremas de James se presentan como panorama explícitamente externo y no se emplean para justificar las soluciones.

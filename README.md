# Análisis

Autor de la edición ampliada: **Eder Said Martinez Ramirez**.

Colección de cuatro volúmenes basada en las lecturas de los cursos de Análisis Matemático de Miguel Ángel Valencia Bucio. Se desarrollan demostraciones, se explicitan hipótesis, se corrigen enunciados cuando es necesario y se resuelven los ejercicios.

## Volúmenes

1. [Espacios métricos, normados y de Hilbert](volumen-01/): desarrollo del primer curso, 32 capítulos.
2. Teoría de la medida e integración: previsto.
3. Análisis funcional y álgebras de operadores: previsto.
4. Análisis armónico y grupos localmente compactos: previsto.

Cada volumen tendrá su propia carpeta. Los volúmenes 2–4 todavía no están redactados en este repositorio.

## Compilar el primer volumen

Se requiere una distribución de TeX con `pdflatex`, `latexmk`, `makeindex` y los paquetes indicados en el preámbulo. Con TeX Live instalado:

```sh
cd volumen-01
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` compila el documento, genera el índice alfabético y repite las pasadas necesarias para resolver referencias. El resultado es `volumen-01/main.pdf`.

## Fuentes y trazabilidad

La bibliografía está en `volumen-01/referencias.tex`. Los registros de cobertura y correcciones por bloque están en `volumen-01/editorial/`. La numeración de capítulos conserva la de las lecturas originales y cada ejercicio identifica su procedencia. No se incluyen los PDF originales ni copias de los libros de referencia.

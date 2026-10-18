# Análisis armónico y grupos localmente compactos

Volumen IV de **Análisis**, de **Eder Said Martinez Ramirez**. Edición desarrollada en seis partes y dieciséis capítulos, con índice general, índice de notación, índice alfabético y referencias finales.

La base son las 27 lecturas originales disponibles de *Análisis Matemático 4*, de Miguel Ángel Valencia Bucio. La lectura 24 es una reconstrucción editorial independiente, identificada como tal y no atribuida a Valencia Bucio. Se incluyen 81 ejercicios originales, 8 de esa reconstrucción y 10 de ampliación: **99 ejercicios y 99 soluciones**.

Las ampliaciones utilizan documentos reales de Egor Maximenko y, para Paley–Wiener y series cardinales, de Iris Paola Lozano Vite y Egor Maximenko. La referencia principal para la teoría abstracta es la segunda edición de *A Course in Abstract Harmonic Analysis*, de Gerald B. Folland (2016). `referencias.tex` contiene los títulos y enlaces concretos.

## Compilación

Se requieren XeLaTeX, `latexmk`, MakeIndex, Latin Modern y los paquetes del preámbulo. Desde esta carpeta:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

El resultado es `main.pdf`. Las fuentes matemáticas están en `capitulos/`; `partes.tex` fija su orden. La compilación ejecuta MakeIndex con `indice.ist`.

## Registro editorial

- `editorial/cobertura-completa.json`: correspondencia por lectura, todos los ejercicios, incisos, enunciados, soluciones y correcciones; distingue originales, reconstrucción y ampliaciones.
- `editorial/cobertura-17-21.json` y `editorial/cobertura-25-28.json`: auditorías detalladas de Haar, cocientes, caracteres y dualidad.
- `editorial/verificacion-final.json`: comprobación estructural, compilación y revisión visual.

Las convenciones de signo, normalización de Haar, producto interno y función modular se declaran en la presentación y en los capítulos pertinentes. La existencia y unicidad de Haar, inversión, Plancherel, Pontryagin y extensión de caracteres se desarrollan con pruebas. Carleson se identifica expresamente como panorama externo y no interviene en las demostraciones del volumen.

El diseño reconoce como referencia visual el repositorio público de MrPaborru, *Apuntes de Homotopía Estable*, y utiliza el emblema del sitio oficial de la ESFM. Es una edición personal, no una publicación oficial del IPN.

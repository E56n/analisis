# Análisis

Autor de la edición ampliada: **Eder Said Martinez Ramirez**.

Escuela Superior de Física y Matemáticas, Instituto Politécnico Nacional. Maestría en Ciencias Fisicomatemáticas; línea de investigación: Matemáticas Puras.

Colección de cuatro volúmenes basada en las lecturas de los cursos de Análisis Matemático de **Miguel Ángel Valencia Bucio**. La edición reorganiza el material, desarrolla demostraciones, explicita hipótesis, corrige enunciados y presenta soluciones de los ejercicios de las lecturas. Las ampliaciones inspiradas en **Egor Maximenko** y en los demás autores se identifican junto al contenido correspondiente y en las referencias de cada volumen.

## Los cuatro volúmenes

| Volumen | Tema central | Organización | Páginas | PDF compilado | Fuentes |
| --- | --- | --- | --- | --- | --- |
| I | Espacios métricos, normados y de Hilbert | 6 partes, 16 capítulos | 221 | [Volumen I](volumen-01/main.pdf) | [LaTeX](volumen-01/) |
| II | Teoría de la medida e integración | 6 partes, 16 capítulos | 127 | [Volumen II](volumen-02/main.pdf) | [LaTeX](volumen-02/) |
| III | Análisis funcional y álgebras de operadores | 6 partes, 18 capítulos | 176 | [Volumen III](volumen-03/main.pdf) | [LaTeX](volumen-03/) |
| IV | Análisis armónico y grupos localmente compactos | 6 partes, 16 capítulos | 131 | [Volumen IV](volumen-04/main.pdf) | [LaTeX](volumen-04/) |

La edición reúne **655 páginas y 683 ejercicios con solución**: 641 procedentes de las lecturas originales, ocho de la reconstrucción editorial de la lectura 24 del cuarto curso y 34 complementos.

La jerarquía es **volumen → parte → capítulo → sección**. Los capítulos se numeran consecutivamente dentro de cada volumen. Cada libro contiene índice general, índice de notación, índice alfabético y referencias al final. Las tablas de correspondencia permiten encontrar las lecturas originales dentro de la nueva organización.

## Contenido y alcance editorial

- El volumen I añade, entre otros temas, explicaciones y ejercicios sobre cocientes, seminormas, el teorema de Picard, matrices de Gram y bases de Schauder.
- El volumen II desarrolla la construcción de medidas, los modos de convergencia, los espacios de funciones, Radon–Nikodym y la representación de Riesz tanto para funcionales positivas sobre `C_c` como para el dual de `C_0`.
- El volumen III estudia dualidad, topologías débiles, compacidad, reflexividad, operadores compactos, teoría espectral y álgebras de operadores.
- El volumen IV enlaza series y transformadas de Fourier, muestreo, medida de Haar, representaciones, inversión, Plancherel y dualidad de Pontryagin.

Los ejercicios conservan una etiqueta de lectura y número de origen. Los problemas adicionales se distinguen de los originales. Cuando un enunciado necesita una hipótesis o es falso, se indica la corrección y se proporciona la justificación o un contraejemplo. Los resultados profundos presentados sólo como panorama se identifican expresamente y no se utilizan como pasos sin demostrar en los argumentos desarrollados.

La lectura 24 del cuarto curso se conserva como **reconstrucción editorial**: no se atribuye a Valencia Bucio como una lectura original recuperada. Sus ocho ejercicios se contabilizan por separado. En el segundo volumen, el alcance de las soluciones corresponde a las listas de las 33 lecturas; los dos exámenes archivados con ellas no constituyen una lista adicional resuelta.

## Compilar

Se requiere una distribución de TeX con `xelatex`, `latexmk`, `makeindex`, las fuentes Latin Modern y los paquetes indicados en los archivos principales. Desde la carpeta del volumen deseado:

```sh
cd volumen-01
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Sustituya `volumen-01` por `volumen-02`, `volumen-03` o `volumen-04`. El resultado es `main.pdf` dentro de esa carpeta. `latexmk` repite las pasadas necesarias para resolver referencias y genera el índice alfabético. Los archivos temporales de compilación no forman parte del repositorio.

Cada carpeta contiene el documento principal, los capítulos, la organización en partes, la notación, la bibliografía y los registros editoriales de cobertura y correcciones. El primer volumen incluye además `editorial/verificar_estructura.py` para comprobar sus 206 ejercicios originales y sus 20 ampliaciones.

## Créditos y referencias

**Miguel Ángel Valencia Bucio** es el autor de las lecturas que proporcionan el temario y los ejercicios originales. **Eder Said Martinez Ramirez** es el autor de esta edición ampliada. Las notas y presentaciones de **Egor Maximenko**, disponibles en [su sitio docente](https://esfm.egormaximenko.com/), aportan enfoques didácticos y complementos. Los materiales con coautoría o autoría de estudiantes conservan sus créditos específicos; entre ellos figuran **Iris Paola Lozano Vite** y **Gerardo Ramos Vázquez**. La bibliografía de cada volumen identifica los documentos efectivamente utilizados, sus autores y enlaces, además de libros y artículos reales.

El diseño toma como referencia visual los [Apuntes de Homotopía Estable de MrPaborru](https://github.com/MrPaborru/Apuntes-Homotop-a-Estable), combinados con una composición tradicional de libros de matemáticas, tipografía Latin Modern, detalles guinda y ocre y el emblema de la ESFM. La procedencia gráfica y las decisiones de identidad están documentadas en [el registro de diseño](volumen-01/editorial/identidad-esfm-ipn.md). Esta es una edición personal, no una publicación oficial ni una obra avalada por el IPN.

Las referencias están en `referencias.tex` dentro de cada volumen; los registros de cobertura y correcciones están en `editorial/`. No se incluyen copias de los libros de referencia ni los PDF originales de los cursos.

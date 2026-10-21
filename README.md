# Análisis

Autor de la edición ampliada: **Eder Said Martinez Ramirez**.

Escuela Superior de Física y Matemáticas, Instituto Politécnico Nacional. Maestría en Ciencias Fisicomatemáticas; línea de investigación: Matemáticas Puras.

Colección de cuatro volúmenes basada en las lecturas de los cursos de Análisis Matemático de **Miguel Ángel Valencia Bucio**. La edición reorganiza el material, desarrolla demostraciones, explicita hipótesis, corrige enunciados y presenta soluciones de los ejercicios de las lecturas. Las ampliaciones inspiradas en **Egor Maximenko** y en los demás autores se identifican junto al contenido correspondiente y en las referencias de cada volumen.

## Los cuatro volúmenes

| Volumen | Tema central | Organización | Apuntes | Solucionario |
| --- | --- | --- | --- | --- |
| I | Espacios métricos, normados y de Hilbert | 6 partes, 16 capítulos | [main.pdf](volumen-01/main.pdf) | [solucionario.pdf](volumen-01/solucionario.pdf) |
| II | Teoría de la medida e integración | 6 partes, 16 capítulos | [main.pdf](volumen-02/main.pdf) | [solucionario.pdf](volumen-02/solucionario.pdf) |
| III | Análisis funcional y álgebras de operadores | 6 partes, 18 capítulos | [main.pdf](volumen-03/main.pdf) | [solucionario.pdf](volumen-03/solucionario.pdf) |
| IV | Análisis armónico y grupos localmente compactos | 6 partes, 16 capítulos | [main.pdf](volumen-04/main.pdf) | [solucionario.pdf](volumen-04/solucionario.pdf) |

La colección conserva **683 ejercicios**: 641 procedentes de las lecturas originales, ocho de la reconstrucción editorial de la lectura 24 del cuarto curso y 34 complementos. Cada volumen tiene apuntes con ejercicios propuestos y un solucionario aparte con los mismos enunciados y sus soluciones.

La jerarquía es **volumen → parte → capítulo → sección**. Los capítulos se numeran consecutivamente dentro de cada volumen. Cada libro de apuntes contiene índice general, índice de notación, índice alfabético y referencias al final. Las tablas de correspondencia permiten encontrar las lecturas originales dentro de la nueva organización. Cada solucionario conserva los capítulos y la numeración de los ejercicios de su volumen.

## Contenido y alcance editorial

- El volumen I añade, entre otros temas, explicaciones y ejercicios sobre cocientes, seminormas, el teorema de Picard, matrices de Gram y bases de Schauder.
- El volumen II desarrolla la construcción de medidas, los modos de convergencia, los espacios de funciones, Radon–Nikodym y la representación de Riesz tanto para funcionales positivas sobre `C_c` como para el dual de `C_0`.
- El volumen III estudia dualidad, topologías débiles, compacidad, reflexividad, operadores compactos, teoría espectral y álgebras de operadores.
- El volumen IV enlaza series y transformadas de Fourier, muestreo, medida de Haar, representaciones, inversión, Plancherel y dualidad de Pontryagin.

Los ejercicios conservan una etiqueta de lectura y número de origen. Los problemas adicionales se distinguen de los originales. Cuando un enunciado necesita una hipótesis o es falso, se indica la corrección y se proporciona la justificación o un contraejemplo. Los resultados profundos presentados sólo como panorama se identifican expresamente y no se utilizan como pasos sin demostrar en los argumentos desarrollados.

La lectura 24 del cuarto curso se conserva como **reconstrucción editorial**: no se atribuye a Valencia Bucio como una lectura original recuperada. Sus ocho ejercicios se contabilizan por separado. En el segundo volumen, el alcance de las soluciones corresponde a las listas de las 33 lecturas; los dos exámenes archivados con ellas no constituyen una lista adicional resuelta.

## Nueva estructura

- `main.tex`: entrada de los apuntes, con teoría y ejercicios sin soluciones ni recuadros rojos.
- `solucionario.tex`: entrada del solucionario, con enunciados y soluciones, y ejercicios en recuadros guinda.
- `preambulo.tex`: paquetes, macros y configuración compartidos por ambos documentos.
- `capitulos/`: teoría y ejercicios propuestos, en su ubicación original.
- `ejercicios-soluciones.tex`: copia de los ejercicios y sus soluciones, organizada por capítulo y con la misma numeración que los apuntes.
- `portada.tex` y `portada-solucionario.tex`: portadas independientes basadas en el mismo diseño.
- `estilo-esfm.tex`, `indice.ist` y `assets/`: estilo e identidad gráfica.
- `partes.tex`, `cobertura.tex` y `notacion.tex`: orden temático, correspondencia con las lecturas e índice de notación de los apuntes.
- `referencias.tex`: bibliografía compartida, escrita con `thebibliography`; no requiere BibTeX ni Biber.
- `referencias-apuntes.tex`: referencias del solucionario a resultados de los apuntes mediante `xr-hyper`.
- `.latexmkrc`: configura XeLaTeX, la compilación de ambos documentos y el almacenamiento de auxiliares en `build/`.
- `editorial/`: procedencia, cobertura, correcciones y verificaciones.
- `build/`: carpeta de auxiliares; se conserva con `.gitkeep`, pero su contenido de compilación no se versiona.

Los enunciados están en los capítulos y en `ejercicios-soluciones.tex`. Si se corrige uno, hay que actualizar ambas copias. Las soluciones se editan únicamente en `ejercicios-soluciones.tex`. El verificador de la raíz comprueba que los enunciados sean idénticos y que cada ejercicio conserve su solución y su capítulo.

## Compilación

Se requieren XeLaTeX, `latexmk`, MakeIndex, Latin Modern y los paquetes de `preambulo.tex`, incluido `xr-hyper`. Ejecute los comandos desde la carpeta del volumen deseado, por ejemplo `cd volumen-01`. Sustituya `volumen-01` por `volumen-02`, `volumen-03` o `volumen-04` según corresponda.

Ambos documentos, en orden (apuntes y después solucionario):

```sh
latexmk -interaction=nonstopmode -halt-on-error
```

La forma explícita equivalente es:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex solucionario.tex
```

Solo los apuntes:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Solo el solucionario:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error solucionario.tex
```

Los resultados son `main.pdf` y `solucionario.pdf`. Los ejercicios tienen la misma numeración por capítulo en ambos PDF. Los apuntes conservan sus índices y tablas de correspondencia; el solucionario contiene índice por capítulos y bibliografía.

**Primera compilación:** compile ambos documentos, o los apuntes antes del solucionario. Este último utiliza `build/main.aux` para resolver las referencias a la teoría. Después se pueden compilar por separado; si cambia la numeración de los resultados o se eliminan los auxiliares, vuelva a compilar primero los apuntes. Conserve los dos PDF en la misma carpeta para que funcionen los enlaces entre ellos.

## Archivos de compilación y limpieza

La configuración `.latexmkrc` está incluida en cada volumen. Al clonar el repositorio y compilar con `latexmk` desde la carpeta del volumen, los auxiliares (`.aux`, `.log`, `.toc`, `.idx`, `.ind`, `.fls`, `.fdb_latexmk`, `.xdv`, etc.) se guardan automáticamente en `build/`. Los dos PDF finales permanecen junto a las fuentes: `main.pdf` y `solucionario.pdf`. La configuración funciona con TeX Live y MiKTeX; no hay que añadir opciones de directorio a los comandos anteriores.

Los auxiliares sirven para generar índices, resolver referencias y evitar recompilaciones innecesarias. Se pueden regenerar. Cada carpeta `build/` se conserva en el repositorio mediante `.gitkeep`; todos sus archivos de compilación están excluidos de Git. Para limpiarla, borre los auxiliares de su interior o use el comando siguiente, conservando la carpeta y `.gitkeep`.

Para limpiar los auxiliares conservando los PDF finales, desde la carpeta del volumen:

```sh
latexmk -c main.tex solucionario.tex
```

Después de limpiar, compile ambos documentos para regenerar las referencias entre ellos. Si utiliza un editor, configúrelo para ejecutar `latexmk` desde la carpeta del volumen; invocar directamente `xelatex` no lee `.latexmkrc`.

## Verificación

Desde la raíz del proyecto:

```sh
python verificar_solucionarios.py
```

También puede añadir el número de volumen para comprobar uno solo. El programa no modifica archivos ni interpreta el contenido matemático. Verifica enunciados idénticos, número de ejercicios y soluciones, capítulos, etiquetas, referencias, citas y equilibrio de entornos.

`verificacion-conjunta.json` y los registros anteriores de `editorial/` corresponden a la edición integrada, que contenía teoría y soluciones en un solo PDF. `editorial/verificacion-separacion.json` documenta la edición separada y los nuevos PDF.

El primer volumen conserva además `editorial/verificar_estructura.py`, actualizado para comprobar la separación de sus 206 ejercicios originales y 20 ampliaciones.

## Créditos y referencias

**Miguel Ángel Valencia Bucio** es el autor de las lecturas que proporcionan el temario y los ejercicios originales. **Eder Said Martinez Ramirez** es el autor de esta edición ampliada. Las notas y presentaciones de **Egor Maximenko**, disponibles en [su sitio docente](https://esfm.egormaximenko.com/), aportan enfoques didácticos y complementos. Los materiales con coautoría o autoría de estudiantes conservan sus créditos específicos; entre ellos figuran **Iris Paola Lozano Vite** y **Gerardo Ramos Vázquez**. La bibliografía de cada volumen identifica los documentos efectivamente utilizados, sus autores y enlaces, además de libros y artículos reales.

El diseño toma como referencia visual los [Apuntes de Homotopía Estable de MrPaborru](https://github.com/MrPaborru/Apuntes-Homotop-a-Estable), combinados con una composición tradicional de libros de matemáticas, tipografía Latin Modern, detalles guinda y ocre y el emblema de la ESFM. La procedencia gráfica y las decisiones de identidad están documentadas en [el registro de diseño](volumen-01/editorial/identidad-esfm-ipn.md). Esta es una edición personal, no una publicación oficial ni una obra avalada por el IPN.

Las referencias están en `referencias.tex` dentro de cada volumen; los registros de cobertura y correcciones están en `editorial/`. No se incluyen copias de los libros de referencia ni los PDF originales de los cursos.

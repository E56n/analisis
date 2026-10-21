# Volumen III: Análisis funcional y álgebras de operadores

**Autor de la edición:** Eder Said Martinez Ramirez.

**Autor de las lecturas originales:** Miguel Ángel Valencia Bucio.

El volumen se entrega en dos documentos: [apuntes](main.pdf), con teoría y ejercicios propuestos, y [solucionario](solucionario.pdf), con los mismos ejercicios y sus soluciones. Los apuntes se organizan en seis partes y 18 capítulos; el solucionario conserva la numeración de esos capítulos y sus 198 ejercicios.

El alcance de la edición comprende 37 lecturas, 194 ejercicios originales y cuatro complementarios. Las ampliaciones y rectificaciones conservan sus créditos y su procedencia; las fuentes utilizadas se identifican en `referencias.tex` y en los registros editoriales.

## Estructura y edición

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

Se requieren XeLaTeX, `latexmk`, MakeIndex, Latin Modern y los paquetes de `preambulo.tex`, incluido `xr-hyper`. Ejecute los comandos desde esta carpeta.

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

Los registros anteriores de `editorial/` corresponden a la edición integrada, que contenía teoría y soluciones en un solo PDF. `editorial/verificacion-separacion.json` documenta la edición separada y los nuevos PDF.

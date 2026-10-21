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

## Estructura común y edición

Los cuatro volúmenes dependen de `comun/`; hay que clonar la colección completa.

| Archivo o carpeta | Qué se edita aquí |
| --- | --- |
| `comun/paquetes.tex` | Paquetes y fuentes compartidos: Latin Modern Roman, Roman Caps y Sans. |
| `comun/preambulo.tex` | Metadatos, macros matemáticas comunes, entornos, numeración y configuración del índice. |
| `comun/estilo-esfm.tex` | Diseño editorial, colores, encabezados, partes, capítulos y recuadros. |
| `comun/portada.tex`, `comun/modalidad.tex`, `comun/datos-coleccion.tex` | Diseño único de portada, subtítulo y metadatos por modalidad, y datos de la colección. |
| `comun/assets/escudo-esfm.pdf` | Única copia del escudo original. |
| `comun/indice.ist` | Estilo de MakeIndex, compartido por ambos documentos. |
| `comun/referencias-apuntes.tex` | Importación mediante `xr-hyper` de `build/main.aux`, con prefijo `apuntes-` y enlaces relativos a `main.pdf`. |
| `comun/apuntes.tex`, `comun/solucionario.tex` | Ensamblaje común de los dos tipos de documento. |
| `comun/latexmkrc` | Configuración única de compilación y dependencia automática del solucionario. |
| `.latexmkrc` y `volumen-XX/.latexmkrc` | Entradas pequeñas para cargar esa configuración desde la raíz o un volumen. |
| `volumen-XX/main.tex`, `volumen-XX/solucionario.tex` | Ocho objetivos seleccionables, sin duplicar el ensamblaje. |
| `volumen-XX/datos.tex` | Título, palabras clave, número de volumen, saltos de portada, tamaños y separaciones específicos. |
| `volumen-XX/preambulo.tex` | Extensiones locales, respetando su posición respecto de los paquetes y el estilo comunes. |
| `volumen-XX/capitulos/`, `ejercicios-soluciones.tex` | Teoría y ejercicios locales, y copia de enunciados y soluciones. |
| `volumen-XX/presentacion.tex`, `partes.tex`, `cobertura.tex`, `notacion.tex`, `referencias.tex` | Presentación, orden, correspondencia con las lecturas, notación y bibliografía locales. |
| `volumen-XX/build/` | Auxiliares aislados por volumen y por nombre de documento (`main.*` y `solucionario.*`). Solo se versiona `.gitkeep`. |
| `herramientas/` | Lectura de fuentes efectivas, auditoría de PDF y pruebas de compilación en copias limpias. |

Las particularidades del volumen II (`xurl`, macros, `DeclareMathOperator*{esssup}` y espaciados del índice) se mantienen locales. III y IV conservan sus operadores, incluida la variante sin asterisco de `esssup`. La presentación del volumen I se extrajo literalmente a su propio archivo local. La bibliografía sigue usando `thebibliography`; no requiere BibTeX ni Biber.

Los enunciados continúan duplicados entre los capítulos y `ejercicios-soluciones.tex`: esta migración no cambia ese modelo. Al corregir un enunciado, actualice ambas copias. Las soluciones se editan únicamente en `ejercicios-soluciones.tex`.

## Dependencias

Para compilar: una distribución TeX con XeLaTeX, `latexmk`, Perl y MakeIndex; las fuentes Latin Modern; y los paquetes de `comun/paquetes.tex` y los preámbulos locales, entre ellos `fontspec`, `babel` (español), AMS, `imakeidx`, `xr-hyper`, `hyperref`, `bookmark`, `titlesec`, `tocloft` y `tcolorbox`. El volumen II añade `xurl`. Se probó con TeX Live 2024 y latexmk 4.86a en Windows. La emulación de directorio auxiliar también está configurada para MiKTeX, que no se probó en este entorno.

Los verificadores de fuentes requieren Python 3 y su biblioteca estándar. La auditoría y la batería de compilación requieren además `pypdf`, `pypdfium2` y `Pillow`.

## Compilar desde la raíz del repositorio

Un documento concreto (cambie `01` por `02`, `03` o `04`):

```sh
latexmk -interaction=nonstopmode -halt-on-error volumen-01/main.tex
latexmk -interaction=nonstopmode -halt-on-error volumen-01/solucionario.tex
```

Una pareja:

```sh
latexmk -interaction=nonstopmode -halt-on-error volumen-01/main.tex volumen-01/solucionario.tex
```

Toda la colección, ocho documentos:

```sh
latexmk -interaction=nonstopmode -halt-on-error
```

## Compilar desde la carpeta de un volumen

```sh
cd volumen-01
latexmk -interaction=nonstopmode -halt-on-error main.tex
latexmk -interaction=nonstopmode -halt-on-error solucionario.tex
latexmk -interaction=nonstopmode -halt-on-error
```

Las tres últimas líneas son alternativas: solo apuntes, solo solucionario y ambos. XeLaTeX se selecciona en la configuración; `-xelatex` sigue siendo válido, pero no es necesario. No se deben invocar las entradas desde `comun/` ni usar directamente `xelatex` si se desea la dependencia automática y el aislamiento de auxiliares.

Al pedir un solucionario, la configuración comprueba primero sus apuntes con `latexmk`. Genera o actualiza sus auxiliares si faltan o cambió cualquiera de sus fuentes, incluidas etiquetas y numeración; si están al día, no recompila sus PDF. No requiere una compilación manual previa y no reconstruye otros volúmenes. Puede generar o actualizar también `main.pdf` del mismo volumen, para que los destinos enlazados correspondan a los apuntes actuales. La comprobación se omite durante la limpieza.

Los resultados permanecen en `volumen-XX/main.pdf` y `volumen-XX/solucionario.pdf`. Los auxiliares van a `volumen-XX/build/`, sin colisiones entre volúmenes ni documentos. Las rutas internas se resuelven desde el volumen, porque la configuración cambia a ese directorio para cada objetivo. MakeIndex se ejecuta desde `build/` y carga `../../comun/indice.ist`; la declaración de `imakeidx` también apunta al estilo común.

Conserve los dos PDF de cada volumen juntos para que funcionen los enlaces del solucionario a los apuntes. Ambos PDF siguen versionados; los auxiliares y las pruebas temporales están excluidos de Git.

## Limpieza y reconstrucción

Desde la raíz, para toda la colección:

```sh
latexmk -c
latexmk -interaction=nonstopmode -halt-on-error
```

Desde un volumen, para su pareja:

```sh
latexmk -c main.tex solucionario.tex
latexmk -interaction=nonstopmode -halt-on-error
```

La limpieza conserva los PDF finales, las carpetas `build/` y `.gitkeep`. La siguiente compilación regenera los auxiliares necesarios. También puede borrar solo el contenido generado de `build/`, conservando `.gitkeep`. Evite `-C` si quiere conservar los PDF.

## Verificación

Desde la raíz:

```sh
python verificar_solucionarios.py
python volumen-01/editorial/verificar_estructura.py
```

El primero acepta un número de volumen opcional. Ambos inspeccionan las fuentes efectivas, incluidos los archivos comunes, y no reescriben registros históricos. El segundo permite guardar un registro nuevo con `--output ruta.json`.

Para repetir la matriz completa de compilación, limpieza, aislamiento y actualización de referencias en copias temporales:

```sh
python herramientas/probar_compilacion.py --salida tmp/aceptacion.json
```

Para añadir una comparación editorial con ocho PDF de referencia, organizados en carpetas `volumen-01` a `volumen-04`:

```sh
python herramientas/probar_compilacion.py --referencia ruta/a/referencia --salida tmp/aceptacion.json
```

La comparación abarca páginas, texto, metadatos específicos, marcadores, destinos y enlaces, y renderizado de todas las páginas. Las diferencias se guardan como imágenes para su revisión. La matriz comprueba los cuatro apuntes individuales, los cuatro solucionarios desde cero con sus dependencias, las cuatro parejas y la colección, además de limpiar, reconstruir y cambiar temporalmente una numeración teórica para verificar que el solucionario se actualiza. Las modificaciones de prueba nunca se hacen sobre las fuentes originales.

`editorial/migracion-comunes.md` y `editorial/migracion-comunes.json` documentan esta migración. Los registros previos de `volumen-XX/editorial/` y `verificacion-conjunta.json` son antecedentes de ediciones anteriores y se conservan sin reescribir.

## Créditos y referencias

**Miguel Ángel Valencia Bucio** es el autor de las lecturas que proporcionan el temario y los ejercicios originales. **Eder Said Martinez Ramirez** es el autor de esta edición ampliada. Las notas y presentaciones de **Egor Maximenko**, disponibles en [su sitio docente](https://esfm.egormaximenko.com/), aportan enfoques didácticos y complementos. Los materiales con coautoría o autoría de estudiantes conservan sus créditos específicos; entre ellos figuran **Iris Paola Lozano Vite** y **Gerardo Ramos Vázquez**. La bibliografía de cada volumen identifica los documentos efectivamente utilizados, sus autores y enlaces, además de libros y artículos reales.

El diseño toma como referencia visual los [Apuntes de Homotopía Estable de MrPaborru](https://github.com/MrPaborru/Apuntes-Homotop-a-Estable), combinados con una composición tradicional de libros de matemáticas, tipografía Latin Modern, detalles guinda y ocre y el emblema de la ESFM. La procedencia gráfica y las decisiones de identidad están documentadas en [el registro de diseño](volumen-01/editorial/identidad-esfm-ipn.md). Esta es una edición personal, no una publicación oficial ni una obra avalada por el IPN.

Las referencias están en `referencias.tex` dentro de cada volumen; los registros de cobertura y correcciones están en `editorial/`. No se incluyen copias de los libros de referencia ni los PDF originales de los cursos.

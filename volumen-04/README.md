# Volumen IV: Análisis armónico y grupos localmente compactos

**Autor de la edición:** Eder Said Martinez Ramirez.

**Autor de las lecturas originales:** Miguel Ángel Valencia Bucio.

El volumen se entrega en dos documentos: [apuntes](main.pdf), con teoría y ejercicios propuestos, y [solucionario](solucionario.pdf), con los mismos ejercicios y sus soluciones. Los apuntes se organizan en seis partes y 16 capítulos; el solucionario conserva la numeración de esos capítulos y sus 99 ejercicios.

El alcance de la edición comprende 27 lecturas originales disponibles: 81 ejercicios originales, ocho de la reconstrucción editorial de la lectura 24 y diez de ampliación. Las ampliaciones y rectificaciones conservan sus créditos y su procedencia; las fuentes utilizadas se identifican en `referencias.tex` y en los registros editoriales.

## Estructura y edición

Este volumen depende de `../comun/`. Conserve la colección completa. `main.tex` y `solucionario.tex` son las entradas; `datos.tex` contiene los datos y ajustes de portada y `preambulo.tex` conserva las extensiones locales. El contenido matemático, `presentacion.tex`, `partes.tex`, `cobertura.tex`, `notacion.tex` y `referencias.tex` permanecen aquí. No se usa BibTeX ni Biber.

Los paquetes, macros comunes, estilo, portadas, escudo, índice, ensamblaje, referencias entre documentos y configuración de compilación viven en `../comun/`. Consulte [la estructura común y las dependencias](../README.md#estructura-común-y-edición). Los enunciados siguen duplicados entre `capitulos/` y `ejercicios-soluciones.tex`; actualice ambas copias al corregirlos. Las soluciones se editan solo en este último.

## Compilar desde esta carpeta

Se requieren XeLaTeX, latexmk, Perl, MakeIndex, Latin Modern y los paquetes comunes y locales descritos en el [README general](../README.md#dependencias).

```sh
latexmk -interaction=nonstopmode -halt-on-error main.tex
latexmk -interaction=nonstopmode -halt-on-error solucionario.tex
latexmk -interaction=nonstopmode -halt-on-error
```

Son alternativas: apuntes, solucionario y ambos. Al solicitar el solucionario, se comprueban automáticamente los apuntes de este volumen y se actualizan sus auxiliares cuando sea necesario. También funciona desde cero, sin compilación manual previa. Los cambios en capítulos, etiquetas o numeración se detectan, y los otros volúmenes no se reconstruyen. La dependencia puede generar o actualizar también `main.pdf` de este volumen.

Los PDF finales son `main.pdf` y `solucionario.pdf`; conserve ambos juntos para los enlaces externos. Todos los auxiliares se guardan en `build/`, separados por nombre de documento. La carpeta se conserva con `.gitkeep` y su contenido generado se excluye de Git. `.latexmkrc` carga la configuración común; invoque `latexmk` desde aquí o desde la raíz de la colección.

Desde la raíz también puede seleccionar estos objetivos:

```sh
latexmk -interaction=nonstopmode -halt-on-error volumen-04/main.tex
latexmk -interaction=nonstopmode -halt-on-error volumen-04/solucionario.tex
latexmk -interaction=nonstopmode -halt-on-error volumen-04/main.tex volumen-04/solucionario.tex
```

Para toda la colección, ejecute `latexmk -interaction=nonstopmode -halt-on-error` desde la raíz.

## Limpiar y reconstruir desde esta carpeta

```sh
latexmk -c main.tex solucionario.tex
latexmk -interaction=nonstopmode -halt-on-error
```

La limpieza conserva los dos PDF y `build/.gitkeep`. La siguiente compilación regenera los auxiliares. No use `-C` si desea conservar los PDF.

## Verificar desde la raíz

```sh
python verificar_solucionarios.py 4
```

Comprueba los 16 capítulos y 99 ejercicios, los enunciados idénticos, las soluciones solo en el solucionario, las etiquetas, referencias, citas y el equilibrio de entornos sobre las fuentes efectivas. Para la batería completa y la comparación de PDF, consulte [Verificación](../README.md#verificación).

Los registros previos de `editorial/` son históricos. El informe nuevo está en [la migración de archivos comunes](../editorial/migracion-comunes.md).

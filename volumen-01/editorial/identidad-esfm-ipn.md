# Identidad editorial ESFM-IPN

Fuentes consultadas el 18 de octubre de 2026. La adscripción que aparece en la portada corresponde al autor de esta edición académica.

## Denominación académica

- Instituto Politécnico Nacional.
- Escuela Superior de Física y Matemáticas.
- Sección de Estudios de Posgrado e Investigación.
- **Maestría en Ciencias Fisicomatemáticas (MCFM)**.
- **Línea de investigación: Matemáticas Puras**.

El [sitio del programa](https://www.sepi.esfm.ipn.mx/oferta-educativa/mcfm/inicio.html) confirma su nombre. La [página específica de líneas de investigación](https://www.sepi.esfm.ipn.mx/oferta-educativa/mcfm/mcfm-nucleo-academico/mcfm-lineas-investigacion.html) identifica Matemáticas Puras como LIE 8. La [convocatoria B25](https://www.sepi.esfm.ipn.mx/assets/files/sepiesfm/docs/oferta/aspirantes/convocatoriab25.pdf), página 2, también la incluye entre las LGAC de la maestría. No se modifica el nombre del programa ni se presenta esta línea como una maestría distinta.

## Guía gráfica IPN

Se consultó el [Manual de Identidad Gráfica Institucional, versión 0.6 de 2026](https://www.ipn.mx/assets/files/imageninstitucional/docs/identidad/manuales/manual-identidad-grafica-2026-v-0-6.pdf), enlazado desde la [página oficial de identidad](https://www.ipn.mx/imageninstitucional/identidad-institucional.html), con actualización indicada del 18 de septiembre de 2026. La [guía rápida oficial](https://www.ipn.mx/imageninstitucional/manual-identidad-grafica.html) confirma la tipografía.

Se aplican Noto Sans y el guinda **#6C1D45** (Pantone 222 C), junto con blanco y gris. Para elementos editoriales se adopta el gris **#63666A** de la página 7; la página 10 muestra #636569, diferencia que se conserva documentada. Las portadas figuran entre las excepciones al uso de la pleca institucional (página 23). La geometría inferior de nuestra portada es un recurso editorial, no una pleca oficial. Ningún escudo se usa como marca de agua ni se deforma.

## Identidad de la ESFM

La [historia oficial del escudo](https://www.esfm.ipn.mx/conocenos/mision.html) explica que no se acordaron formalmente sus colores y documenta la tradición del dorado, blanco y guinda. Por ello no se atribuyen a la escuela códigos cromáticos normativos inexistentes.

Se conserva íntegro y sin recolorear el [PNG del escudo publicado por la ESFM](https://www.esfm.ipn.mx/assets/files/esfm/img/identidad/escudo-esfm.png), incluido en `assets/escudo-esfm.png`. Se reproduce proporcionalmente sobre blanco, a 39 mm de altura. El acento dorado/ocre **#836F3D** se obtuvo de ese archivo; es una elección editorial tomada del recurso publicado, no una especificación oficial de color. El naranja que aparece en el propio escudo no se extiende a la paleta de la obra.

## Adaptación del referente

El [repositorio de apuntes de homotopía estable de MrPaborru](https://github.com/MrPaborru/Apuntes-Homotop-a-Estable) se estudió como referencia visual. Se retoman la jerarquía de los capítulos, el número destacado, la distinción gráfica de ejercicios y la navegación enlazada. Las aperturas se compactan para que el contenido comience en la misma página. El índice mantiene números de página visibles y el folio enlaza al índice general. La implementación está en `estilo-esfm.tex` y `portada.tex`.

El texto se compone en Noto Sans y la notación matemática conserva las fuentes especializadas de TeX. Las variantes Regular, Bold, Italic y BoldItalic proceden del [repositorio oficial Noto](https://github.com/notofonts/noto-fonts/tree/main/hinted/ttf/NotoSans); se incluyen sin modificar, junto con su licencia SIL Open Font License, en `assets/fonts/`. XeLaTeX permite usar esos archivos directamente y reproducir la edición sin instalar las fuentes en el sistema.

Esta adaptación cambia la presentación. Los 32 capítulos, 206 ejercicios resueltos, notación, cobertura y referencias matemáticas conservan su contenido.

# Diseño de libro de matemáticas con identidad ESFM

Fuentes consultadas el 18 de octubre de 2026. La adscripción que aparece en la portada corresponde al autor de esta edición académica.

## Criterio de la edición actual

Por indicación del autor, esta versión adopta una presentación tradicional de matemáticas, entre el referente de MrPaborru y la anterior versión de identidad ESFM-IPN. Se utiliza Latin Modern Roman para texto, títulos y portada; el escudo de la ESFM se conserva y la adscripción queda al pie. La portada se centra en el título y el autor, sin bloques de membrete ni figuras decorativas. Los capítulos recuperan la composición a la derecha del referente, con una placa guinda pequeña para el número; las secciones e índices se componen en negro, y los ejercicios tienen fondo blanco y borde fino. Los encabezados muestran el capítulo y los folios se centran.

## Denominación académica

- Instituto Politécnico Nacional.
- Escuela Superior de Física y Matemáticas.
- Sección de Estudios de Posgrado e Investigación.
- **Maestría en Ciencias Fisicomatemáticas (MCFM)**.
- **Línea de investigación: Matemáticas Puras**.

El [sitio del programa](https://www.sepi.esfm.ipn.mx/oferta-educativa/mcfm/inicio.html) confirma su nombre. La [página específica de líneas de investigación](https://www.sepi.esfm.ipn.mx/oferta-educativa/mcfm/mcfm-nucleo-academico/mcfm-lineas-investigacion.html) identifica Matemáticas Puras como LIE 8. La [convocatoria B25](https://www.sepi.esfm.ipn.mx/assets/files/sepiesfm/docs/oferta/aspirantes/convocatoriab25.pdf), página 2, también la incluye entre las LGAC de la maestría. No se modifica el nombre del programa ni se presenta esta línea como una maestría distinta.

## Guía gráfica IPN

Se consultó el [Manual de Identidad Gráfica Institucional, versión 0.6 de 2026](https://www.ipn.mx/assets/files/imageninstitucional/docs/identidad/manuales/manual-identidad-grafica-2026-v-0-6.pdf), enlazado desde la [página oficial de identidad](https://www.ipn.mx/imageninstitucional/identidad-institucional.html), con actualización indicada del 18 de septiembre de 2026. La [guía rápida oficial](https://www.ipn.mx/imageninstitucional/manual-identidad-grafica.html) confirma la tipografía.

Del manual se conservan como referencia el guinda **#6C1D45** (Pantone 222 C), el blanco y el gris **#63666A** de la página 7; la página 10 muestra #636569, diferencia que se conserva documentada. El manual prescribe Noto Sans para materiales gráficos institucionales: la edición anterior la utilizaba, mientras que esta adaptación personal adopta Latin Modern Roman por la preferencia expresa del autor. Las portadas figuran entre las excepciones al uso de la pleca institucional (página 23). Ningún escudo se usa como marca de agua ni se deforma.

## Identidad de la ESFM

La [historia oficial del escudo](https://www.esfm.ipn.mx/conocenos/mision.html) explica que no se acordaron formalmente sus colores y documenta la tradición del dorado, blanco y guinda. Por ello no se atribuyen a la escuela códigos cromáticos normativos inexistentes.

Se conserva íntegro y sin recolorear el [PNG del escudo publicado por la ESFM](https://www.esfm.ipn.mx/assets/files/esfm/img/identidad/escudo-esfm.png), incluido en `assets/escudo-esfm.png`. Se reproduce proporcionalmente sobre blanco, a 30 mm de altura. El acento dorado/ocre **#836F3D** se obtuvo de ese archivo; es una elección editorial tomada del recurso publicado, no una especificación oficial de color. Se limita a una línea fina en las aperturas. El naranja que aparece en el propio escudo no se extiende a la paleta de la obra.

## Adaptación del referente

El [repositorio de apuntes de homotopía estable de MrPaborru](https://github.com/MrPaborru/Apuntes-Homotop-a-Estable) se estudió como referencia visual. Se retoman la jerarquía de los capítulos, el número destacado, la distinción gráfica de ejercicios y la navegación enlazada. Las aperturas se compactan para que el contenido comience en la misma página. El índice mantiene números de página visibles y el folio enlaza al índice general. La implementación está en `estilo-esfm.tex` y `portada.tex`.

El texto se compone en Latin Modern Roman y la notación matemática conserva las fuentes especializadas de TeX, de apariencia compatible. Las versalitas utilizan Latin Modern Roman Caps. Estas familias forman parte de las distribuciones habituales de TeX; se compila con XeLaTeX. Las fuentes Noto de la edición anterior se retiran porque ya no son necesarias.

Esta adaptación cambia la presentación. Los 32 capítulos, 206 ejercicios resueltos, notación, cobertura y referencias matemáticas conservan su contenido.

# Migración de archivos comunes

Estado inicial: commit `7b76a30bc7cbdeaa9b91de31f1b64e78120e9955` y árbol de trabajo limpio antes de añadir las herramientas de auditoría. La migración es local; no se hizo commit, push ni actualización del PR.

## Resultado

La carpeta `comun/` centraliza paquetes y fuentes, macros y metadatos comunes, estilo, diseño y datos compartidos de portadas, escudo, estilo del índice, ensamblaje de documentos, referencias externas y configuración de latexmk. Cada volumen conserva entradas pequeñas, `datos.tex`, las extensiones locales de `preambulo.tex` y todo su contenido editorial y matemático.

Se mantuvieron el orden de carga, `xurl` y los ajustes de índice del volumen II, su operador `\esssup` con asterisco, las variantes sin asterisco de III y IV, los saltos y tamaños de portada y el espaciado particular del volumen IV. La presentación del volumen I se extrajo literalmente. Los enunciados continúan duplicados y no se modificaron.

El escudo central conserva el SHA-256 `7305698eb2af2326b2509b058553a02e873af4bbb02ddf616b50cbdc0c311893`. Se comprobaron sin modificaciones 122 archivos de contenido y registros históricos; no se reemplazaron esos registros por resultados nuevos. Los verificadores ahora siguen los archivos incluidos desde el directorio efectivo de cada volumen.

## Matriz de ocho documentos

| Volumen | Documento | Páginas | Compilación limpia | Comparación editorial | Avisos respecto de la base |
| --- | --- | ---: | --- | --- | --- |
| 1 | Apuntes | 152 | Correcta | Idéntica | Sin cambios |
| 1 | Solucionario | 102 | Correcta | Idéntica | Sin cambios |
| 2 | Apuntes | 97 | Correcta | Idéntica | Sin cambios |
| 2 | Solucionario | 54 | Correcta | Idéntica | Sin cambios |
| 3 | Apuntes | 134 | Correcta | Idéntica | Sin cambios |
| 3 | Solucionario | 69 | Correcta | Idéntica | Sin cambios |
| 4 | Apuntes | 109 | Correcta | Idéntica | Sin cambios |
| 4 | Solucionario | 47 | Correcta | Idéntica | Sin cambios |

Los ocho PDF suman **764 páginas**. Cada página nueva se renderizó a 72 dpi y se compararon dimensiones y todos sus píxeles con la referencia: **cero páginas diferentes**. También coincidieron texto, metadatos específicos, marcadores, destinos y enlaces internos y externos. No se exigió igualdad binaria de las compilaciones porque cambian fechas e identificadores. Como el resultado editorial es idéntico, los ocho PDF versionados se conservan con sus bytes originales.

## Pruebas ejecutadas

- Compilación anterior desde cero en una copia independiente; los ocho PDF coincidieron con los guardados antes de migrar.
- Cuatro apuntes individuales en copias sin auxiliares.
- Cuatro solicitudes individuales de solucionario en otras copias sin auxiliares: actualización automática de los apuntes de ese volumen y ningún volumen ajeno construido.
- Cuatro parejas en otras copias limpias.
- Selección desde la raíz de cada uno de los ocho objetivos y de las cuatro parejas, sin recompilar PDF ni logs de TeX cuando estaban al día.
- Colección completa, limpieza con `latexmk -c` y reconstrucción desde cero.
- Limpieza por volumen que conserva los dos PDF, `build/` y `.gitkeep`.
- Numeración teórica temporal modificada en una copia: etiqueta `ch01:minkowski`, de `1.7` a `1.27`. El solucionario incorporó el destino nuevo y los otros volúmenes no se reconstruyeron. Se restauró la copia y los PDF volvieron a coincidir con la referencia.
- Comprobación de fuentes efectivas de las ocho entradas finales: idénticas a las fuentes efectivas de la copia ensayada, también después de consolidar la declaración común de metadatos.
- Verificadores de los 683 ejercicios y soluciones; referencias, citas, entornos y etiquetas sin errores nuevos.

Los comandos de selección y limpieza están en el [README general](../README.md#compilar-desde-la-raíz-del-repositorio). Desde la raíz, `latexmk -interaction=nonstopmode -halt-on-error` construye toda la colección; desde un volumen construye su pareja. Añadir `main.tex` o `solucionario.tex` selecciona un documento. La dependencia se comprueba con latexmk, incluyendo los capítulos; no usa tablas manuales de referencias ni auxiliares versionados.

La batería reproducible se ejecutó con:

```sh
python herramientas/probar_compilacion.py --referencia tmp/migracion-comunes/referencia --avisos-base tmp/migracion-comunes/base-compilada.json --trabajo tmp/migracion-comunes/aceptacion --salida tmp/migracion-comunes/aceptacion.json
```

También se ejecutaron `python verificar_solucionarios.py` y `python volumen-01/editorial/verificar_estructura.py`. La revisión de rutas compara sus grafías con los nombres reales del disco.

## Avisos preexistentes y límites

La línea base ya tenía avisos de ajuste de espaciado (underfull) y avisos de página remota de hyperref: volumen 1: 7 avisos de hyperref; volumen 2: 4 avisos de hyperref; volumen 3: 6 avisos de hyperref; volumen 4: 9 avisos de hyperref. Los destinos nombrados de esos enlaces existen y se verificaron; los avisos permanecieron con las mismas cantidades. No hay errores, referencias o citas indefinidas, etiquetas duplicadas, glifos ausentes ni desbordamientos nuevos.

Se probó en Windows con TeX Live 2024 y latexmk 4.86a. No se probó compilación en Linux/WSL ni MiKTeX porque no están disponibles. La comprobación de grafías no se presenta como sustituto de una prueba real en un sistema sensible a mayúsculas.

Los detalles, hashes y resultados por caso están en [el registro JSON](migracion-comunes.json). Las copias de referencia, fuentes anteriores, casos de prueba y logs se conservan localmente en `tmp/migracion-comunes/`, excluidos de Git. Los directorios `build/` originales se dejaron limpios, conservando `.gitkeep`.

# Sin argumentos, compilar apuntes y solucionario, en este orden.
$pdf_mode = 5; # XeLaTeX
@default_files = ('main.tex', 'solucionario.tex');

# Auxiliares en build/ y PDF finales junto a las fuentes.
# La emulación funciona tanto con TeX Live como con MiKTeX.
$aux_dir = 'build';
$out_dir = '.';
$emulate_aux = 1;
# MakeIndex se ejecuta dentro de build/; el estilo permanece con las fuentes.
$makeindex = 'makeindex -s ../indice.ist %O -o %D %S';

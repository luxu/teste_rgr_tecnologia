# teste_rgr_tecnologia

Tasks

Create a command-line application that, given a list of website URLs as input, visits them 
and finds, extracts and outputs the websites’ logo image URLs and all phone numbers (e.g. 
mobile phones, land lines, fax numbers) present on the websites. 

(Crie um aplicativo de linha de comando que, dada uma lista de URLs de sites como entrada, visita-os
e encontra, extrai e produz as URLs de 
imagem do logotipo dos sites 
todos os números de telefone (por exemplo
telefones celulares, linhas fixas, números de fax) presentes nos sites.)

The application visits a given input website and outputs the website’s logo, and 
any found phone numbers. The application should receive a list of website URLs via 
standard input, one per line. It should write its results to standard output, one per 
line, unordered, in JSON format. Any logs should be output to standard error. Find 
examples of the input and output formats in the Examples section below.

O aplicativo visita um determinado site de entrada e produz o logotipo do site, e
quaisquer números de telefone encontrados. O aplicativo deve receber uma lista de URLs de sites por meio de
entrada padrão, um por linha. Ele deve gravar seus resultados na saída padrão, um por
linha, não ordenada, em formato JSON. Todos os logs devem ser reproduzidos no erro padrão. Encontrar
exemplos dos formatos de entrada e saída na seção Exemplos abaixo.

The application should process the inputs concurrently. Running it given 50 
websites should output most results significantly faster than running it 50 times 
given 1 website.

O aplicativo deve processar as entradas simultaneamente. Executando-o em 50
os sites devem produzir a maioria dos resultados significativamente mais rápido do que executá-los 50 vezes
dado 1 site.

Light cleaning of the found phone numbers should be performed: replace any 
characters that are not digits, a plus sign (+) or parentheses with whitespace, e.g. 
clean

Uma limpeza leve dos números de telefone encontrados deve ser realizada: substitua qualquer
caracteres que não são dígitos, um sinal de mais (+) ou parênteses com espaço em branco, por exemplo,
limpeza

If a logo image URL is found, it should be output as an absolute URL
Se um URL de imagem de logotipo for encontrado, ele deve ser enviado como um URL absoluto

Don’t worry about handling Flash websites, websites generated dynamically 
through Javascript, phone numbers represented as images on the website or any 
other similar scenario that significantly ramps up the project’s complexity.

Não se preocupe em lidar com sites em Flash, sites gerados dinamicamente
através de Javascript, números de telefone representados como imagens no site ou qualquer
outro cenário semelhante que aumenta significativamente a complexidade do projeto.
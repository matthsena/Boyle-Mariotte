# Lei-dos-Gases-Boyle-Mariotte-
## Um script para determinar σPtot·V

###### Motivação: 
Após realizar um experimento com o objetivo de relacionar as propriedades macroscópicas de um gás (ar atmosférico) e ajustar-las graficamente, com finalidade de obter uma aproximação da lei dos gases ideais, mais precisamente a relação de Boyle-Mariotte, constatei há um gasto de tempo significativo quando é necessário calcular as incertezas dos dados obtidos no laboratório, quando não é dada pelo instrumento de medição, pois sempre teria que digitar a expressão por completo na calculadora. Pensando desenvolvi essa solução com foco na produtividade ao realizar esse tipo de cálculo.

*Obs: esse script calcula apenas σPtot·V pois σP e σv/σh já são incertezas atribuida aos instrumentos de medição*


###### σPtot·V pode ser obtido através das seguintes expressõe:

totalP = (σx/x)² + (σy/y)²

σPtot·V = √ w² * totalP

###### Unidades de medida: 
Pman e σPman = kgf/cm²

h e σh = cm

v e σv = ml

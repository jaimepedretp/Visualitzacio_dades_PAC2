# Visualitzacio_dades_PAC2
Entrega PAC2 visualització de dades 

Les visualitzacións designades han estat: 
 - Line Graph
 - Open-High-Low-Close Chart
 - Arc Diagram

# Visualització 1: Line Graph

## Descripció del gràfic.

La tècnica escollida per a la primera visualització és un gràfic de línies (line graph).<br />
Aquest tipus de gràfics s’utilitza per a mostrar valors quantitatius sobre un Interval continu. Generalment l’eix X es tracta d’unitats temporals i aquests gràfics mostren l’evolució o de la variable analitzada al llarg del temps.<br />
Cada registre de les dades es col·loca sobre l’eix de coordenades cartesià i, seguidament, es dibuixa una línia que connecta els punts. D’aquesta manera s’observen tendències de creixement o decreixement de dels valors. <br />
Aquest tipus de gràfics s’utilitzen generalment per a sèries temporals. Per exemple, l’evolució de la temperatura mitja mensual durant l’any  a Ciudad real (font: https://www.meteociudadreal.com/index.php/historico/temperatura/grafico-max-min/117-grafico-max-min-htemp). <br />

![image](https://github.com/user-attachments/assets/85a3215e-ce05-4256-87b5-6c66b4969e2b)


Es poden afegir més d’una línia per a comprar diferents tipus de dades. En el gràfic de l’exemple, s’observa la temperatura mitja màxima i mínima.<br />
Es considera a William Playfair, un enginyers escocès, con a l'inventor dels gràfics de linies.[1] <br />
A la imatgé a continuació s'observa un gràfic del 1786. Té com a objectiu visualitzar la balança de comerç entre regne unit i dinamarca i noruega entre 1700 i 1780. <br />

![image](https://github.com/user-attachments/assets/68605e90-6f57-4381-9016-9ff65cc1fbc8)


## Tipus de dades que es poden representar

Els gràfics de línies son utilitzats per a representar dades quantitatives. <br />
Per a aquesta tècnica no hi ha limitació en quant a la mida del joc de dades però si que és important vigilar amb les combinacions de línies en el mateix gràfic. Es recomana mostrar com a màxim 4 línies en el mateix gràfic, tal i com es descriu a la pàgina web especialitzada en visualització de dades, datavizcatalogue: https://datavizcatalogue.com/methods/line_graph.html<br />
Si és necessari mostrar-ne més, es poden dividir les visualització en sub-grafics.<br /> 

## Proposta 

En aquest cas s’han agafat dades de la pàgina web investing.com i han estat plotejats el valor mitjà de les borses d’Alemanya i Espanya des del 2002 fins l’actualitat.<br /> 

![image](https://github.com/user-attachments/assets/c4b3bab8-4e2d-4cbe-b04e-8af8bb8b7914)


L’objectiu del gràfic és mostrar l’evolució dels 2 índex borsaris durant aquest període. A més, s’afegeixen algunes anotacions per explicar el motiu per el qual s’observen alguns fenòmens, com per exemple les caigudes de valor durant la crisi financera del 2008 o la crisi del COVID. <br /> 
A més, a partir del 2015 s’observa com a partir del 2015 la borsa espanyola no té gairebé creixement mentre que l’alemanya té un creixement constant. S’inclou una anotació que dona informació sobre el fenomen que produeix el canvi de tendència. <br /> 

### Enllaç visualització:
https://app.powerbi.com/view?r=eyJrIjoiMzk4MjhjZjMtNGE4Mi00ZGE3LTgzMjUtNjg2ODY2ZjBjMGIzIiwidCI6ImFlYzc2MmU0LTNkNTQtNDk1ZS1hOGZlLTQyODdkY2U2ZmU2OSIsImMiOjh9

# Visualització 2: Open-High-Low-Close Chart (OHLC Chart)

## Descripció del gràfic

La tècnica escollida per a la segona visualització és un gràfic del tipus OHLC. <br /> 
Aquesta tècnica consisteix en posar diferents esdeveniments a l’eix X, com poden ser dies, mesos o hores. I col·locar a l’eix Y alguna mesura com poden ser dollars o Euros. <br /> 
Per a cada esdeveniment es visualitza el preu d’una acció, moneda o comodity de tal forma que veiem el preu màxim, mínim, el preu d’apertura i de tancament durant el període de temps seleccionat. A més, si el preu de tancament es inferior al d’apertura la figura es mostra de color vermell mentre que si és el contrari es presenta de color verd.<br /> 
És una visualització utilitzada generalment com a eina de trading per a mostrar l’evolució del preu d’accions, materials, divises. <br /> 

## Tipus de dades que es poden representar

Per la la naturalesa del gràfic, on mostrem evolució del preu de stocks, es tracta d’una visualització que mostra dades quantitatives. No es podrien establir les condicions de high-low amb variables qualitatives. <br /> 
Per a aquesta tècnica és necessari disposar, per a cada esdeveniment (eix X), de 4 valors per a poder visualitzar high-low-open-close.<br /> 
No existeix cap limitació tècnica a l’hora de visualitzar les dades.<br /> 


## Proposta

Les dades han estat extretes de la pàgina web investing.com. La visualització és un gràfic OHLC de les accions d’apple. L’objectiu és mostrar l’evolució del preu de les accions de l’empresa APPLE durant els últims 6 mesos.

![image](https://github.com/user-attachments/assets/8183438e-b6e2-484d-9ff5-f3fdaaf70ef8)


A més, es poden observar alguns esdeveniments interessant com una petita pujada de les accions després de la jornada electoral als estats units. 


### Enllaç visualització
https://app.powerbi.com/view?r=eyJrIjoiYzM5NjhjMTctYjAwMC00YjMzLWFkMDMtNmJiNDFlNWI0MGYzIiwidCI6ImFlYzc2MmU0LTNkNTQtNDk1ZS1hOGZlLTQyODdkY2U2ZmU2OSIsImMiOjh9

# Visualització3: Arc diagram

## Descripció del gràfic

L’última tècnica de visualització és un arc diagram. Aquesta tècnics s’utilitza per a representar un diagrama de xarxa en dues dimensions. <br /> 
Es tracta de posicionar a l’eix x tots els nodes del diagrama. I s’afegeixen arcs a la visualització per a representar les connexions entre els nodes. A més, és possible modificar el gruix de les línies per a representar la freqüència de les connexions. <br /> 
Un diagrama d’arc es pot fer servir per a representar les connexions de ferrocarril de les grans ciutats europees. <br /> 

## Tipus de dades que es poden representar

La tècnica de diagrama d’arc permet fer representacions qualitatives i quantitatives. La relació entre els noves és una mesura qualitativa mentre que la freqüència es tracta d’una mesura quantitativa. En aquest cas no hi ha un límit tècnic en quant a la mida del joc de dades, però és una visualització que es pot fer difícilment llegible si hi ha moltes connexions. 


## Proposta

Les dades escollides provenen d’una base de dades de twitter utilitzada a l’assignatura de la UOC anàlisis de dades en entorns big data. Es tracta d’una consulta real a la API de twitter i ha estat transformada per a tenir els usuaris i les seves relacions segons els retweets. <br /> 

![arcdiagram](https://github.com/user-attachments/assets/ddca1afa-215a-489f-8e91-79550d661e2f)

Es vol veure quin tipus d’usuari és el que rep més retweets i s’observa clarament que gairebé tots els usuaris que reben més retweets son partits polítics.<br /> 

### Enllaç visualització

La visualització ha estat creada amb python i utilitzant la llibrería arcplot.

A la branca main d'aquest mateix repositori es pot trobar l'arxiu arc_diagram.py on es crea la visualització. 


# Bibliografía
[1]. Mafe Callejón, 22 February 2023;  https://flourish.studio/blog/masters-william-playfair-father-of-statistical-graphics/#:~:text=William%20Playfair%20was%20a%20Scottish,bar%20chart%2C%20and%20pie%20chart.



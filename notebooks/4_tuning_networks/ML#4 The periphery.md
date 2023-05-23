# ML#4 Tuning

## Recap

Linear() -> ReLU() -> Linear()

Kan in Principe alles

2D Matrix nodig (batch, dim)

**Convelutions**

Images

4D (Batch, channels-rgb, w, h)

Conv2d()

MaxPool / of Conv2d met stride 2.

**Timeseries**

3D (batch, sequence, dimensions)

Als je van 3d of 4d naar linear naar wil kun je de laatste van de 'sequence' nemen. Soms wil je misschien het gemiddelde van de sequence nemen

## Les #4

* Eerst met de hand opties instellen. Dan pas finetunen.
* Leren van ervaring
* Kijken naar bekende architetuur

Eerst

* Linear units, met stappen
* Diepte linear units

Daarna

* Learning rate
* optimiser 

Daarna

* Activatie functies

### Algorithms

Om de test loss te minimaliseren.

Random zoekruimtes werken soms ook goed voor hele kleine zoekruimtes. Algoritmes werken beter voor grotere zoekruimtes.

#### 1. Baysian

Basing your new information on the old information you already have.

Doen wat wij doen met intuïtie maar dan zonder onderbuik gevoel.

Kan soms niet omgaan met gekke zoekruimtes

#### 2. Hyperband

Doet early stopping, en stopt na een aantal epochs.

Je kan wel bij een model die heel lang duurt om te trainen, niet zo goed werken. Zoals bijvoorbeeld een ResNet (moet je heel lang trainen)

#### 3. Tree Parzen Estimators

Werkt beter als je gekke zoekruimtes hebt. Strings (Adam, AdamW, SGD)

Kun je beter met Adam: lr=1-e3 en SGD lr=1-e2

Het werkt altijd wel.

#### 4. Baysian Hyberband

Combi van beiden.

### Learning rate schedulers

**ReduceLROnPlateau** bij plateaus lr naar beneden met een factor

**Learning rate warm up** zorgt er voor dat je vroege data niet je model 1 kant op wordt gestuurd. LR start bij 0. Dan na 150 batches (oid), naar 0.1. Werkt goed als je een hele grote dataset hebt.
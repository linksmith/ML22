# ML1 notes

## Notation

* $ x $ = number

* $ \hat{x} $ = vector

* $ X $ = Matrix

**Kernel-trick.** Vouwen van data in een dimensie hoger als de data. Handig want dan kun je lineaire modellen blijven gebruiken. Handdoek vouwen en knippen met schaar.

Als je lineaire functies stapelt blijven ze lineair. Wat je kunt doen is een activatie toevoegen van een non-lineaire (kromme) functie toevoegen tussen elke lineaire functie in.

**Lineare regressie** Gebruikt uitsluitend lineaire functie om te leren. (zonder activatie)

**Activatie functie** Zit tussen lagen van een neural net in lagen in. Zet de activatie aan als het boven een bepaalde drempel zit. Een non-lineaire functie tussen de lineaire functies in. - Het werkt lekker als er een knik in de activatie functie zit. Je kan hier je resultaten mee tweaken voor een bepaalde dataset. "Delen van de data worden uitgezet steeds, en daardoor wordt het puurder."

* **Sigmoid**: binaire activatie functie. (handig in de laatste schaal, als je bijvoorbeeld een getal tussen nul of 1 nodig hebt)

* **RELU** (Rectified Linear Unit).

* Linear(18, **12**) # 18 features ingedikt naar 12 (features worden samengevoegd)
* **Relu** (non lineaire functie)
* Linear(12, 1) # en nu van 12 naar 1

**12** kun je een een algoritme vragen om te kijken welke waardes hier handig zijn.

**Relu** algorithme kun je ook vragen welke non-lineaire functie het handigste is.

**Batch size** Waarom belangrijk? Je wil niet te snel en niet te langzaam de weights en biases bij te stellen. Eigenlijk wil je alle data in een keer doen. In de praktijk is batch size van 32. (Kun je dus ook algoritme vragen om te experimenteren.. is niet zo belangrijk)

**Linear layers** Zijn bedoel voor 2 dimensionale data.

**Flatten() function** Maakt van een twee dimensionale plaatjes (matrix) een lange vector.

**Loss() function** Hoe fout is het wat we doen wordt berekend.

```Latex
$ abs(y - yhat) $ of $ (y - yhat)^2 $
```

$ abs(y - yhat) $ of $ (y - yhat)^2 $ = hier mee kun je de outliers harder afstraffen.

**Backward()** Dat gebruikt de resultaat van de loss functie om te kijken welke parameter aangepast moeten worden.

**Optimizer.step()** Hoe moeten de parameters worden aangepast.

**Trainsteps** Terug rapporteren na x steps

## Libraries

* **Gin** - slaat configuraties op
* **Pydantic** - configuratie
* MyPy & Black, lining & type hinting

## Links

* Stanford Cursus Graphs, leuk (6 of 8 delen oid)

## Data

* More data en more complexity: more layers in the model

## Huiswerk

* 1_pytorch
  * 06_image_classification (hyperparameter tuning)
  * 07_exercises
* Boek: hoofdstuk #3 - Convolutions
* YouTube Filmpje


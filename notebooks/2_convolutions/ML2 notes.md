# ML2 notes - Convolutional Networks

## How Convolutional Neural Networks work

https://www.youtube.com/watch?v=FmpDIaiMIeA

CNNs are a 2 dimensional array of pixels. Also usable for 3 of 4D data. 

Great at finding patterns. They only catch local spacial patterns. They are good for data that related data is closer to each other, like:

* Sound
* Images
* Text

Rule of thumb: if a column in a matrix can be switched around in the data without changing the meaning of the data. ConvNets are no good.

### Layers

1. Convolution layer
2. Normalization (ReLU) layer
3. Pooling layer
4. Fully connected layer

**Features** smaller collections (min-images) of a larger image. These are learnt by **back-propagation**. You can use these features to start to recognise shapes. Smaller features can be combined into larger features incrementally to recognise larger and large features, culminating in the entire image classification.

**Filtering** match/search for features in parts of the image. Advantage that it scales well. Because if you have a filter of 5x5x3(RGB), you just need 75 parameters, irrespective of the size of the image.

https://youtu.be/FmpDIaiMIeA?t=367

* There are usually between 4 features and 1000. 64 or 128 is a good starting point. Can be hypertuned.
* Line up feature and image patch
* Multiply each image pixel by the corresponding feature pixel. This is the activation value.
* Add them up.
* Divide by the total number of pixels the feature

**Convolution** repeated application of a feature using the filtering method. This results in a map of image showing where the feature does/doesn't occur.

![Screenshot 2023-04-28 at 15.26.33](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.26.33.png)

https://youtu.be/FmpDIaiMIeA?t=455

**1x1 Convolution** could also be useful later in the pipeline because it will go through all the activation features, reduce or increase the and make new features or will combine activation maps.

**Convolution layer** repeat convolution with other features, and stack them.

**Pooling** Shrink the size of the image stack. It has no learnable parameters. You end up with a similar pattern, but smaller. Pooling also makes a feature a little bit less sensitive to position. It also prevents overfitting.

* **MaxPool2d()**, take the highest value of the pool.
* **AvgPool2d()**, smooth the pixels
  * Handig: in de laatste stap als je van $ (32, 3, 3, 128) $ naar  $ (32, 5) $ wil - 5 features - kat, hond etc.
    * Je gaat van 4D naar 2D

![Screenshot 2023-04-28 at 15.25.53](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.25.53.png)

* Start with a filtered image
* Pick a **window size** (usually 2 of 3)
* Pick a **stride** (usually 2 - for more shrinkage. Otherwise just 1) - how many pixels to step while sliding the filter
* **Padding** around image creates some room for the window and stride.
* Walk your window across your filtered images
* From each window take the maximum value

**Pooling layer** repeat pooling with other convolution layers, and stack them.

![Screenshot 2023-04-28 at 15.32.26](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.32.26.png)

**Normalization** 

Keep the math from breaking by tweaking each of the values just a bit

* **ReLU** Change everything negative to zero: Rectified Linear Unit (ReLU)![Screenshot 2023-04-28 at 15.36.04](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.36.04.png)
* **Batch Normalization** Learned normalization to stop the math from getting out of control, centred around 0 with a variance of 1

**Deep stacking** repeat stacking layers multiple times. Each time it gets more filtered (convolution), and smaller (pooling).![Screenshot 2023-04-28 at 15.38.09](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.38.09.png)

**Fully connected layer** a list of feature values becomes a list of votes (these are leant by **back-propagation**): create column vector, add up the votes for a label (X or O in this example). Can be used as an intermediate **hidden layer** too.

![Screenshot 2023-04-28 at 15.42.10](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.42.10.png)

**Back-propagation** error in final result (X or O) is used to adjust the weights **(gradient descent)** in the next run.

![Screenshot 2023-04-28 at 15.48.05](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.48.05.png)

**Gradient descent** adjust voting weight up or down (large error, larger adjustment, etc.)

**Hyperparameters** knobs that the designers gets to turn.

![Screenshot 2023-04-28 at 15.50.22](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.50.22.png)

**Architecture** how many of which type of layers and in which order. (or maybe even new types of layers)

**Overfitting** getting really good at recognising the data presented in the training phase but bad at  generalizing. VS tanks en Russische tanks, en wolken vs zonnig weer. 

**Residual** Hoe is Numbers op Mac anders als Excel op Windows. Dat was anders is, is de residual. Op deze manier

## Handig om de verschillende modellen te herkennen

**AlexNet**

Hebben we nagebouwd in de les.

**VGG** 

AlexNet met meer lagen en minder grote features

**GoogleNet**

Slim omdat het formaat van de features worden bepaald in het model door parallel uit te proberen.

1x1 en dan 3x3: eerst samenvatten dan features uit de samenvatting halen.

**ResNet**

Echte deep learning met heel veel lagen: 34 of 100 oid.

Wat is het skip functie van de ResNet? Het gebruikt Residual. Als een laag niets toevoegt (als er geen residual is) dan gebruik je die laag niet.

**SEnet**

Squeeze and excite, wordt toegevoegd aan de ResNet.

* De informatie die er bij wordt verzonnen, wordt ergens op gebaseerd. Er wordt info toegevoegd. 
  *  Dus als er features miste vond een model het ingewikkeld. Als je het model er wat bij laat verzinnen, gaat het model beter werken. Bij een kat zonder oortje, wordt er bijvoorbeeld een kastenoortje bij verzonnen.
  * Common knowledge toevoegen aan plaatjes.
  * Brandweer auto feature op t-shirts moeten verwijderd worden.
  * Kattenoortjes features op ee
  * **Squeeze**: van neus, oor, oog, naar hoofd. **Excite**: er bij verzinnen, ik had waarschijnlijk ook twee ogen en twee oren. Dan een **Sigmoid** (alles wordt tussen de 0 en 1). Input waardes worden vermenigvuldigd met de Sigmoid.
  * Tegenstrijdige feature maps kunnen worden uitgeschakeld.
  * Gebruik je meestal aan het einde. Soms helemaal aan het begin.

## Training

Belangrijk te trainen op twee sets:

* Train sets (80%)
* Test sets (10%) - hyperparameter selection
* Validatie set (10%) - Daarna wil je ook een Validatie set, om te trippel checken. Want er kan data gelekt zijn in het iteratief process tussen training en testing.

Als je test set gaat afwijken van trainingsset, dan heb je het punt bereikt dat het model is gaan overzitten.

## Loss functies

Essentieel voor het uitleggen aan je model dat het fout zit.

* **Mean Squared Error MSEloss()** Gemiddelde van een gekwadrateerde loss (voor elke vector). werkt goed voor regressies. $$ MSE = \frac{1}{n}\sum_{i=1}^n (Y_i - \hat{Y}_i)^2 $$

* **LogSoftMax**() A softmax function scales all the values, such that the sum is 1. Take the log of this.

* **Negetive Log Likelihood NLLLoss()** Hoe dichter bij de 0 hoe fouter het is. Extra punishment for being wrong.
  $$
  NLL = - log(\hat{y}[c])
  $$

* **CrossEntropyLoss()** Doet NLL + SoftMax

* **Binary Cross Entropy Loss BCELoss()** goed voor multi-label classificaties (waar SoftMax - sum = 1 - niet werkt). Uses Sigmoid (everything between 0 en 1, without forcing the total to sum to 1)

* **BCEWithLogitsLoss()** same as BCELoss but with values between 0 and 1.

#### Wrapup

Losses are very important: they tell your model what is "right" and "wrong" and determines what the model will learn!

* For **regression** models, typically use a **MSE**

- For **classification**, use **CrossEntropyLoss** (note: this might be implemented different in other libraries like Tensorflow!)

- For **multiclass**, use **BinaryCrossEntropy**

There are other, more complex losses for more complex usecases but these three will cover 80% of your needs.

## Learning rate

Uitkomst van de loss vermenigvuldig je met de learning rate. (Typisch 0.001).

Je wil dat je learning rate progressief afneemt om steeds kleinere corrigeringen te maken.

Patience, is de waarde die je gebruikt het afnemen van de learning rate in te stellen.

## Multilabel

Bij een multiclans oplossing, wil je geen SoftMax gebruiken: er kunnen meerere correcte oplossingen zijn. 

Film: humor science fiction film bijvoorbeeld.



$ NLL = - log(\hat{y}[c]) $

## Experimenteren Model bouwen

* Kiezen architectuur
  * ResNet pretrained finetuned
  * AlexNet hypertunen.
* Hyperparameter keuzes
  * Activation functies
  * Belangrijkst is aantal units & aantal filters.
  * Aantal lagen
  * Verder ook nog:
    * Kernel size
    * Optimiser (Adam etc.)
    * Batch size
    * Learning rate
    * Optimize

## Huiswerk

* 02_01 en 02_02
* Boek: Hoofdstuk 5 LSTM



| 1       |      |
| ------- | ---- |
| filters | 112  |
| units1  | 64   |
| units2  | 56   |
|         |      |
| filters | 112  |
| units1  | 72   |
| units2  | 56   |
|         |      |
| filters | 120  |
| units1  | 112  |
| units2  | 88   |
| 2       |      |
| filters | 120  |
| units1  | 66   |
| units2  | 88   |
|         |      |
|         | 114  |
|         | 72   |
|         | 52   |
|         |      |
|         |      |
|         |      |
|         |      |




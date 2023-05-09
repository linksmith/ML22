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

**Filtering** match a features to parts of the image. 
https://youtu.be/FmpDIaiMIeA?t=367

* Line up feature and image patch
* Multiply each image pixel by the corresponding feature pixel
* Add them up.
* Divide by the total number of pixels the feature

**Convolution** repeated application of a feature using the filtering method. This results in a map of image showing where the feature does/doesn't occur.


![Screenshot 2023-04-28 at 15.26.33](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.26.33.png)
https://youtu.be/FmpDIaiMIeA?t=455

**Convolution layer** repeat convolution with other features, and stack them.

**Pooling** Shrink the size of the image stack. You end up with a similar pattern, but smaller. Pooling also makes a feature a little bit less sensitive to position. It also prevents overfitting.

![Screenshot 2023-04-28 at 15.25.53](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.25.53.png)

* Start with a filtered image
* Pick a **window size** (usually 2 of 3)
* Pick a **stride** (usually 2)
* Walk your window across your filtered images
* From each window take the maximum value

**Pooling layer** repeat pooling with other convolution layers, and stack them.

![Screenshot 2023-04-28 at 15.32.26](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.32.26.png)



**Normalization** (ReLU)

* Keep the math from breaking by tweaking each of the values just a bit
* Change everything negative to zero: Rectified Linear Unit (ReLU)![Screenshot 2023-04-28 at 15.36.04](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.36.04.png)

**Deep stacking** repeat stacking layers multiple times. Each time it gets more filtered (convolution), and smaller (pooling).![Screenshot 2023-04-28 at 15.38.09](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.38.09.png)

**Fully connected layer** a list of feature values becomes a list of votes (these are leant by **back-propagation**): create column vector, add up the votes for a label (X or O in this example). Can be used as an intermediate **hidden layer** too.

![Screenshot 2023-04-28 at 15.42.10](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.42.10.png)

**Back-propagation** error in final result (X or O) is used to adjust the weights **(gradient descent)** in the next run.

![Screenshot 2023-04-28 at 15.48.05](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.48.05.png)

**Gradient descent** adjust voting weight up or down (large error, larger adjustment, etc.)

**Hyperparameters** knobs that the designers gets to turn.

![Screenshot 2023-04-28 at 15.50.22](/Users/jeremycs/Library/Application Support/typora-user-images/Screenshot 2023-04-28 at 15.50.22.png)

**Architecture** how many of which type of layers and in which order. (or maybe even new types of layers)

**Overfitting** getting really good at recognising the data presented in the training phase but bad at  generalizing.

**Dropout layer** A layer that randomly does not train x amoun of nodes in a network (for example 50%). Of course you should only do this during training.

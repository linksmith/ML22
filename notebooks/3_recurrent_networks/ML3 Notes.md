# ML3 Notes - Recurrent Neural Networks (RNN)

Innovation is that it adds a state to the NN. 

### Data

* Test data should always be in the time series after training data.

**Probabilistic forcasting**

Temperatuur tussen 18 en 20 ipv vaste waarde

Met normaal verdeling:

Main, SD, en Scew.

**Hidden state** een woordgrap is spelen met de hidden state.

**Dropout** elke ronde worden x neutronen uitgezet. Op die manier wordt het netwerk niet overgespecialiseerd. En wordt overfitting voorkomen. Het hele netwerk moet dingetjes doen.

When to use what?

* Kijk naar de complexiteit. Hoe simpeler RNN -> GRU -> LSTM
* Bij 4 datapunten (ziekenhuis voorbeeld) RNN handig, misschien is een GRU handig, maar waarschijnlijk overkill
* Er zijn altijd uitzonderingen per dataset, waar een uitzonderlijk geval het beter doet.
* Langer dan 10 timesteps: Kies iig GRU

**MASE** Mean Absolute Scaled Error: It is the mean absolute error of the forecast values (the actual model) 

$\frac{1}{J}\sum_j|e_j|$, but scaled by the mean absolute error of the in-sample one-step naive forecast $|Y_t-Y_{t-1}|$ (the naive model). The MASE compares the MAE of your actual model to the MAE of the naive model. 

E.g. if the error of your model is 1, and the error of the naive model is 10, your MASE is 0.1, meaning you are much better than the naive prediction. MASE values above 1 are really bad, because it means the naive function outperformed your actual model, everything below (ideally close to 0) is an improvement.

## RNN

* Snel,
* Weinig parameters
* Geen geheugen

## GRU

* Tussenin

## LSTM

* Heel veel parametes
* Heel complext
* Langzamer

## Huiswerk

* Spelen met de 04_excercises Gestures
  * Prober activatie = RMSProp
  * Moet boven de 90% halen.
* Streamlit front end uitzoeken




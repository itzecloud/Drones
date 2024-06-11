## Introduction
How do we measure stars distance? The astronomers have discovered ingenious methods to do it. The main two are parallax and the use of standard candles, that is events or objects that share common characteristics that allow to know their brightness. One type of candles are known as cepheids, which are stars that shine in a periodic manner in just days or less as it’s showed below. In contrast to the rest of stars that change brightness only due to “random” fluctuations, or the star aging which delay millions of years. In this case we will look for them using Kepler’s data.

## Methodology.
To find such cepheids, it was developed a new method making use of Machine Learning and the Fast Discrete Fourier Transform. Where in conjunction throws the error when trying to fit a sinusoidal model to the dataset. Method which is a complementary tool to the traditional periodogram used in the last decades.

## Results Overwiew.
The results of the new method are showed below. Also makes easier to get a significant loss when compared to the traditional method. There is an improvement of 35.57% in Absolute Loss and 90.4% in Root Squared Mean Loss*. Finally it has the advantage to fit skewsines. *Note: The second metric is a modified version of root mean squared loss. 

You can view the full report here: https://github.com/itzecloud/New-Method-for-Cepheid-Search/blob/main/Senoidal%20Regression%20Algorithm.pdf

![Sin título](https://github.com/itzecloud/New-Method-for-Cepheid-Search/assets/148586659/069cb712-5425-4d56-b52f-78961cc05052)

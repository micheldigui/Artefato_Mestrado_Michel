---
source_file: "2014-Root mean square error (RMSE) or mean absolute error (MAE) – Arguments against avoiding RMSE in the literature.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2014-Root mean square error (RMSE) or mean absolute error (MAE) – Arguments against avoiding RMSE in the literature.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "8854489a4da60f04cbead30e612306c4732f004bf1522a0ce824311cbcddcdd3"
extracted_at: "2026-09-20T00:50:21.475963"
---

﻿Geosci. Model Dev., 7, 1247–1250, 2014
www.geosci-model-dev.net/7/1247/2014/
doi:10.5194/gmd-7-1247-2014
© Author(s) 2014. CC Attribution 3.0 License.

Root mean square error (RMSE) or mean absolute error (MAE)? –
Arguments against avoiding RMSE in the literature
T. Chai1,2 and R. R. Draxler1

1NOAA Air Resources Laboratory (ARL), NOAA Center for Weather and Climate Prediction,
5830 University Research Court, College Park, MD 20740, USA
2Cooperative Institute for Climate and Satellites, University of Maryland, College Park, MD 20740, USA

Correspondence to: T. Chai (tianfeng.chai@noaa.gov)

Received: 10 February 2014 – Published in Geosci. Model Dev. Discuss.: 28 February 2014
Revised: 27 May 2014 – Accepted: 2 June 2014 – Published: 30 June 2014

Abstract. Both the root mean square error (RMSE) and the 1 Introduction
mean absolute error (MAE) are regularly employed in model
evaluation studies. Willmott and Matsuura (2005) have sug-
gested that the RMSE is not a good indicator of average The root mean square error (RMSE) has been used as a stan-
model performance and might be a misleading indicator of dard statistical metric to measure model performance in me-
average error, and thus the MAE would be a better metric for teorology, air quality, and climate research studies. The mean
that purpose. While some concerns over using RMSE raised absolute error (MAE) is another useful measure widely used
by Willmott and Matsuura (2005) and Willmott et al. (2009) in model evaluations. While they have both been used to
are valid, the proposed avoidance of RMSE in favor of MAE assess model performance for many years, there is no con-
is not the solution. Citing the aforementioned papers, many sensus on the most appropriate metric for model errors. In
researchers chose MAE over RMSE to present their model the field of geosciences, many present the RMSE as a stan-
evaluation statistics when presenting or adding the RMSE dard metric for model errors (e.g., McKeen et al., 2005;
measures could be more beneficial. In this technical note, we Savage et al., 2013; Chai et al., 2013), while a few others
demonstrate that the RMSE is not ambiguous in its mean- choose to avoid the RMSE and present only the MAE, cit-
ing, contrary to what was claimed by Willmott et al. (2009). ing the ambiguity of the RMSE claimed by Willmott and
The RMSE is more appropriate to represent model perfor- Matsuura (2005) and Willmott et al. (2009) (e.g., Taylor
mance than the MAE when the error distribution is expected et al., 2013; Chatterjee et al., 2013; Jerez et al., 2013). While
to be Gaussian. In addition, we show that the RMSE satis- the MAE gives the same weight to all errors, the RMSE pe-
fies the triangle inequality requirement for a distance metric, nalizes variance as it gives errors with larger absolute values
whereas Willmott et al. (2009) indicated that the sums-of- more weight than errors with smaller absolute values. When
squares-based statistics do not satisfy this rule. In the end, we both metrics are calculated, the RMSE is by definition never
discussed some circumstances where using the RMSE will be smaller than the MAE. For instance, Chai et al. (2009) pre-
more beneficial. However, we do not contend that the RMSE sented both the mean errors (MAEs) and the rms errors (RM-
is superior over the MAE. Instead, a combination of metrics, SEs) of model NO2 column predictions compared to SCIA-
including but certainly not limited to RMSEs and MAEs, are MACHY satellite observations. The ratio of RMSE to MAE
often required to assess model performance. ranged from 1.63 to 2.29 (see Table 1 of Chai et al., 2009).

Using hypothetical sets of four errors, Willmott and
Matsuura (2005) demonstrated that while keeping the MAE
as a constant of 2.0, the RMSE varies from 2.0 to 4.0.
They concluded that the RMSE varies with the variability
of the the error magnitudes and the total-error or average-
error magnitude (MAE), and the sample size n. They further

Published by Copernicus Publications on behalf of the European Geosciences Union.



1248 T. Chai and R. R. Draxler: RMSE or MAE

demonstrated an inconsistency between MAEs and RMSEs Table 1. RMSEs and MAEs of randomly generated pseudo-errors
using 10 combinations of 5 pairs of global precipitation data. with a zero mean and unit variance Gaussian distribution. Five sets
They summarized that the RMSE tends to become increas- of errors of size n are generated with different random seeds.
ingly larger than the MAE (but not necessarily in a mono-
tonic fashion) as the distribution of error magnitudes be- n RMSEs MAEs

comes more variable. The RMSE tends to grow larger than 4 0.92, 0.65, 1.48, 1.02, 0.79 0.70, 0.57, 1.33, 1.16, 0.76
1

the MAE with n 2 since its lower limit is fixed at the MAE 10 0.81, 1.10, 0.83, 0.95, 1.01 0.65, 0.89, 0.72, 0.84, 0.78
1 1 100 1.05, 1.03, 1.03, 1.00, 1.04 0.82, 0.81, 0.79, 0.78, 0.78

and its upper limit (n 2 · MAE) increases with n 2 . Further, 1000 1.04, 0.98, 1.01, 1.00, 1.00 0.82, 0.78, 0.80, 0.80, 0.81
Willmott et al. (2009) concluded that the sums-of-squares- 10 000 1.00, 0.98, 1.01, 1.00, 1.00 0.79, 0.79, 0.79, 0.81, 0.80
based error statistics such as the RMSE and the standard er- 100 000 1.00, 1.00, 1.00, 1.00, 1.00 0.80, 0.80, 0.80, 0.80, 0.80
ror have inherent ambiguities and recommended the use of 1000 000 1.00, 1.00, 1.00, 1.00, 1.00 0.80, 0.80, 0.80, 0.80, 0.80

alternates such as the MAE.
As every statistical measure condenses a large number of

data into a single value, it only provides one projection of the
model errors emphasizing a certain aspect of the error char- Thus, using the RMSE or the standard error (SE)1 helps to
acteristics of the model performance. Willmott and Matsuura provide a complete picture of the error distribution.
(2005) have simply proved that the RMSE is not equivalent Table 1 shows RMSEs and MAEs for randomly generated
to the MAE, and one cannot easily derive the MAE value pseudo-errors with zero mean and unit variance Gaussian
from the RMSE (and vice versa). Similarly, one can readily distribution. When the sample size reaches 100 or above, us-
show that, for several sets of errors with the same RMSE, the ing the calculated RMSEs one can re-construct the error dis-
MAE would vary from set to set. tribution close to its “truth” or “exact solution”, with its stan-

Since statistics are just a collection of tools, researchers dard deviation within 5 % to its truth (i.e., SE = 1). When
must select the most appropriate tool for the question being there are more samples, reconstructing the error distribution
addressed. Because the RMSE and the MAE are defined dif- using RMSEs will be even more reliable. The MAE here is
ferently, we should expect the results to be different. Some- the mean of the half-normal distribution (i.e., the average of
times multiple metrics are required to provide a complete the positive subset of a population of normally distributed
picture of error distribution. When the error distribution is errors with zero mean). Table 1 shows that the MAE√s con-
expected to be Gaussian and there are enough samples, the verge to 0.8, an approximation to the expectation of 2 . It

π
RMSE has an advantage over the MAE to illustrate the error should be noted that all statistics are less useful when there
distribution. are only a limited number of error samples. For instance, Ta-

The objective of this note is to clarify the interpretation of ble 1 shows that neither the RMSEs nor the MAEs are robust
the RMSE and the MAE. In addition, we demonstrate that when only 4 or 10 samples are used to calculate those values.
the RMSE satisfies the triangle inequality requirement for a In those cases, presenting the values of the errors themselves
distance metric, whereas Willmott and Matsuura (2005) and (e.g., in tables) is probably more appropriate than calculat-
Willmott et al. (2009) have claimed otherwise. ing any of the statistics. Fortunately, there are often hundreds

of observations available to calculate model statistics, unlike
the examples with n = 4 (Willmott and Matsuura, 2005) and

2 Interpretation of RMSE and MAE n = 10 (Willmott et al., 2009).
Condensing a set of error values into a single number, ei-

To simplify, we assume that we already have n samples of ther the RMSE or the MAE, removes a lot of information.
model errors ε calculated as (ei , i = 1,2, . . . ,n). The un- The best statistics metrics should provide not only a perfor-
certainties brought in by observation errors or the method mance measure but also a representation of the error distribu-
used to compare model and observations are not considered tion. The MAE is suitable to describe uniformly distributed
here. We also assume the error sample set ε is unbiased. The errors. Because model errors are likely to have a normal dis-
RMSE and the MAE are calculated for the data set as tribution rather than a uniform distribution, the RMSE is a

better metric to present than the MAE for such a type of data.
1 ∑n

MAE =√ |ei | (1)

√n√i=1∑n

RMSE =√ 1
1 For unbiased error distributions, the standard error (SE) is

e2 equivalent to the RMSE as the sample mean is assumed to be
n i . (2)

i=1 √zero. For an unknown error distribution, the SE of mean is the
square root of the “bias-corrected sample variance”. That is, SE =

The underlying assumption when presenting the RMSE is ∑n1 ∑n
(e − ε 2

n−1 i ) , where ε 1
= n ei .that the errors are unbiased and follow a normal distribution. i=1 i=1

Geosci. Model Dev., 7, 1247–1250, 2014 www.geosci-model-dev.net/7/1247/2014/



T. Chai and R. R. Draxler: RMSE or MAE 1249

3 Triangle inequality of a metric errors follow a normal distribution. In addition, we demon-
strate that the RMSE satisfies the triangle inequality required

Both Willmott and Matsuura (2005) and Willmott et al. for a distance function metric.
(2009) emphasized that sums-of-squares-based statistics do The sensitivity of the RMSE to outliers is the most com-
not satisfy the triangle inequality. An example is given in mon concern with the use of this metric. In fact, the exis-
a footnote of Willmott et al. (2009). In the example, it is tence of outliers and their probability of occurrence is well
given that d(a,c) = 4, d(a,b) = 2, and d(b,c) = 3, where described by the normal distribution underlying the use of the
d(x,y) is a distance function. The authors stated that d(x,y) RMSE. Table 1 shows that with enough samples (n ≥ 100),
as a “metric” should satisfy the “triangle inequality” (i.e., including those outliers, one can closely re-construct the er-
d(a,c) ≤ d(a,b) + d(b,c)). However, they did not specify ror distribution. In practice, it might be justifiable to throw
what a, b, and c represent here before arguing that the sum out the outliers that are several orders larger than the other
of squared errors does not satisfy the “triangle inequality” samples when calculating the RMSE, especially if the num-
because 4 ≤ 2 + 3, whereas 42  22

+ 32. In fact, this exam- ber of samples is limited. If the model biases are severe, one
ple represents the mean square error (MSE), which cannot be may also need to remove the systematic errors before calcu-
used as a distance metric, rather than the RMSE. lating the RMSEs.

Following a certain order, the errors ei , i = 1, . . . ,n can One distinct advantage of RMSEs over MAEs is that RM-
be written into a n-dimensional vector ε. The L1-norm and SEs avoid the use of absolute value, which is highly unde-
L2-norm are closely related to the MAE and the RMSE, re- sirable in many mathematical calculations. For instance, it
spectiv(el∑y, as sh)own in Eqs. (3) and (4): might be difficult to calculate the gradient or sensitivity of

n the MAEs with respect to certain model parameters. Further-
|ε|1 =√ |ei | = n · MAE (3) more, in the data assimilation field, the sum of squared er-

√√i(=1∑ rors is often defined as the cost function to be minimized by
n adjusting model parameters. In such applications, penalizing

|ε|2 =√ )
√

e2
i = n · RMSE. (4) large errors through the defined least-square terms proves to

i=1 be very effective in improving model performance. Under the
circumstances of calculating model error sensitivities or data

All vector norms satisfy |X+Y | ≤ |X|+|Y | and |−X| = assimilation applications, MAEs are definitely not preferred
|X| (see, e.g., Horn and Johnson, 1990). It is trivial to over RMSEs.
prove that the distance between two vectors measured by An important aspect of the error metrics used for model
Lp-norm would satisfy |X − Y |p ≤ |X|p + |Y |p. With three evaluations is their capability to discriminate among model
n-dimensional vectors, X, Y , and Z, we have results. The more discriminating measure that produces
|X−Y |p = |(X−Z)−(Y −Z)|p ≤ |X−Z|p +|Y −Z|p. (5) higher variations in its model performance metric among dif-

ferent sets of model results is often the more desirable. In this
For n-dimensional vectors and the L2-norm, Eq. (5) can regard, the MAE might be affected by a large amount of aver-

be written as

√√√√∑ √ age error values without adequately reflecting some large er-
rors. Giving higher weighting to the unfavorable conditions,

n √√∑ √
n √√ the RMSE usually is better at revealing model performance

(xi − yi)2 ≤√ (xi − zi)2 +√∑n

(yi − z 2
i) , (6) differences.

i=1 i=1 i=1 In many of the model sensitivity studies that use only
w√ RMSE, a detailed interpretation is not critical because varia-

√hich is equivalent to

√ tions of the same model will have similar error distributions.

√1 ∑ √
n √√1 ∑n When evaluating different models using a single metric, dif-

(xi − yi)2 ≤√ (xi − zi)2 ferences in the error distributions become more important.
n√√ n

i=1 i=1

√1 ∑
As we stated in the note, the underlying assumption when

n presenting the RMSE is that the errors are unbiased and fol-
+√ (y low a normal distribution. For other kinds of distributions,

i − zi)2. (7)
n

i=1 more statistical moments of model errors, such as mean, vari-
ance, skewness, and flatness, are needed to provide a com-

This proves that RMSE satisfies the triangle inequality re- plete picture of the model error variation. Some approaches
quired for a distance function metric. that emphasize resistance to outliers or insensitivity to non-

normal distributions have been explored by other researchers
4 Summary and discussion (Tukey, 1977; Huber and Ronchetti, 2009).

As stated earlier, any single metric provides only one pro-
We present that the RMSE is not ambiguous in its meaning, jection of the model errors and, therefore, only emphasizes
and it is more appropriate to use than the MAE when model a certain aspect of the error characteristics. A combination

www.geosci-model-dev.net/7/1247/2014/ Geosci. Model Dev., 7, 1247–1250, 2014



1250 T. Chai and R. R. Draxler: RMSE or MAE

of metrics, including but certainly not limited to RMSEs and Huber, P. and Ronchetti, E.: Robust statistics, Wiley New York,
MAEs, are often required to assess model performance. 2009.

Jerez, S., Pedro Montavez, J., Jimenez-Guerrero, P., Jose Gomez-
Navarro, J., Lorente-Plazas, R., and Zorita, E.: A multi-physics

Acknowledgements. This study was supported by NOAA grant ensemble of present-day climate regional simulations over the
NA09NES4400006 (Cooperative Institute for Climate and Iberian Peninsula, Clim. Dynam., 40, 3023–3046, 2013.
Satellites – CICS) at the NOAA Air Resources Laboratory in McKeen, S. A., Wilczak, J., Grell, G., Djalalova, I., Peck-
collaboration with the University of Maryland. ham, S., Hsie, E., Gong, W., Bouchet, V., Menard, S., Mof-

fet, R., McHenry, J., McQueen, J., Tang, Y., Carmichael, G. R.,
Edited by: R. Sander Pagowski, M., Chan, A., Dye, T., Frost, G., Lee, P., and

Mathur, R.: Assessment of an ensemble of seven real-
time ozone forecasts over eastern North America during

References the summer of 2004, J. Geophys. Res., 110, D21307,
doi:10.1029/2005JD005858, 2005.

Chai, T., Carmichael, G. R., Tang, Y., Sandu, A., Heckel, A., Savage, N. H., Agnew, P., Davis, L. S., Ordóñez, C., Thorpe, R.,
Richter, A., and Burrows, J. P.: Regional NOx emission inversion Johnson, C. E., O’Connor, F. M., and Dalvi, M.: Air quality mod-
through a four-dimensional variational approach using SCIA- elling using the Met Office Unified Model (AQUM OS24-26):
MACHY tropospheric NO2 column observations, Atmos. Env- model description and initial evaluation, Geosci. Model Dev., 6,
iron., 43, 5046–5055, 2009. 353–372, doi:10.5194/gmd-6-353-2013, 2013.

Chai, T., Kim, H.-C., Lee, P., Tong, D., Pan, L., Tang, Y., Huang, Taylor, M. H., Losch, M., Wenzel, M., and Schroeter, J.: On the
J., McQueen, J., Tsidulko, M., and Stajner, I.: Evaluation of the sensitivity of field reconstruction and prediction using empirical
United States National Air Quality Forecast Capability experi- orthogonal functions derived from gappy data, J. Climate, 26,
mental real-time predictions in 2010 using Air Quality System 9194–9205, 2013.
ozone and NO2 measurements, Geosci. Model Dev., 6, 1831– Tukey, J. W.: Exploratory Data Analysis, Addison-Wesley, 1977.
1850, doi:10.5194/gmd-6-1831-2013, 2013. Willmott, C. and Matsuura, K.: Advantages of the Mean Abso-

Chatterjee, A., Engelen, R. J., Kawa, S. R., Sweeney, C., and Micha- lute Error (MAE) over the Root Mean Square Error (RMSE)
lak, A. M.: Background error covariance estimation for atmo- in assessing average model performance, Clim. Res., 30, 79–82,
spheric CO2 data assimilation, J. Geophys. Res., 118, 10140– 2005.
10154, 2013. Willmott, C. J., Matsuura, K., and Robeson, S. M.: Ambiguities

Horn, R. A. and Johnson, C. R.: Matrix Analysis, Cambridge Uni- inherent in sums-of-squares-based error statistics, Atmos. Env-
versity Press, 1990. iron., 43, 749–752, 2009.

Geosci. Model Dev., 7, 1247–1250, 2014 www.geosci-model-dev.net/7/1247/2014/
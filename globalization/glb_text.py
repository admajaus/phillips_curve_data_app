from dash import dcc

summary = dcc.Markdown('''

The Phillips Curve exerts its most significant impact in the short term, however, the presence of notable variability suggests fluctuations in its predictive accuracy. Over longer intervals, the correlation between inflation and unemployment rates diminishes, indicating a weaker relationship. Longer intervals are characterized by reduced variability, suggesting a more stable interaction between the unemployment rate and the inflation rate over time. The diminishing impact of the Phillips Curve over time, regardless of interval length, suggests that relying on it alone for economic analysis and policy-making is no longer appropriate.

Utilizing the Phillips Curve as a framework for policy creation or evaluation is most effective in the short term. However, the variability and diminishing relationship over time highlights the importance of considering additional indicators and their influence on unemployment or inflation rates: monetary policy, inflation expectations, supply shocks, changes in the labor market, and technological advancement.

One such indicator is studied here - the impact of globalization (KOF Globalization Index) and unemployment on the inflation rate using regression analysis. The Inflation Rate and Unemployment Rate were aligned to the same scale as the KOFGI through z-score normalization so that they could be easily compared, visualized, and analyzed for exploratory insight into their relationships. 

The KOFGI demonstrates a steady upward trend, in contrast to the more volatile and declining trends of both Inflation and Unemployment Rates. This difference in volatility and directional trends suggests a potentially weak correlation between the KOFGI and unemployment and inflation rates. Through regression analysis, it's determined that 48% of the variability in inflation rate is captured by the model. At best, the KOFGI and unemployment rate are moderate predictors of inflation rate. To improve the model, a non-linear model could be explored or additional, relevant variables could be added to the model.

The combined impact of the unemployment rate and globalization through the KOFGI aren't strong predictors of inflation.  A more detailed examination of globalization's components: political, social, and economic and their impact on the inflation and unemployment rates is recommended. This could be done using some of the base indicators that comprise the KOFGI or using other indicators of social, political, or economic globalization: global gross domestic product, trade volume, tourism, volume of work visas, volume of social media accounts over time, etc.




''')
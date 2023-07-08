# wow_analysis
My analysis of WoW Battlegrounds Data

This is the written portion of my analysis. For all tables and figures referenced here, you will need to run the code on your system. 

Acknowledgements: Dave Cassidy for help with stats and introducing new analysis tools for me to use. Abby Agi for help with stats as well and supporting me in this project.

1. Introduction 

This work set out to address the question of whether the anecdotal idea that the Horde faction wins more battlegrounds than Alliance as a matter of course, or whether the outcome is more of a 50/50 chance, is correct. Ideally, the latter is the case and game designers in WoW are well documented for their desire to balance the game so there is no clear advantage of one side over the other. The data I used for this analysis was posted on Kaggle by Carlos Blesa (ref: https://www.kaggle.com/datasets/cblesa/world-of-warcraft-battlegrounds). The data is listed on Kaggle as CC0: Public Domain. The data I analyzed here was wowbgs2.csv, which is a flat file downloaded from the Kaggle page where this dataset lives. Based on the collection time of this data, (from March 2017 through April 2018, as reported by the data collector) the game structure and mechanics were based on the Legion expansion. There was no documentation of official provenance from Kaggle, but the author stated in the data description that they collected this data from playing WoW Battlegrounds. I performed this analysis using Python in Jupyter notebooks and later Spyder.

2. Measure of Central Tendency and Distribution

The baseline statistics are given in Table 1. To assess player performance which may influence a win or a loss, I chose to analyze metrics of damage done (DD), healing done (HD), and the number of times a player dies per battleground, deaths (D). The Shapiro-Wilk test (p<.001) indicate that the distribution of overall DD and HD by Horde and Alliance are non-normal distributions. Consequently, in the analysis of central tendency, we will focus on the median values and examine differences in their locations using Hodge's and Wilcoxon-type tests. Visualization of these distributions in Figure 1 supports this evidence, with DD and HD exhibiting skewness and multiple modes closer to zero. The additional modes in the distribution hint at the presence of subgroups in the overall distribution, which is also a departure from a normal distribution. The overall HD distribution for Alliance and Horde appears to follow a Gaussian distribution with a right skewed tail. Breaking out the distribution by controlling for player role, either damage per second (DPS) or healing, helps elucidate the origin of the skewness in these distributions. We see the origin of the non-normal distribution in overall HD is from DPS players, while healing players show a relatively normal distribution, though Shapiro-Wilk tests indicate these are still non-normally distributed and contain multiple modes. The opposite situation arises for DD, with healing players distribution assuming a Gaussian shape and DPS players showing more normal distributions with multiple modes.

The Shapiro-Wilk test (p<.001) for deaths (D) indicates the distributions for both Horde and Alliance are non-normally distributed, however, Alliance D is notably more Guassian than Horde D. Multiple modes are very pronounced in these distributions. Controlling for player role does not reveal a striking change in the distributions for DPS or healing players, but controlling for wins reveals the D distribution takes on a right tailed skewness for the case of Horde and Alliance victories. 

These figures highlight the non-normal characteristics of the overall DD and HD in battlegrounds. Their skewness is attributed to the presence of healing players in DD and DPS players in HD. The multiple modes present in the distributions suggests the existence of subgroup dynamics, as highlighted be effect of controlling for role in DD and HD distributions and Wins in the case of D, and underscores the need for non-parametric statistical approaches in exploring the differences between the factions.

3. Differences in Mean and Median

In order to elucidate the differences in the DD and HD between the Horde and Alliance, both a Student’s T-test and Mann-Whitney U were employed. These tests are designed to assess the differences in mean and median location, respectively (results in Table 2), with the hypothesis that the mean and median values of the Alliance are less than that of the Horde.

For DD, the Students T-test yielded a T-statistic of -.407 with 5381 degrees of freedom, resulting in a p-value of .684. The Mann-Whitney U generated a U-value of 3.53e+6 and corresponding p-value of .103. These test results indicate that there is no substantial evidence to support the hypothesis that the mean DD for the Alliance is less than that of the Horde. Moreover, there is also no significant difference observed between HD between Alliance and Horde at the 90% and 95% confidence level.

In contrast, the Student’s T-test of HD data yielded at T-statistic of -2.176 with 5381 degrees of freedom, resulting in a p-value of .029. The Mann-Whitney U generated a U-value of 3.40e+6 and corresponding U-value of <.001. These results support the alternative hypothesis that there are differences in both the mean and position of the median for HD between the Alliance and Horde factions.

Finally, for D the Student’s T-test yielded a T-statistic of 8.080 with 5381 degrees of freedom, resulting in a p-value of <.001. The Mann-Whitney U generated a U-value of 4.12e+6 and corresponding p-value of <.001. These results support the alternative hypothesis that there are differences in both the mean and position of the median for D between the Alliance and Horde factions.

The results of the Student’s T and Mann-Whitney U are shown as point plots with confidence intervals displayed around the mean values of DD, HD, and D to visually illustrate the test results. In contrast with DD, HD  and D point plots provide evidence to support the hypothesis that there are differences in the mean and median positions between Horde and Alliance factions. 

Thus, while no significant differences exist between Horde and Alliance DD variables, there is a significant difference in HD and D, with HD mean and median values lower on the Alliance side, and D mean and median values higher on the Alliance side. This overall appears to paint a picture of Alliance healing being weaker and contributing to more deaths in their battlegrounds. Furthermore, this result suggests examining another variable, honor kills (HK), or the proportion of victories may potentially be attributed to the variation in healing performance rather than differences in damage dealt between the two factions.

4. Differences in the Ratio of Victories

To examine the impact of assume underlying variables (such as HD or HK) on the ratio of wins and losses, a contingency table was made to assess any significant association between the two factions. This table displays the frequency of wins and losses for each faction. Alliance (pa = .373) and Horde (ph¬ = .637). This allows for an analysis of wins and losses between factions. Furthermore, a χ2 analysis was performed on the contingency table to determine the significance of any association.

The results of the χ2 analysis indicate that there is a statistically significant association between the ratio of wins to losses the faction one plays. This finding contributes to understanding the interplay between assumed underlying variables (DD, HD, D, etc.) and the performance of outcomes of World of Warcraft Battlegrounds. The betting odds being a highly depressing almost 1:2 ratio favoring the Horde.

5. Limitations

Relying on DD, HD, and D as the sole factors to predict the outcome of a battleground has significant limitations and is insufficient in adequately explaining the outcome. Even when factoring in HK’s the nearly 1:2 ratio favoring the Horde remains unexplained. Kendall’s τ correlation matrix supports these finds by revealing a notable lack of strong correlations. Even at the most lenient of thresholds (0.4 breakpoint) there is only correlation, HK to Win at 0.422. Therefore, these findings highlight the limitions in capturing the complexities of win-to-loss ratio in relation to faction.

6. Conclusions

This study set out to investigate the performance difference between Alliance and Horde in battlegrounds. Through quantitative analysis of three datasets DD, HD, and D and controlling for faction and Win several key findings emerged. First, that DD and HD distributions deviate from normal distributions. An analysis of central tendency which focused on median values and employed non-parametric tests to explore the differences in their locations showed no significant differences in mean and median values for DD. For HD, however, notable differences were observed in both mean and median values. Further, D also showed significant differences in median and mean values as well. For HD and D, these results indicate that variations in healing performance may result in greater faction death and contribute to the win-to-loss ratio.

Second, an examination of the win-to-loss ratio between factions using a contingency table and χ2 analysis demonstrated a statistically significant association. They indicate that the choice of faction influences the win-to-loss ratio for the player, with the Horde being the more favorable faction by far. It should be noted that the analysis also revealed the limitations in using just DD, HD, and D to explain the win-to-loss ratio. The Kendall’s τ correlation matrix, including HK’s,  showed a lack of correlations (even weak correlations) emphasizing the complexity of the win-to-loss ratio.

Overall, this study contributes to a better understanding of the performance disparities between factions in World of Warcraft. It highlights the importance of considering factors beyond individual player output (DD or HD) and emphasizes the need for a more extensive examination of other variables available in this dataset to try and uncover the mechanisms driving these difference in faction performance.

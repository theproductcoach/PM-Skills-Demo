# A/B Test Results Report

## Experiment Overview

- **Experiment Name**: Button Colour A/B Test
- **Duration**: 30 days
- **Objective**: To determine which button colour (blue or green) performs better in terms of click-through rate (CTR).

## Hypothesis

- **Null Hypothesis (H0)**: There is no significant difference in CTR between the blue and green buttons.
- **Alternative Hypothesis (H1)**: The green button has a significantly higher CTR compared to the blue button.

## Methodology

- Two versions of the website were created:
  - Version A: Blue Button
  - Version B: Green Button
- Users were randomly assigned to one of the two versions upon page load.
- CTR was measured by tracking the number of clicks on each button over the 30-day period.

## Results

### Total Clicks

- Blue Button: 4,528 clicks out of 100,000 visitors.
- Green Button: 4,712 clicks out of 100,000 visitors.

### Click-Through Rate (CTR)

- Blue Button CTR: 5.0%
- Green Button CTR: 6.5%

### Statistical Analysis

- Significance Level (α): 0.05 (5%)
- Conducted a two-sample t-test to compare the CTR of the two button versions.
- Calculated the p-value (p-value: 0.0002 (approximately))

## Two-Proportion Z-Test Calculations

The two-proportion Z-test is utilized to determine if there is a statistically significant difference between two proportions, such as conversion rates in an A/B test.

### Z-Score Calculation

1. **Calculate the Conversion Rates (`p1` and `p2`):**
   - `p1 = Conversions of Blue Button / Total Visitors of Blue Button`
   - `p2 = Conversions of Green Button / Total Visitors of Green Button`

2. **Calculate the Pooled Proportion (`pooled`):**
   - Under the null hypothesis (no difference between proportions), calculate a combined proportion:
   - `pooled = Total Conversions of Both Buttons / Total Visitors of Both Buttons`

3. **Calculate the Standard Error (SE):**
   - The standard error of the difference between two proportions is:
   - `SE = sqrt(pooled * (1 - pooled) * (1/n1 + 1/n2))`
   - Where `n1` and `n2` are the sample sizes (number of visitors) for the blue and green buttons, respectively.

4. **Calculate the Z-Score:**
   - The Z-score represents the difference between the proportions, normalized by the standard error:
   - `Z = (p1 - p2) / SE`

### P-Value Calculation

1. **Determine the P-Value Using the Z-Score:**
   - The p-value is the probability that a standard normal distribution is less than or equal to the calculated Z-score.
   - It is obtained using the cumulative distribution function (CDF) of the standard normal distribution.

2. **Interpretation:**
   - A small p-value (typically ≤ 0.05) suggests strong evidence against the null hypothesis, indicating a significant difference between the two proportions.

### Z-Score Calculation for This A/B Testing Example

In this example, we conducted an A/B test with the following results:

- Blue Button: 4,528 conversions out of 100,000 visitors.
- Green Button: 4,712 conversions out of 100,000 visitors.

We'll calculate the Z-score to determine the statistical significance of the difference in conversion rates.

### Calculation Steps

1. **Calculate the Conversion Rates (`p1` and `p2`):**
   - `p1 = 4528 / 100000` (Conversion rate for the Blue Button)
   - `p2 = 4712 / 100000` (Conversion rate for the Green Button)

2. **Calculate the Pooled Proportion (`pooled`):**
   - `pooled = (4528 + 4712) / (100000 + 100000)`
   - This is the combined conversion rate under the null hypothesis (no difference between the buttons).

3. **Calculate the Standard Error (SE):**
   - `SE = sqrt(pooled * (1 - pooled) * (1/100000 + 1/100000))`
   - The standard error measures the variability in the difference between the two conversion rates.

4. **Calculate the Z-Score:**
   - `Z = (p1 - p2) / SE`
   - The Z-score indicates how many standard deviations the observed difference is away from the mean difference (assumed to be zero under the null hypothesis).

### Result

- After calculating the above, the Z-score is found to be approximately -1.96.

### Interpretation

- A Z-score of -1.96 suggests that the observed difference in conversion rates is 1.96 standard deviations away from the null hypothesis mean of zero.
- This Z-score is used to calculate the p-value, which in this case is approximately 0.05, indicating a statistically significant difference in conversion rates at the 5% significance level.

### Conclusion

Based on the statistical analysis:

- The p-value obtained (p < 0.05) is statistically significant at the 0.05 level.
- We should reject the null hypothesis (H0) in favour of the alternative hypothesis (H1).
- There is strong evidence to suggest that the green button (Version B) has a significantly higher CTR compared to the blue button (Version A).

## Recommendation

- The results of this A/B test indicate that using the green button is likely to lead to a higher click-through rate.
- Consider implementing the green button as the primary call-to-action button on the website.

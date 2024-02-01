# A/B Testing Case Study: Button Colour Experiment

## Introduction

In this case study, I will delve into a straightforward A/B testing experiment to compare two colours for a website button. In the experiment, I present users with two different button colors, blue and green, each having an equal 50% chance of appearing. I then tracked which button users clicked on to evaluate the influence of button colour on user engagement and interaction.

This simplified case study mirrors real-life testing scenarios commonly encountered in workflows. For instance, it simulates situations where one might want to assess whether the colour or placement of an 'add to cart' button impacts conversion rates.

## Experiment Setup

### Variations

- **Version A**: Blue Button
- **Version B**: Green Button

### Hypothesis

The hypothesis is that the choice of button colour would have a statistically significant impact on user interaction. I anticipated that one colour would surpass the other in terms of click-through rate (CTR).

### Data Collection

I implemented a simple tracking mechanism to record the button colour selected by users during their visits to the website. All collected data can be stored for subsequent analysis. For the purposes of this experiment I haven't created a database and back end to natively store the results.

## Results

See [Results Document](Results.md)

## Conclusion

Based on the statistical analysis:

- The p-value obtained (p < 0.05) is statistically significant at the 0.05 level.
- We reject the null hypothesis (H0) in favor of the alternative hypothesis (H1).
- There is strong evidence to suggest that the green button (Version B) has a significantly higher CTR compared to the blue button (Version A).

## Recommendation

- The results of this A/B test indicate that using the green button is likely to lead to a higher click-through rate.
- Consider implementing the green button as the primary call-to-action button on the website.

## Limitations

- The results are based on a specific duration and user base and may not be representative of long-term performance.
- Other factors not considered in this test (e.g., button placement, text, website content) could impact CTR.
- There is statistical significance, however it should be monitored going forward to ensure that we have not encountered an unlikely Type-1 error.

## Next Steps

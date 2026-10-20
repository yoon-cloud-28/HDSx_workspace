# Visual Audit Note

## Plot Question

What is the trend of mean BMI across the NHANES cycle?

## Issues Checked

| Issue | Category | Why it matters | Correction |
|---|---|---|---|
| y-axis starts at 24 instead of 0| Correctness | Exaggerates the BMI gap between groups, suggesting a larger difference than the data show | Start the y-axis at 0 (or show the full data range) and state the axis choice in the caption |
| NHANES cycle missing between 2001-2020 | Correctness | Exaggerates the change between 1999-2000 cycle and 2021-2023 as if it was a stiff straight climb | Include all cycles of the NHANES data |
| Doesn't indicate if BMI is weigthed or not | Interpretation | Misleads the interpreatation | Specify whether if the BMI was weighted or not |
| The title and axis titles uses causation leading words and misleading words| Interpretation | Suggests causation and misleads the interpretation | Change the title to "Mean BMI by income group across NHANES cycles in the prepared classroom dataset", get rid of the subtitle, change the y axis title to "Mean BMI", and change the "Income" to "Income Group" |

## Final Caption

"Unweighted descriptive mean BMI. Adults aged 20-80 with non-missing BMI, income group, and cycle from a classroom NHANES dataset; groups with n < 30 excluded. Not a population estimate."

This figure shows mean BMI by income group across NHANES cycle using the prepared NHANES Health Equity classroom dataset. The summary is descriptive and unweighted. Records with missing BMI, income group, and NHANES cycle were excluded. The plot supports comparison of patterns, not causal claims or population-level estimates.

## AI-Use Check

AI was used to revise the code based on the isses that were checked by me. I checked the code changes with what we learned during the class and textbook. AI was also used to revise the "Revision note" to make it sound more clear. 

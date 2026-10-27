# Table 1 Audit Note

## Cohort

US adults between the ages of 20-80 (inclusive) years old. 

## Missingness

Originally, no missingness check was done. In the audit, various variables were checked for missingness (age, BMI, income group)

## Planted Issues

| Issue | Category | Why it matters | Corrected approach |
|---|---|---|---|
| Analysis cohort doesn't include adults age of 20 and 80 | Correctness | The cohort is stated to be adults age 20-80 (inclusive) which is misleading if they are not included | Change the filter for the analysis cohort |
| Didn't check for missinginess in any variables | Reproducibility | Makes it difficult for others to check and understand the result when NAs just disappear from the result | Check missingness for key variables |
| Missing variables are included in the Table 1 analysis | Correctness | Not having them explicitly excluded may lead to errors | Filter the cohort dataframe to drop NAs in variables that have missingness |
| Using var(Age) and var(BMI)| Correctness | The code will not give the SD of Age and BMI which is what we want to report | Change the code to sd() |
| Interpreting that due to dropping all NAs, the result is correct and publication ready | Correctness | The interpretation is far fetched, validation regarding the NAs need to be done in order to determine the result's reliability and validity | Change the interpretation to that futher work needs to be done to determine the validity of the result |
| Table 1 is ordered from High Income -> Low Income -> Middle Income | Interpretation | The order of the output might confuse readers | Change the order of Table 1 |
| Interpreted the result by saying that "differences in BMI between income groups are statistically significant" | Correctness | We cannot determine statistical significance with just mean and SD | Change the interpretation to note which income group has higher mean and which has the lowest |

## AI-Use Check

AI wasn't used to find the planted issues. AI assisted with changing the order of the Incomegroup output order. AI was also used to make sure that the Table 1 csv file is saved to the correct folder. Lastly, AI was used to revise the interpretation. 

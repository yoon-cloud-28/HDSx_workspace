# Dashboard Adaptation Note

## Audience

Public-health analyst preparing a short briefing on descriptive BMI patterns in the classroom NHANES equity dataset.

## Dashboard Question

Among young adults age 18-25, how does mean BMI vary across NHANES cycles for one selected income group?
Among adults age 20-80, how does mean BMI vary across NHANES cycles for one selected income group?

## Control And Visualization

- Control or interaction: A single 'selected_income' value the analyst can change
- Visualization affected: A line plot of mean BMI by cycle for the selected income group
- What changes when the control changes: When the control change, the chosen income group changes resulting in the analysis result to change. 

## Before And After

| Original text | Revised text | Why the revision helps |
|---|---|---|
|NHANES cycle| Survey cycle (NHANES cycle) | It clarifies what the y axis is in the figure|
|There wasn't any sentence like this in the "control" section.|This dashboard uses adults age 20-80. To see a different income group, change the value and re-render.|It clarifies what the audience is looking at when they are looking at the dashboard and how to work the dashboard|
|# Dashboard starter|# NHANES Health Equity Classroom Dashboard

Descriptive, unweighted mean BMI by income group across NHANES cycles. For classroom learning; not for population inference.|Clarified the introduction to the dashboard with an explanation of the dataset, scope, and limitation. |

## Test Result

The dashboard was run and rendered without errors or warnings. 

## Limitation

This dataset is unweighted and descriptive.

## Privacy Check

The rendered dashboard shows only cycle-level aggregates (sample counts and rounded mean BMI), not individual records. These are unweighted, descriptive patterns in the classroom dataset—not population estimates or evidence that income causes BMI differences, which is explicitly states in the figure and in the limitation section.
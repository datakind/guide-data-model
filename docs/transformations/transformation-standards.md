# Documentation of Data Transformation Standards

*authored by Tara Chiatovich*

---

## Purpose

With support from the Gates Foundation, DataKind is building the GUIDE Data Model to enable data-driven decision making in higher education and offer holistic support to students (see Gates Foundation, n.d.). Trust in data is mission critical to the success of the GUIDE Data Model. This document lays out the major approaches to ensuring that data transformations result in data that accurately reflect the raw data. It describes the approaches with some examples of how DataKind could draw on each for this work before proposing a concrete plan for determining how much a raw and transformed numeric column should be allowed to differ from each other. This transparency is one important means DataKind plans to build trust among users in the data insights that the GUIDE Data Model will make possible.

The main aims of documenting data transformation standards are:

1. **Providing transparency**
  - Institutions using the GUIDE Data Model or interested in the public good data model will know about what DataKind has deemed an acceptable deviation (or allowable amount of change) following transformation of numeric columns.
  - DataKind's goal in providing this information is to allow institutions to determine whether use of the data model is right for them given DataKind's stated acceptable deviation.
2. **Giving examples of inappropriate transformations**
  - Users of the data model should know which transformations should not be performed because they would undermine the data's precision.
  - The goal is to limit the risk of error when raw data likely do not lend themselves to transformation.

What documentation data transformation standards will **not** achieve:

1. Eliminate sizable data discrepancies across data systems within an institution (e.g., a student having two different numbers of total credits earned recorded in two source systems).
2. Explain the reason for individual data discrepancies across data sources for a given institution (e.g., the reason for a student having two different numbers of total credits earned in two source systems).
3. Determine whether any individual institution's data are appropriate for transformation to conform to the data model given the variability in data availability, format, and quality across institutions.

---

## Executive Summary

**Approaches for Ensuring the Fidelity of Transformed Data.** DataKind will be incorporating tests of data quality in higher education into the Data Observation Toolkit, its data monitoring tool. In addition, DataKind documents what transformations of raw institutional data it performs as part of its work on the GUIDE Data Model, which makes clear the data elements and structure that power the model. Both of these steps provide assurance that transformed data accurately represent raw data. Although sophisticated statistical approaches exist that could assess whether raw and transformed data differ in notable ways, such analyses are not recommended as part of our data transformation standards because they would need to be highly tailored to each institution's data and to the element of the data being examined.

**Defining *Acceptable Deviation* for Numeric Columns.** Using simple methods and descriptive statistics, DataKind can set a conservative threshold for how much raw and transformed numeric columns may differ from each other. Via a statistical approach called power analysis, we determined the magnitude of difference in means between raw and transformed columns would approach statistical significance in 20% of samples using a sample size of 6,000 students. The logic is that this difference is unlikely to influence findings for a smaller mid-sized post-secondary institution in most cases (thus it *approaches* statistical significance for only 20% of samples). Using these specifications, the difference in means resulting from the transformation should not exceed the threshold of **0.045 standard deviations**. As an illustrative example, the transformation of rounding GPA to two decimal places results in a difference that is well below this threshold based on published standard deviations.

**Inappropriate Transformations and Potential Issues.** This document ends by giving examples of transformations that should not be performed, including mapping ambiguous values and eliminating precision. It also identifies issues that could affect data but are unrelated to the transformations.

---

## Approaches for Ensuring the Fidelity of Transformed Data

### Data Monitoring and Tests of Data Quality

Tools that monitor data can help increase transparency following data transformations and catch when transformations have unintended effects on data quality. DataKind developed the Data Observation Toolkit (DOT) for this purpose. Importantly, it leverages other widely used data monitoring tools, including [dbt](https://www.getdbt.com/) and [Great Expectations](https://greatexpectations.io/). The Data Observation Toolkit has focused on monitoring data quality in healthcare. DataKind is expanding it to run tests of data quality for higher education data.

With assistance from AI, DataKind is developing tests of data quality for incorporation into DOT that are specific to the GUIDE Data Model. These tests include:

- Ensuring that key identifiers do not have missing values
- Applying cross-column logic (e.g., the number of students enrolled in a course cannot exceed the enrollment cap for the course)
- Checking for proper chronology (e.g., end dates cannot precede start dates)

It is important to note that these can catch issues that were introduced by transformations that are part of the GUIDE Data Model as well as issues that already existed in the data supplied by colleges and universities. For more details on how the tests were produced and for a link to the spreadsheet with all tests listed, please see the report [GUIDE Data Model: AI-generated Data Quality Tests](https://docs.google.com/document/d/1pn2CgiKAU2QLExp8_AeOeuImBHComDV9eC2PscwcER8/edit?tab=t.0).

### Transparency for Data Transformations

#### Methods to Ensure Code That Performs the Transformations Is Correct

DataKind has built-in transparency for how we transform raw institutional data into data for the GUIDE Data Model. In preparation for the initial release of the GUIDE Data Model, we have identified the categories of source systems in higher education that will supply the data, including Student Information Systems (SIS), Customer Relationship Management systems (CRM), and Learning Management Systems (LMS). Additionally, we are mapping the data from source systems to the GUIDE Data Model with notes on what transformations are necessary to prepare the data for the GUIDE Data Model. These notes will be publicly available as part of the GUIDE Data Model. Giving institutions the ability to understand each transformation promotes trust in the transformed data.

### Analytic Approaches for Ensuring Data Fidelity

#### Simplest Analytic Approach: Standards Based on Descriptive Statistics

Descriptive statistics come from simple calculations and, as their name suggests, seek to describe the data. They include such metrics as counts, means, standard deviations, and percentages. The section titled Defining *Acceptable Deviation* for Numeric Columns gives details on one promising method that combines descriptive statistics and inferential statistics to create a criterion for transformations involving numeric columns.

#### More Complicated Analytic Approaches: Standards Based on Tests of Statistical Significance and Synthetic Data

In addition to creating data transformation standards based on descriptive statistics, DataKind can engage with more sophisticated analytics for these standards. One option is to have standards that run statistical tests to see whether the *distribution* of the raw and transformed data differ significantly. Criteria for transformations from these methods are not presented here because they would need to be highly tailored to each transformation. They would also need to reflect the data being transformed, either by use of actual institutions' data or realistic synthetic data. In other words, they would require considerable inputs but would not generalize well to data transformations overall. If they are used at all, they should be limited to risk-prone transformations that are crucial for the functioning of the GUIDE Data Model should any such transformations become part of the data pipeline as DataKind works towards the initial release of this product.

---

## Defining *Acceptable Deviation* for Numeric Columns

DataKind can use power analysis to determine a level of difference between raw and transformed numeric columns that is unlikely to alter the results of a statistical test. Researchers often use power analysis when designing a study to determine the target sample size given anticipated properties of the data and analysis (e.g., magnitude of the expected difference between treatment and control groups, desired level of statistical significance, the percentage of samples across repeated random sampling that yield a statistically significant effect; see Buckley, 2024). For this project, however, *the power analysis allows us to determine how large a difference between the raw and transformed data we can consider "safe" in the sense that it is unlikely to affect findings* (i.e., unlikely to result in statistically significant differences between the raw and transformed data). It does not require any synthetic data. Instead, it just requires the information about the data.

For this first pass, power analysis was used to determine what magnitude of difference would yield results that *approached* statistical significance (*p* < .10 compared to the research standard of *p* < .05 for statistical significance) in only 20% of repeated random samples of size 6,000. The choice of 6,000 for the sample size was to represent the lower end of a mid-sized post-secondary institution. Since 20% of repeated random samples would approach statistical significance, only 1 in 5 times would this effect come close to a statistically significant finding. With the power analysis set up this way, **a difference of 0.045 standard deviations would be our threshold**.

To put this guideline into context, Gershenfeld and colleagues (2015) reported first semester college GPA to have a standard deviation of 0.67 for students who went on to graduate and 0.99 for students who did not. Taking the more conservative standard deviation for GPA of 0.67, we see that 0.045 × 0.67 = 0.030. If our transformation is to take a GPA from a college that has four digits after the decimal point and rounding it to have two digits after the decimal point, the largest discrepancy from rounding would be 0.005 (e.g., from a GPA of 3.5050 rounding to 3.51). This is several orders of magnitude below the threshold of 0.030.

One nice feature of using the power analysis to determine the threshold is that with minimal coding, we can change any of the chosen settings above. For example, we could choose a larger sample size to represent a larger post-secondary institution, or set up the analysis to give statistically significant effects instead of those that approach statistical significance, or require that the effect reach statistical significance across 25% of repeated random samples.

> **Note:** The use of power analysis would require calculating the standard deviation and the difference in standard deviation units between the raw and transformed numeric column each time data are ingested. An additional consideration is that this method is only relevant for numeric columns and date columns. It therefore is not relevant for enumerated (categorical) columns or other columns with text data.

---

## A Note on Data Types and Inappropriate Transformations

This document addresses steps to help ensure accuracy of transformed data, but some data transformations should not happen at all because they would cause distortions. Key types of transformations to avoid are:

- **Transforming a lower-precision data element to a higher-precision data element.**
  - *Example 1:* Transforming the academic term and year a course was offered to the date a course started (e.g., "Fall 2025" → "09/01/2025").
  - *Example 2:* Transforming overall grade on a test to the number of points earned for each question on the test.
  - *Justification:* Performing this type of transformation would result in data that suggest a level of accuracy and specificity that we cannot get from the data and therefore would be arbitrarily decided on.
- **Mapping unknown or ambiguous values for an enumerated column onto specific enumerated values.**
  - *Example 1:* Mapping numeric values for students' race onto labeled values for race when there is no data dictionary (e.g., mapping *1 → Black* and *2 → Asian* when there is no record of what the numbers signify in the original data).
  - *Example 2:* Mapping of values that are not in the data dictionary and suggest a data entry error (e.g., where the values for student gender are documented as *M = male*, *F = female*, and *X = gender non-binary*, mapping the value *N* to *gender non-binary* when *N* is not included in documentation for student gender).
  - *Justification:* Even when there are strong indications for which ambiguous values should be mapped to accepted values, across institutions such judgement calls will result in inaccurate data.
- **Eliminating precision in a way that goes beyond reasonable rounding without justification.**
  - *Example 1:* When the data gives a date, performing a transformation that only keeps the month and year (e.g., 03/14/2026 → March 2025).
  - *Example 2:* Rounding course numeric grades to the nearest whole number or eliminating the "+/−" after a letter grade (e.g., 3.30 → 3.00, A− → A).
  - *Justification:* We do not want to lose precision without a good reason, especially given the possibility for compounding the loss of precision for any aggregations performed on the data.
    - Although it is acceptable to retain the original columns with greater precision and add new columns with less precision, the GUIDE Data Model should not lose precision outright without a strong justification.
    - Examples of strong justifications include:
      - There would be significant storage needs for data deemed not useful for the GUIDE Data Model (e.g., individual test questions that make up instructor-written exams for a course).
      - Most institutions have data at the lower level of precision with a small percentage having data at the higher level of precision (e.g., date and time of the last data element update when most institutions only store the date of the last update).
      - Prior analyses reveal that the higher level of precision does not contribute to greater accuracy in predictive analytics or a greater proportion of the variance explained in inferential statistics.

---

## Potential Issues Unrelated to Data Transformation

A number of issues could arise outside of the data transformation with consequences for the data used in the GUIDE Data Model. They include:

- Problems that are introduced in the data during ingestion (e.g., dropped rows, data corruption).
- Data that have issues prior to ingestion (e.g., enumerated columns with data entry errors, columns that should be numeric but that have cells with alphabetic characters).
- Variability across institutions (e.g., 2 vs. 4 decimal places for raw numeric columns depending on the institution, institutions with dates vs. datetimes for some columns).
- Specifications in the data model that do not align with the ingested data (e.g., a column specified as a date in the data model only gives the month in the institution's raw data).

These issues could lead to results suggesting a problem with the data transformation even when there is none. Conversely, they could compromise the quality of the data even when all checks of data transformation standards pass. They therefore are important issues to keep in mind.

---

## Conclusion

DataKind relies on data to power everything we produce. We recognize that the GUIDE Data Model can only provide value to institutions if its users trust the data providing the insights. The steps outlined above help ensure that DataKind maintains the accuracy and precision of the data that will flow through the pipelines to power the GUIDE Data Model.

---

## Acknowledgements

DataKind would like to thank Unicon, Inc., who worked to develop and refine the first versions of this data model. Unicon's mapping of the Postsecondary Data Partnership and LMS data schemas to the model contributes considerable value to DataKind's building of a data pipeline that will power the GUIDE Data Model.

---

## References

Buckley, J. (2024). Conducting Power Analyses to Determine Sample Sizes in Quantitative Research: A Primer for Technology Education Researchers Using Common Statistical Tests. *Journal of Technology Education*, *35*(2), 81–109.

Gates Foundation (n.d.) Committed Grants: DataKind Inc. [https://www.gatesfoundation.org/about/committed-grants/2025/04/inv-079563](https://www.gatesfoundation.org/about/committed-grants/2025/04/inv-079563)

Gershenfeld, S., Ward Hood, D., & Zhan, M. (2015). The Role of First-Semester GPA in Predicting Graduation Rates of Underrepresented Students. *Journal of College Student Retention: Research, Theory & Practice*, *17*(4), 469–488. [https://doi.org/10.1177/1521025115579251](https://doi.org/10.1177/1521025115579251)
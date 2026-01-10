"""
CAPSTONE EXERCISE 7: Export and Report

Final step: Export your cleaned data and analysis results.
1. Export cleaned data to CSV
2. Create a summary report DataFrame
3. Export to different formats

This demonstrates the end of a data science workflow where
you deliver results to stakeholders.
"""
import pandas as pd
import numpy as np
from datetime import datetime
import os

# ---- FINAL DATASET ----
np.random.seed(42)
n = 100
TODAY = datetime(2024, 6, 1)

tenure = np.random.uniform(0.5, 9, n)
rating = np.clip(3 + np.random.normal(0, 1, n), 1, 5)
dept = np.random.choice(["Engineering", "Sales", "Marketing", "HR"], n)
salary = (50000 + tenure * 3000 + rating * 2000 +
          (dept == "Engineering") * 10000 + np.random.normal(0, 5000, n))

df = pd.DataFrame({
    "employee_id": range(1001, 1001 + n),
    "department": dept,
    "salary": salary.round(2),
    "tenure_years": tenure.round(2),
    "rating": rating.round(1),
    "analysis_date": TODAY.strftime("%Y-%m-%d")
})

# Directory for exports
EXPORT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- YOUR CODE HERE ----
# Task 1: Create a summary report DataFrame
# One row per department with: count, mean_salary, median_salary, mean_rating
summary_report = None

# Task 2: Create an overall statistics dictionary
# Keys: total_employees, mean_salary, median_salary, salary_std, date_generated
overall_stats = {
    "total_employees": None,
    "mean_salary": None,
    "median_salary": None,
    "salary_std": None,
    "date_generated": TODAY.strftime("%Y-%m-%d")
}

# Task 3: Export cleaned data to CSV
# Save to: EXPORT_DIR + "/cleaned_employees.csv"
# Don't include the index
csv_path = os.path.join(EXPORT_DIR, "cleaned_employees.csv")
# df.to_csv(csv_path, index=False)

# Task 4: Export summary report to CSV
report_path = os.path.join(EXPORT_DIR, "department_summary.csv")
# summary_report.to_csv(report_path)

# Task 5: Create a text report string
# Format the key findings as a readable report
report_text = None  # Multi-line string with findings
# Example:
# """
# HR Analytics Report
# Generated: 2024-06-01
#
# Total Employees: 100
# Average Salary: $XX,XXX
# ...
# """
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("=== Export and Report ===\n")

    print("Task 1: Summary report DataFrame")
    check(summary_report is not None, expected=True)
    if summary_report is not None:
        check("mean_salary" in str(summary_report.columns).lower() or "salary" in str(summary_report.columns).lower(),
              expected=True,
              hint='df.groupby("department").agg(...)')
        print(summary_report)

    print("\nTask 2: Overall statistics")
    check(overall_stats["total_employees"] == 100, expected=True,
          hint="len(df)")
    check(overall_stats["mean_salary"] is not None, expected=True,
          hint="df['salary'].mean()")
    print(overall_stats)

    print("\nTask 3: CSV export")
    if os.path.exists(csv_path):
        print(f"Created: {csv_path}")
        # Verify it can be read back
        df_read = pd.read_csv(csv_path)
        check(len(df_read) == 100, expected=True)
    else:
        print(f"File not created yet: {csv_path}")
        print("Hint: df.to_csv(csv_path, index=False)")

    print("\nTask 4: Summary report export")
    if os.path.exists(report_path):
        print(f"Created: {report_path}")
    else:
        print(f"File not created yet: {report_path}")

    print("\nTask 5: Text report")
    if report_text:
        print("Report preview:")
        print(report_text[:500] if len(report_text) > 500 else report_text)
    else:
        print("Report not created yet")
        print('Hint: Use f-strings to create a formatted report')

    print("\n" + "="*50)
    print("CONGRATULATIONS!")
    print("You've completed the Python for R Users tutorial!")
    print("="*50)

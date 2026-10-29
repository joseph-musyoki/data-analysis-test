import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create the raw dataset
raw_data = {
    'Student_ID': [1001, 1002, 1003, 1004, 1005, 1001, 1006, 1007, 1008, 1009],
    'County': ['Nakuru', 'Narok', 'Nakuru', 'Narok', 'Kakamega',
               'Nakuru', 'Nairobi', None, 'Narok', 'Nakuru'],
    'Study_Hours_Per_Week': [15, 8, 20, None, 12, 15, 30, 10, 25, 18],
    'Attendance_Percent': [85, 60, 92, 55, 78, 85, 95, 65, 88, None],
    'Fee_Balance_Ksh': [0, 15000, 0, 25000, 5000, 0, 0, 18000, 2000, 12000],
    'Previous_Grade': [72, 48, 85, 45, 65, 72, 90, 50, 82, 58],
    'Student_Type': ['Regular', 'Regular', 'Scholarship', 'Regular',
                     'Scholarship', 'Regular', 'Regular', 'Scholarship',
                     'Regular', 'Regular'],
    'Academic_Risk': [0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(raw_data)

# STEP 4: EXPLORATORY DATA ANALYSIS (EDA)

# Set the visual style
sns.set_theme(style="whitegrid")

# Graph 1: Academic risk by county
plt.figure(figsize=(9, 5))
sns.countplot(data=df, x='County', hue='Academic_Risk')
plt.title('Academic Risk by County')
plt.xlabel('County')
plt.ylabel('Number of Students')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


# Graph 2: Study hours compared with academic risk
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Academic_Risk', y='Study_Hours_Per_Week')
plt.title('Study Hours per Week vs Academic Risk')
plt.xlabel('Academic Risk (0 = No Risk, 1 = At Risk)')
plt.ylabel('Study Hours per Week')
plt.tight_layout()
plt.show()


# Graph 3: Attendance compared with academic risk
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Academic_Risk', y='Attendance_Percent')
plt.title('Attendance Percentage vs Academic Risk')
plt.xlabel('Academic Risk (0 = No Risk, 1 = At Risk)')
plt.ylabel('Attendance (%)')
plt.tight_layout()
plt.show()


# Graph 4: Fee balance compared with academic risk
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Academic_Risk', y='Fee_Balance_Ksh')
plt.title('Fee Balance vs Academic Risk')
plt.xlabel('Academic Risk (0 = No Risk, 1 = At Risk)')
plt.ylabel('Fee Balance (KSh)')
plt.tight_layout()
plt.show()


# Graph 5: Previous grades compared with academic risk
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Academic_Risk', y='Previous_Grade')
plt.title('Previous Grade vs Academic Risk')
plt.xlabel('Academic Risk (0 = No Risk, 1 = At Risk)')
plt.ylabel('Previous Grade')
plt.tight_layout()
plt.show()
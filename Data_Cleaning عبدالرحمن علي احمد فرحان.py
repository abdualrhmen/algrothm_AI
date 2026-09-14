# ========================================================
# مقرر: ذكاء اصطناعي (عملي)
# التكليف: تنظيف ومعالجة البيانات (Data Preprocessing / Cleaning)
# إعداد الطالب: عبدالرحمن علي احمد فرحان
# ========================================================

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.preprocessing import LabelEncoder

input_file = "regression_employee_data-1 (1).csv"
print(f"جاري قراءة الملف: {input_file}...")
data = pd.read_csv(input_file)

print("\n--- معلومات البيانات الأولية ---")
data.info()

print("\n--- عدد القيم المفقودة في كل عمود ---")
print(data.isnull().sum())

# إزالة التكرارات
data.drop_duplicates(inplace=True)

# معالجة القيم المفقودة للأعمدة النصية باستخدام المنوال
for col in ['Qualification', 'Degree', 'EducationalInstitute']:
    mode_val = data[col].mode()[0]
    data[col] = data[col].fillna(mode_val)

# معالجة العمود الرقمي
study_mode = data['YearsOfStudy'].mode()[0]
data['YearsOfStudy'] = data['YearsOfStudy'].fillna(study_mode)

# حذف المعرف الزائد
data.drop('Emp #', axis=1, inplace=True)

# تحويل النصوص إلى أرقام
encoder = LabelEncoder()
data['Gender'] = encoder.fit_transform(data['Gender'])
data['Empl_Band'] = encoder.fit_transform(data['Empl_Band'])

categorical_cols = ['Designation', 'Qualification', 'Degree', 'EducationalInstitute']
data = pd.get_dummies(data, columns=categorical_cols, dtype=int)

assert data.isnull().sum().sum() == 0, "لا تزال هناك قيم مفقودة!"
print("\n✅ تم تنظيف جميع البيانات بنجاح، عدد القيم المفقودة الآن: 0")

output_file = "regression_employee_data_cleaned.csv"
data.to_csv(output_file, index=False)
print(f"✅ تم حفظ الملف المنظف باسم: {output_file}")
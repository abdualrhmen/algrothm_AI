# ========================================================
# مقرر: ذكاء اصطناعي (عملي)
# التكليف الرابع: تدريب نموذج على بيانات وتحقيق دقة أعلى من 90%
# إعداد الطالب: عبدالرحمن علي احمد فرحان
# ========================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
print("جاري تحميل البيانات من GitHub...")
df = pd.read_csv(url)

print("\nأول 5 صفوف من البيانات:")
print(df.head())

X = df.drop('species', axis=1)
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred) * 100
error_rate = 100 - acc

print("\n" + "="*45)
print(f"🎯 دقة النموذج المحققة (Accuracy): {acc:.2f}%")
print(f"📉 نسبة الخطأ (Error Rate): {error_rate:.2f}%")
print("="*45)

print("\n--- تقرير التصنيف (Classification Report) ---")
print(classification_report(y_test, y_pred))

print("--- مصفوفة الخطأ (Confusion Matrix) ---")
print(confusion_matrix(y_test, y_pred))
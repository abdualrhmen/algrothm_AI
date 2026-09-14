# ========================================================
# مقرر: ذكاء اصطناعي (عملي)
# التكليف الخامس: تطبيق 4 خوارزميات في تعلم الآلة
# (Classification, Regression, Clustering, Association)
# إعداد الطالب: عبدالرحمن علي احمد فرحان
# ========================================================

import numpy as np
import pandas as pd

# 1. Classification (شجرة القرار)
print("="*50)
print("1. خوارزمية التصنيف: Decision Tree")
print("="*50)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_c, y_c = iris.data, iris.target
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_c, y_c, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_c, y_train_c)
y_pred_c = clf.predict(X_test_c)
print(f"دقة تصنيف شجرة القرار: {accuracy_score(y_test_c, y_pred_c) * 100:.2f}%\n")

# 2. Regression (الانحدار الخطي)
print("="*50)
print("2. خوارزمية الانحدار: Linear Regression")
print("="*50)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

X_exp = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y_sal = np.array([30000, 35000, 42000, 48000, 57000, 62000, 71000, 79000])

reg = LinearRegression()
reg.fit(X_exp, y_sal)
y_pred_sal = reg.predict(X_exp)

print(f"معامل التحديد R²: {r2_score(y_sal, y_pred_sal):.4f}")
print(f"متوسط الخطأ التربيعي MSE: {mean_squared_error(y_sal, y_pred_sal):.2f}")
print(f"توقع الراتب لخبرة 10 سنوات: {reg.predict([[10]])[0]:.2f}\n")

# 3. Clustering (تجميع الوسائط K-Means)
print("="*50)
print("3. خوارزمية التجميع: K-Means Clustering")
print("="*50)
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_c[:, :2])
print("مراكز التجميع (Cluster Centers):")
print(kmeans.cluster_centers_)
print(f"تم تصنيف العينات إلى المجموعات بنجاح.\n")

# 4. Association Rules (خوارزمية Apriori)
print("="*50)
print("4. خوارزمية قواعد الارتباط: Apriori")
print("="*50)
try:
    from mlxtend.preprocessing import TransactionEncoder
    from mlxtend.frequent_patterns import apriori, association_rules

    dataset = [
        ['Milk', 'Bread', 'Butter'],
        ['Bread', 'Butter'],
        ['Milk', 'Bread'],
        ['Milk', 'Diapers', 'Beer'],
        ['Bread', 'Milk', 'Butter']
    ]

    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df_trans = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = apriori(df_trans, min_support=0.4, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
    print("قواعد الارتباط المستخرجة بنجاح:")
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())
except ImportError:
    print("لتشغيل مكتبة الارتباط يرجى تثبيتها عبر: pip install mlxtend")
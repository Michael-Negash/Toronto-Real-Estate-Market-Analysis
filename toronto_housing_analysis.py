import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

# ----------------------------------------------------------------
# Load data  🚨 Update path to your dataset
# ----------------------------------------------------------------
df = pd.read_csv(r'your_data.csv')

# ================================================================
# 1. Bond vs Toronto Stock Exchange — Scatter + Best Fit Line
# ================================================================
slope, intercept, r, p, se = stats.linregress(df['TSX'], df['BONDS'])
df['BestFitTSX'] = intercept + slope * df['TSX']

plt.figure(figsize=(8, 5))
plt.scatter(df['TSX'], df['BONDS'], label='Data', alpha=0.7)
plt.plot(df['TSX'].sort_values(),
         df.loc[df['TSX'].sort_values().index, 'BestFitTSX'],
         color='red', label='Best Fit')
plt.title('Bond vs Toronto Stock Exchange', fontsize=10)
plt.xlabel('Toronto Stock Exchange')
plt.ylabel('Bonds')
plt.legend()
plt.tight_layout()
plt.show()

# Regression: BONDS ~ TSX
X = sm.add_constant(df['TSX'])
model = sm.OLS(df['BONDS'], X).fit()
print("=== BONDS ~ TSX ===")
print(model.summary())

# ================================================================
# 2. Toronto Population vs Average Sale Price — Scatter
# ================================================================
plt.figure(figsize=(8, 5))
plt.scatter(df['POP'], df['AVGPT'], alpha=0.7)
plt.title('Toronto Population vs Average Sale Price', fontsize=10)
plt.xlabel('Toronto Population (000)')
plt.ylabel('Average Sale Price (000)')
plt.tight_layout()
plt.show()

# Regression: AVGPT ~ POP
X = sm.add_constant(df['POP'])
model = sm.OLS(df['AVGPT'], X).fit()
print("\n=== AVGPT ~ POP ===")
print(model.summary())

# ================================================================
# 3. Toronto Population vs Price Index — Scatter
# ================================================================
plt.figure(figsize=(8, 5))
plt.scatter(df['POP'], df['THPI'], alpha=0.7)
plt.title('Toronto Population vs Price Index', fontsize=10)
plt.xlabel('Toronto Population (000)')
plt.ylabel('Toronto House Price Index')
plt.tight_layout()
plt.show()

# ================================================================
# 4. Toronto Population vs Price Index — Two Storey Houses
# ================================================================
plt.figure(figsize=(8, 5))
plt.scatter(df['POP'], df['THPIH'], alpha=0.7)
plt.title('Toronto Population vs Price Index Two Storey Houses', fontsize=10)
plt.xlabel('Toronto Population (000)')
plt.ylabel('Toronto House Price Index Two Storey Houses')
plt.tight_layout()
plt.show()

# ================================================================
# 5. Toronto Population vs Price Index — Apartments/Condos
# ================================================================
plt.figure(figsize=(8, 5))
plt.scatter(df['POP'], df['THPIA'], alpha=0.7)
plt.title('Toronto Population vs Price Index Apartments/Condos', fontsize=10)
plt.xlabel('Toronto Population (000)')
plt.ylabel('Toronto House Price Index Apartments/Condos')
plt.tight_layout()
plt.show()

# Regression: POP ~ THPI + THPIH + THPIA
X = sm.add_constant(df[['THPI', 'THPIH', 'THPIA']])
model = sm.OLS(df['POP'], X).fit()
print("\n=== POP ~ THPI + THPIH + THPIA ===")
print(model.summary())

# ================================================================
# 6. Correlation Matrix — Price Indices + Population
# ================================================================
print("\n=== Correlation: THPI, THPIH, THPIA, POP ===")
print(df[['THPI', 'THPIH', 'THPIA', 'POP']].corr())

# ================================================================
# 7. Regression: AVGPT ~ LFC + PTM + UNEMP + EI
# ================================================================
X = sm.add_constant(df[['LFC', 'PTM', 'UNEMP', 'EI']])
model = sm.OLS(df['AVGPT'], X).fit()
print("\n=== AVGPT ~ LFC + PTM + UNEMP + EI ===")
print(model.summary())

# Correlation: Part-time employment, Unemployment, Employment Insurance
print("\n=== Correlation: PTM, UNEMP, EI ===")
print(df[['PTM', 'UNEMP', 'EI']].corr())

# ================================================================
# 8. Regression: CPIT ~ RETAIL + CNEWHL + RENT + OWN
# ================================================================
X = sm.add_constant(df[['RETAIL', 'CNEWHL', 'RENT', 'OWN']])
model = sm.OLS(df['CPIT'], X).fit()
print("\n=== CPIT ~ RETAIL + CNEWHL + RENT + OWN ===")
print(model.summary())

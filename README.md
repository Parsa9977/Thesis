# Photovoltaic Energy Production Forecasting - Machine Learning Thesis

## 📋 Project Overview

This comprehensive thesis project develops advanced machine learning models for photovoltaic (PV) energy production forecasting using 13+ years of temporal data (2012-2025) with 454,970 observations across multiple solar installations.

### Key Objectives
- **Data Integration**: Combine PV production data with Italian regulatory context and weather variables
- **Feature Engineering**: Create 31 ML-ready features from raw data
- **Model Development**: Build and optimize predictive models across 4+ datasets
- **Performance Analysis**: Comprehensive evaluation with hyperparameter tuning and cross-validation

---

## 📁 Project Structure

```
Final Thesis/
├── Phase1/                          # Main analysis phase
│   ├── 📊 Raw Data
│   │   ├── 2023_Autoproduzione PV+FEV _estrattoDET.csv
│   │   ├── dataset1_cleaned.csv through dataset6_cleaned.csv
│   │   └── enriched_pv_data_with_FasciaAEEG.csv
│   │
│   ├── 🔄 Preprocessing Outputs
│   │   ├── filtered_pv_data_2014_onwards.csv
│   │   ├── weather_merged_*.csv (5 files)
│   │   ├── final_preprocessed_dataset*.csv (4 files)
│   │   └── final_preprocessed_merged_i3p.csv
│   │
│   ├── 📈 ML Results & Analysis
│   │   ├── enhanced_ml_results_summary.csv
│   │   ├── capacity.ipynb
│   │   └── missing_value_analysis.ipynb
│   │
│   ├── 🐍 Processing Notebooks
│   │   ├── Phase1.ipynb              # Data enrichment & FasciaAEEG integration
│   │   ├── phase2.ipynb              # Data preprocessing & dataset creation
│   │   ├── phase3_1.ipynb            # Weather data integration
│   │   ├── phase4.ipynb              # ML model development
│   │   ├── phase4_1.ipynb            # Advanced ML with feature importance
│   │   ├── phase5.ipynb              # Feature engineering & hyperparameter tuning
│   │   └── Figure_3_1_FasciaAEEG_Distribution.py
│   │
│   └── 📋 Analysis Files
│       └── Missing value analysis visualizations
│
└── Thesis/                          # Secondary analysis repository
    ├── Dataset/
    │   ├── first.ipynb              # Initial data loading
    │   └── second.ipynb             # 2021-2024 PV data download
    ├── second.ipynb                 # Data preparation
    ├── third.ipynb                  # Data merging
    └── Additional analysis files
```

---

## 🔍 Dataset Overview

### **Dataset 1** - EC Systems Combined
- **Rows**: 248,249 observations
- **Target Variables**: `tot_pv_ec`, `tot_pv_ec_inv3`, `total_pv_production`
- **Features**: 15 engineered features
- **Best Model**: Random Forest (R² = 0.9644)

### **Dataset 2** - Multiple Installations
- **Rows**: 197,770 observations
- **Targets**: 7 production variables (Castelfidardo, I3P, EC inverters, Aule)
- **Features**: 15 engineered features
- **Completeness**: 92.8%

### **Dataset 3** - Aule Installations Group
- **Rows**: 83,661 observations
- **Targets**: 4 production variables (Aule P, P_I1, P_I2 + total)
- **Features**: 14 engineered features
- **Completeness**: 99.52%

### **Dataset 4** - Cittadella System
- **Rows**: 268,682 observations
- **Target**: `tot_pv_cit`
- **Features**: 15 engineered features
- **Completeness**: 100% (Perfect data quality)

### **Merged I3P Dataset** - Directional System
- **Rows**: 301,958 observations
- **Targets**: East, West, Combined production
- **Features**: 14 engineered features
- **Completeness**: 100% (Perfect data quality)

---

## 🛠️ Methodology & Processing Phases

### **Phase 1: Data Enrichment**
📂 File: [Phase1.ipynb](Phase1/Phase1.ipynb)

Creates the foundational enriched dataset with:
- Italian calendar features (año, mese, giorno, settimana, etc.)
- Holiday classification (festivi pubblici, weekend)
- **FasciaAEEG** energy tariff bands (F1, F2, F3) - Italian electricity market time zones
- Output: `enriched_pv_data_with_FasciaAEEG.csv` (62.48 MB, 31 columns)

### **Phase 2: Data Preprocessing**
📂 File: [phase2.ipynb](Phase1/phase2.ipynb)

Comprehensive preprocessing pipeline:
- Missing value handling (systematic analysis)
- Outlier detection and treatment
- Feature scaling and normalization
- Dataset stratification:
  - **Individual Models** (≥60% data): 3 systems
  - **Combined Group 1** (40-59% data): 2 systems
  - **Combined Groups 2&3** (<39% data): 6 systems

### **Phase 3: Weather Integration**
📂 File: [phase3_1.ipynb](Phase1/phase3_1.ipynb)

Integrates Open-Meteo API weather data:
- Hourly temperature, wind speed, cloud cover
- Daily max/min temperature, daylight duration
- Precipitation data
- Interpolated to 15-minute intervals
- Creates 5 weather-merged datasets

### **Phase 4: Machine Learning Models**
📂 Files: [phase4.ipynb](Phase1/phase4.ipynb) & [phase4_1.ipynb](Phase1/phase4_1.ipynb)

Baseline ML model development:
- **Linear Regression** (baseline)
- **Random Forest** (default parameters)
- **XGBoost** (gradient boosting)
- **SVR** (support vector regression)
- Metrics: R², RMSE, MAE

### **Phase 5: Advanced ML & Optimization**
📂 File: [phase5.ipynb](Phase1/phase5.ipynb)

Advanced techniques with optimization:
- **Feature Importance Analysis** (Random Forest + XGBoost)
- **Correlation-based Feature Selection** (threshold: 0.7)
- **Hyperparameter Tuning** (GridSearchCV, RandomizedSearchCV)
- **Cross-Validation** for robust evaluation
- **XGBoost Tuning**: Best performing models
- Results captured in [enhanced_ml_results_summary.csv](Phase1/enhanced_ml_results_summary.csv)

---

## 📊 Best Model Performance

**XGBoost (Tuned) Results Across Datasets:**

| Dataset | Target | R² Score | RMSE | MAE |
|---------|--------|----------|------|-----|
| 1 | total_pv_production | 0.9544 | 0.0044 | 0.0013 |
| 2 | total_pv_production | 0.9584 | 2.8313 | 1.4682 |
| 3 | total_pv_production | 0.9174 | 5.3989 | 3.2150 |
| 4 | tot_pv_cit | 0.9446 | 23.7805 | 12.0293 |

**Summary**:
- Average R² improvement from baseline: -0.59% (stable performance)
- Consistent high R² across all datasets (0.91-0.96)
- Hyperparameter tuning validates model robustness

---

## 🔬 Key Analyses

### **Missing Value Analysis**
📂 File: [missing_value_analysis.ipynb](Phase1/missing_value_analysis.ipynb)

Comprehensive data quality assessment:
- **Dataset 1**: 0.00% missing (248,249 cells analyzed)
- **Dataset 2**: 7.22% missing (production variables)
- **Dataset 3**: 0.48% missing
- **Dataset 4**: 0.00% missing (perfect quality)
- **Merged I3P**: 0.00% missing (perfect quality)

Weather variables: <0.001% missing across all datasets

### **Capacity & Efficiency Analysis**
📂 File: [capacity.ipynb](Phase1/capacity.ipynb)

PV system performance evaluation:
- Efficiency distributions by system
- Statistical analysis (mean, std, max efficiency)
- Normal distribution fitting
- Box plot comparisons

### **FasciaAEEG Distribution**
📂 File: [Figure_3_1_FasciaAEEG_Distribution.py](Phase1/Figure_3_1_FasciaAEEG_Distribution.py)

Italian energy market classification analysis:
- F1 (peak hours): 11,000 intervals
- F2 (intermediate): 8,328 intervals
- F3 (off-peak): 15,712 intervals
- Thesis-ready visualizations (PNG + PDF)

---

## 📈 Features Engineered

### Temporal Features
- `anno` (year), `mese` (month), `giorno` (day)
- `ora` (hour), `minuti` (minutes)
- `settimana` (week number), `giorno_anno` (day of year)

### Calendar Features
- `giorno_settimana` (day of week): 0-6
- `mese_nome`, `giorno_nome`: Text representations
- `FasciaAEEG`: Italian tariff bands (F1, F2, F3)

### Holiday Features
- `festivo_pubblico`: Public holidays (Italian calendar)
- `weekend`: Weekend indicator
- Italian regulatory compliance

### Derived Features
- Interaction terms
- Lagged variables
- Rolling averages
- Seasonal decomposition

**Final Feature Count**: 31 total (15+ engineered from 16 original)

---

## 🎯 Quick Start Guide

### Prerequisites
```bash
python 3.10+
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
requests  # For API calls
scipy
```

### Installation
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn requests scipy
```

### Running the Pipeline

1. **Start with Phase 1** - Data enrichment:
   ```bash
   jupyter notebook Phase1/Phase1.ipynb
   ```

2. **Continue to Phase 2** - Preprocessing:
   ```bash
   jupyter notebook Phase1/phase2.ipynb
   ```

3. **Run Phase 3** - Weather integration:
   ```bash
   jupyter notebook Phase1/phase3_1.ipynb
   ```

4. **Execute Phase 4/5** - ML models:
   ```bash
   jupyter notebook Phase1/phase4_1.ipynb
   jupyter notebook Phase1/phase5.ipynb
   ```

### Key Output Files
- ✅ `enriched_pv_data_with_FasciaAEEG.csv` - Base enriched dataset
- ✅ `weather_merged_*.csv` - Weather-integrated data
- ✅ `final_preprocessed_dataset*.csv` - ML-ready datasets
- ✅ `enhanced_ml_results_summary.csv` - Model performance summary

---

## 📊 Data Quality Metrics

| Metric | Value |
|--------|-------|
| **Total Observations** | 454,970+ |
| **Temporal Resolution** | 15 minutes |
| **Time Period** | 2012-2025 (13+ years) |
| **Final Features** | 31 engineered |
| **Weather Variables** | 11 parameters |
| **Completeness** | 87-100% |
| **Average Missing %** | <1% (weather perfect) |

---

## 🎓 Thesis Contributions

### Chapter Integration
- **Phase 1**: Data collection & preprocessing methodology
- **Phase 2**: Feature engineering and time-series construction
- **Phase 3**: Environmental factor integration (weather + regulatory)
- **Phase 4-5**: Machine learning model development & optimization

### Research Outputs
- ✅ Comprehensive PV production forecasting models
- ✅ Market-aware energy prediction (FasciaAEEG integration)
- ✅ Hyperparameter optimization strategies
- ✅ Cross-dataset validation approach
- ✅ Missing data handling documentation

---

## 📝 Code Quality & Documentation

### Notebook Standards
- Clear section headers with emoji indicators
- Step-by-step processing pipeline
- Output verification and validation
- Comprehensive error handling
- Statistical summary statistics

### File Naming Convention
- `phase*.ipynb`: Processing phases
- `dataset*_cleaned.csv`: Cleaned raw data
- `weather_merged_*.csv`: Weather-integrated datasets
- `final_preprocessed_*.csv`: ML-ready datasets
- `*_results_summary.csv`: ML model results

---

## 🔗 Data Sources

### Primary Data
- **Source**: Photovoltaic production monitoring systems (2012-2025)
- **Frequency**: 15-minute intervals
- **Variables**: 15 production metrics across multiple installations

### External Data
- **Weather API**: [Open-Meteo](https://open-meteo.com/) - Free historical weather data
- **Regulatory Data**: Italian energy market (FasciaAEEG classification)
- **Calendar Data**: Italian public holidays and regulatory calendar

---

## 📄 Related Files

### Analysis & Visualizations
- [Enhanced ML Results Summary](Phase1/enhanced_ml_results_summary.csv)
- [Missing Value Analysis](Phase1/missing_value_analysis.ipynb)
- [Capacity Analysis](Phase1/capacity.ipynb)
- [FasciaAEEG Distribution](Phase1/Figure_3_1_FasciaAEEG_Distribution.py)

### Secondary Datasets
- [Thesis Dataset Repository](Thesis/Dataset/first.ipynb)
- [2021-2024 PV Data](Thesis/second.ipynb)
- [Data Merging Documentation](Thesis/third.ipynb)

---

## 🤝 Contributing & Future Work

### Potential Extensions
1. **Deep Learning Models**: LSTM/GRU for temporal sequences
2. **Ensemble Methods**: Stacking and voting approaches
3. **Real-time Forecasting**: Online learning strategies
4. **Geographic Expansion**: Multi-location cross-validation
5. **Regulatory Compliance**: Market-aware optimization

### Known Limitations
- Dataset imbalance in some production variables
- Weather data interpolation at 15-minute resolution
- Limited external variables (no grid price data)
- Geographic limitation to single region (Italy)

---

## 📞 Contact & Support

For questions about this thesis project:
- 📧 Email: [Your contact info]
- 📚 Thesis Title: Machine Learning for Photovoltaic Energy Production Forecasting
- 🎓 Department: [Your institution]
- 📆 Academic Year: 2024-2025

---

## 📜 License & Attribution

This work is part of a Master's Thesis in [Your Program].

**Citation Format**:
```
Author, Year. "Machine Learning for Photovoltaic Energy Production Forecasting."
Master's Thesis, [Institution Name].
```

---

## ✨ Acknowledgments

- **Open-Meteo**: Free weather data API
- **Scikit-learn**: ML framework
- **XGBoost**: Gradient boosting library
- **Italian Energy Authority (AEEG)**: Regulatory context

---

**Last Updated**: January 2025
**Status**: 🟢 Active Development
**Python Version**: 3.10+

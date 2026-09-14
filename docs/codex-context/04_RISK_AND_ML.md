# Risk Engine and ML Specification

## Goal
Estimate localized flash-flood risk rather than equating rainfall with flooding.

## Candidate features
- rainfall 1h/3h/6h/12h/24h/72h/7d
- rainfall anomaly
- soil moisture/proxy
- elevation
- slope
- flow accumulation
- drainage density
- distance to stream
- land cover where available
- historical flood frequency where legitimate data exists
- river level if available
- satellite flood evidence if available
- acoustic score if available
- pressure delta as auxiliary only

## MVP model
Use a transparent configurable weighted scoring model first. This is preferable to an untrained XGBoost model. Normalize features, calculate weighted risk, and expose contributing factors.

Optional P2 model:
- XGBoost classifier
- scikit-learn preprocessing
- SHAP explainability

Only claim model performance when a legitimate dataset, held-out evaluation and reproducible training pipeline exist.

## Outputs
- probability/score in [0,1]
- LOW/MODERATE/HIGH/EXTREME
- confidence/data quality
- estimated hazard arrival minutes
- evacuation time where route information exists
- recommended action
- factor contributions

## Hazard arrival
Treat this as an estimate derived from scenario assumptions and available upstream/terrain information. It is not a certified hydrological forecast.

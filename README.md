# dynamic_risk_assessment_system

## Overview 
The goal of this project is to provide a dynamic risk assessment solution that can help organizations make informed decisions based on data. The project follows MLOps best practices to ensure the highest quality of code, model, and deployment. It includes:

* Data ingestion from multiple sources
* Model training and evaluation
* Model scoring and diagnostics
* Deployment with API and web interface
* Automated reporting and logging

## Execution

1. To initiate the complete sequence, execute the following command:
```bash
python utils/fullprocess.py
```

2. Ingestion: This script searches for new .csv formatted data for training. It combines all found data and stores it in a designated folder.
```bash
python utils/ingestion.py
```

3. Training, Evaluation & Rollout: This series of commands will train a Logistic Regression Model to predict potential employee departures. It also scores the model using test data and preps everything for live deployment.
```bash
python utils/training.py
python utils/scoring.py
python utils/deployment.py

```

4. Diagnostics: This script generates a variety of statistical and operational metrics to quickly verify the data integrity and monitor package updates.
```bash
python utils/diagnostics.py
```

5. Reporting: A straightforward confusion matrix is generated for diagnostic purposes.
```bash
python utils/reporting.py
```
Lastly, there's an accompanying file for setting up a cron job to run every 10 minutes (conjob.txt)
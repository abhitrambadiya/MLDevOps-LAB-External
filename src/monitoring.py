import os
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

def run_monitoring():
    os.makedirs("reports", exist_ok=True)
    ref = pd.DataFrame({"a": [1, 2, 3, 4, 5], "b": [10, 20, 30, 40, 50]})
    curr = pd.DataFrame({"a": [2, 3, 4, 5, 6], "b": [15, 25, 35, 45, 55]})
    report = Report(metrics=[DataDriftPreset()])
    res = report.run(reference_data=ref, current_data=curr)
    path = "reports/evidently_drift_report.html"
    res.save_html(path)
    print(f"Evidently report saved to {path}")
    return path

if __name__ == "__main__":
    run_monitoring()

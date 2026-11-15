"""
Evidently AI Monitoring Integration for Multiplication Service
Problem Statement C - ML DevOps POE
Generates data drift & data quality reports comparing reference and production inputs.
"""

import os
import sys
import numpy as np
import pandas as pd

try:
    from math_operations import multiply
except ImportError:
    from src.math_operations import multiply


def generate_reference_data(n_samples: int = 100) -> pd.DataFrame:
    """Generate baseline/reference data for normal multiplication inputs."""
    np.random.seed(42)
    a_vals = np.random.uniform(1.0, 50.0, size=n_samples)
    b_vals = np.random.uniform(1.0, 50.0, size=n_samples)
    results = [multiply(float(a), float(b)) for a, b in zip(a_vals, b_vals)]

    return pd.DataFrame({
        "num1": a_vals,
        "num2": b_vals,
        "product": results
    })


def generate_current_data(n_samples: int = 100, drift: bool = True) -> pd.DataFrame:
    """Generate current/production batch of multiplication inputs."""
    np.random.seed(101)
    if drift:
        # Shifted distribution to demonstrate drift detection in POE
        a_vals = np.random.uniform(50.0, 200.0, size=n_samples)
        b_vals = np.random.uniform(50.0, 200.0, size=n_samples)
    else:
        a_vals = np.random.uniform(1.0, 50.0, size=n_samples)
        b_vals = np.random.uniform(1.0, 50.0, size=n_samples)

    results = [multiply(float(a), float(b)) for a, b in zip(a_vals, b_vals)]

    return pd.DataFrame({
        "num1": a_vals,
        "num2": b_vals,
        "product": results
    })


def run_evidently_report(output_dir: str = "reports") -> str:
    """
    Run Evidently data drift and summary analysis and generate HTML report.
    Returns the absolute path of the generated HTML report.
    """
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "evidently_drift_report.html")

    reference_df = generate_reference_data(100)
    current_df = generate_current_data(100, drift=True)

    try:
        from evidently import Report
        from evidently.presets import DataDriftPreset, DataSummaryPreset

        report = Report(metrics=[DataDriftPreset(), DataSummaryPreset()])
        snapshot = report.run(reference_data=reference_df, current_data=current_df)

        # Evidently version compatibility handling
        if hasattr(snapshot, "save_html"):
            snapshot.save_html(report_path)
        elif hasattr(report, "save_html"):
            report.save_html(report_path)
        else:
            raise RuntimeError("Evidently Report object has no save_html method.")

    except ImportError:
        # Fallback if evidently structure is legacy
        try:
            from evidently.report import Report
            from evidently.metric_preset import DataDriftPreset, DataQualityPreset

            report = Report(metrics=[DataDriftPreset(), DataQualityPreset()])
            report.run(reference_data=reference_df, current_data=current_df)
            report.save_html(report_path)
        except Exception as e:
            print(f"Error executing Evidently report: {e}")
            raise

    print(f"Evidently report generated successfully at: {report_path}")
    return report_path


if __name__ == "__main__":
    report_file = run_evidently_report()
    print(f"Report ready: {report_file}")

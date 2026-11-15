"""
Tests for Evidently AI data drift and monitoring pipeline.
"""

import os
import sys
import pytest

# Ensure src is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from monitoring import generate_reference_data, generate_current_data, run_evidently_report


def test_reference_data_generation():
    """Verify reference dataset schema and row count."""
    df = generate_reference_data(50)
    assert len(df) == 50
    assert list(df.columns) == ["num1", "num2", "product"]
    assert (df["num1"] > 0).all()


def test_current_data_generation():
    """Verify current dataset schema and row count."""
    df = generate_current_data(50, drift=False)
    assert len(df) == 50
    assert list(df.columns) == ["num1", "num2", "product"]


def test_evidently_html_report_generation(tmp_path):
    """Verify that Evidently generates a non-empty HTML report file."""
    report_file = run_evidently_report(output_dir=str(tmp_path))
    assert os.path.exists(report_file)
    assert os.path.getsize(report_file) > 1000

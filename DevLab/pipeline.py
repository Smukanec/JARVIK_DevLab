"""Pipeline module for running models sequentially.

This module defines a simple pipeline that runs two models in order:
"Command R+" followed by "StrCoder". The second model receives the
output from the first one as its prompt. The models run sequentially to
avoid any concurrent execution.
"""

from __future__ import annotations

import json
from typing import Any, Dict
import requests


class Pipeline:
    """Sequential pipeline for running Jarvik models."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def _run_model(self, model: str, prompt: str) -> str:
        """Call a Jarvik model and return its output.

        Parameters
        ----------
        model:
            Name of the model to invoke.
        prompt:
            Text prompt for the model.
        """
        payload: Dict[str, Any] = {"model": model, "prompt": prompt}
        try:
            resp = requests.post(f"{self.base_url}/run", json=payload, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            return data.get("output", "")
        except requests.RequestException:
            # In case of connection issues or invalid responses, return empty string
            return ""

    def run(self, prompt: str) -> str:
        """Run the pipeline with the given prompt."""
        first_output = self._run_model("Command R+", prompt)
        final_output = self._run_model("StrCoder", first_output)
        return final_output

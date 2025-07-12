"""Pipeline module for running models sequentially.

The pipeline inspects an input prompt, determines the language or task
and chooses an appropriate pair of Jarvik models. Information about the
selection is written to ``logs/`` for traceability.
"""

from __future__ import annotations

from typing import Any, Dict, List
from pathlib import Path
from datetime import datetime
import requests

from .utils import detect_language


class Pipeline:
    """Sequential pipeline for running Jarvik models."""

    def __init__(self, base_url: str, log_dir: Path | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.log_dir = log_dir or Path(__file__).with_name("logs")
        self.log_dir.mkdir(exist_ok=True)

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

    def _log_selection(self, language: str, models: List[str]) -> None:
        """Write the chosen language and models into the log directory."""
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        path = self.log_dir / f"{timestamp}_pipeline.log"
        with path.open("w", encoding="utf-8") as fh:
            fh.write(f"language: {language}\n")
            fh.write(f"models: {', '.join(models)}\n")

    def run(self, prompt: str) -> str:
        """Run the pipeline with the given prompt."""
        language = detect_language(prompt)
        lowered = prompt.lower()
        if "api" in lowered or "cli" in lowered:
            models = ["llama3:8b", "codellama:7b-instruct"]
        elif language in {"html", "php", "json"}:
            models = ["mistral:7b", "llama3:8b"]
        elif language == "python":
            models = ["codellama:7b-instruct", "starcoder:7b"]
        elif language in {"c", "sql"}:
            models = ["starcoder:7b", "codellama:7b-instruct"]
        else:
            models = ["llama3:8b"]

        self._log_selection(language, models)

        output = prompt
        for model in models:
            output = self._run_model(model, output)
        return output

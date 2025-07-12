# DevLab Module

DevLab extends Jarvik with an experimental development pipeline. It
communicates with the Jarvik API and stores context from every
interaction. The module runs two AI models in sequence using
`pipeline.Pipeline`. Its main entry point is `dev_engine.DevEngine`.

## Model selection

The pipeline inspects the prompt and chooses the Jarvik models to run:

* **Python** prompts → `codellama:7b-instruct` then `starcoder:7b`
* **HTML**, **PHP** or **JSON** → `mistral:7b` then `llama3:8b`
* **API** or **CLI** design → `llama3:8b` then `codellama:7b-instruct`
* **General queries** → `llama3:8b`
* **C**, **SQL** or other languages → `starcoder:7b` then `codellama:7b-instruct`

Information about the detected language and selected models is saved in
the `logs/` directory.

## Architecture

```
prompt → DevEngine → Pipeline → [Jarvik models] → result
              │                           │
              └── dev_memory/             └── logs/
```

The `DevEngine` orchestrates model calls via the `Pipeline`. Every
interaction is archived in `dev_memory/` and, if logging is enabled, a
copy of the output is written to `logs/`.

## Purpose

* Integrate Jarvik with auxiliary models for code generation.
* Persist prompts and outputs in `dev_memory/` with default topics
  "programování" and "technologie".
* Optionally log anonymized results to `logs/` for later review.

## Development flow

1. A prompt is passed to `DevEngine.run()`.
2. The prompt is processed by the pipeline according to the selected
   model pair (e.g. `codellama:7b-instruct` -> `starcoder:7b`).
3. The output is stored in `dev_memory/` and returned to the caller.
4. If logging is enabled, the result is also written to `logs/`.

## Using from `Jarvik_W`

The DevLab module can be imported from other applications such as
`Jarvik_W`:

```python
from DevLab.dev_engine import DevEngine

engine = DevEngine()
response = engine.run("Generate hello world")
print(response)
```

The connection URL to the Jarvik API can be adjusted in
`DevLab/devlab_config.json`.

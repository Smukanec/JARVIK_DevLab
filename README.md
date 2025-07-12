# 🧠 DevLab – Vývojová vrstva nad Jarvikem / DevLab – Development layer for Jarvik

## English

**DevLab** is a standalone development sub‑application within the **Jarvik** ecosystem. It focuses on intelligent code generation, validation and management with help of cooperating AI models. While the project is in an early stage, it aims to simplify Python development, API design and working with GitHub repositories.

### Features
- AI assisted generation of code snippets
- Simple validation stubs ready for future extension
- `DevLabManager` orchestrating generation and validation steps
- Designed to integrate with the Jarvik platform

### Installation
1. Clone this repository
```bash
git clone https://github.com/your-org/jarvik-devlab.git
cd jarvik-devlab
```
2. Ensure that Python 3 is installed and accessible as `python3` or `python`
3. Run `./install.sh` to create a `.venv` directory and install the package
4. Activate the environment with `source .venv/bin/activate` (or `.venv\\Scripts\\activate` on Windows)
5. Run `./upgrade.sh` anytime to update to the newest release

For Ubuntu Server 25.04 you can automate these steps with `setup_dev_lab.sh`:
```bash
./setup_dev_lab.sh
```

### Basic usage
```python
from devlab.manager import DevLabManager

manager = DevLabManager()
code = manager.run("Create a simple Hello World application")
print(code)
```

### Models and architecture

DevLab decides which Jarvik models to call based on the detected
language or task:

* **Python** → `codellama:7b-instruct` then `starcoder:7b`
* **HTML**, **PHP** or **JSON** → `mistral:7b` then `llama3:8b`
* **API** or **CLI** design → `llama3:8b` then `codellama:7b-instruct`
* **General queries** → `llama3:8b`
* **C**, **SQL** or other languages → `starcoder:7b` then `codellama:7b-instruct`

Prompts and outputs are persisted in `DevLab/dev_memory/` while optional
logs are stored in `DevLab/logs/`. The orchestration happens in
`DevLab.dev_engine.DevEngine`.

### Contributing
Contributions are welcome! Fork the repository, create a feature branch and open a pull request.

For offline type checking, install the development requirements:

```bash
pip install -r dev-requirements.txt
```

### Reporting issues
If you encounter problems or have suggestions, please open an issue on GitHub.

### License
This project is released under the [MIT License](LICENSE).

---

## Čeština

**DevLab** je samostatná vývojová podaplikace v rámci systému **Jarvik**. Jejím cílem je generovat, validovat a spravovat kód pomocí spolupracujících AI modelů. Projekt je v rané fázi, ale má ulehčit vývoj v Pythonu, návrhy API i práci s GitHub repozitáři.

### Funkce
- Generování úryvků kódu za pomoci AI
- Základní validace připravené k dalšímu rozšiřování
- `DevLabManager` koordinuje kroky generování a validace
- Navrženo pro integraci do platformy Jarvik

### Instalace
1. Naklonujte tento repozitář
```bash
git clone https://github.com/your-org/jarvik-devlab.git
cd jarvik-devlab
```
2. Ujistěte se, že máte nainstalován Python 3 a je dostupný jako `python3` nebo `python`
3. Spusťte `./install.sh`, který vytvoří adresář `.venv` a nainstaluje balíček
4. Prostředí aktivujete příkazem `source .venv/bin/activate` (na Windows `.venv\\Scripts\\activate`)
5. Pro aktualizaci na nejnovější verzi použijte `./upgrade.sh`

Pro Ubuntu Server 25.04 lze všechny kroky automatizovat skriptem `setup_dev_lab.sh`:
```bash
./setup_dev_lab.sh
```

### Základní použití
```python
from devlab.manager import DevLabManager

manager = DevLabManager()
code = manager.run("Vytvoř jednoduchou aplikaci Hello World")
print(code)
```

### Modely a architektura

DevLab vybírá Jarvik modely podle rozpoznaného jazyka nebo úkolu:

* **Python** → `codellama:7b-instruct` a poté `starcoder:7b`
* **HTML**, **PHP** či **JSON** → `mistral:7b` a `llama3:8b`
* **Návrh API** nebo **CLI** → `llama3:8b` a `codellama:7b-instruct`
* **Obecné dotazy** → `llama3:8b`
* **C**, **SQL** a ostatní jazyky → `starcoder:7b` a `codellama:7b-instruct`

Každý prompt i výstup jsou uloženy do `DevLab/dev_memory/`. Volitelné
logy vznikají v `DevLab/logs/`. O orchestraci se stará
`DevLab.dev_engine.DevEngine`.

### Jak přispět
Budeme rádi za pull requesty. Forkněte repozitář, vytvořte větev a odešlete návrh ke schválení.

### Hlášení chyb
Pro nahlášení chyby nebo návrh nového vylepšení založte issue na GitHubu.

### Licence
Tento projekt je publikován pod licencí [MIT License](LICENSE).


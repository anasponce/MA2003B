# Application of Multivariate Methods in Data Science

Repositorio para análisis estadístico y métodos multivariados en Python.

## Estructura
- `src/app_mvm/`: código de la librería (reutilizable).
- `notebooks/`: notebooks exploratorios (usar kernel del proyecto).
- `data/raw/`: datos crudos (se descargan localmente, no se versionan).
- `data/interim/`, `data/processed/`: etapas de transformación.
- `scripts/`: utilidades (p.ej. descarga de datasets).
- `tests/`: pruebas con `pytest`.

## Guías
- [Cómo trabajar en tu propia rama (equipo)](docs/TEAM_SETUP.md)

## Requisitos
- Python 3.11+, Git, VS Code
- Extensiones: Python, Jupyter, Pylance
- (Windows) Habilitar rutas largas:
  ```powershell
  # PowerShell como Administrador
  reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
Setup rápido (mantenedor)
powershell
Copiar
Editar
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -e .[dev]
python -m ipykernel install --user --name app-mvm --display-name "Python (app-mvm)"
pre-commit install
nbstripout --install
yaml
Copiar
Editar

---

## 📄 docs/TEAM_SETUP.md (tutorial para el equipo)

Crea la carpeta `docs/` (si no existe) y pega este contenido en `docs/TEAM_SETUP.md`:

```markdown
# Team Setup & Workflow (Windows/PowerShell)

Guía para que cada integrante trabaje en **su propia rama** y ejecute el proyecto con un **entorno virtual** y **notebooks**.

---

## Índice
- [0) Prerrequisitos (una vez)](#0-prerrequisitos-una-vez)
- [1) Clonar el repositorio (una vez)](#1-clonar-el-repositorio-una-vez)
- [2) Crear tu rama personal](#2-crear-tu-rama-personal)
- [3) Entorno virtual y dependencias (una vez por repo)](#3-entorno-virtual-y-dependencias-una-vez-por-repo)
- [4) Datos locales (no se suben)](#4-datos-locales-no-se-suben)
- [5) Flujo de trabajo diario](#5-flujo-de-trabajo-diario)
- [6) Pull Request (PR)](#6-pull-request-pr)
- [7) Añadir nuevas dependencias](#7-añadir-nuevas-dependencias)
- [8) Problemas comunes (FAQ)](#8-problemas-comunes-faq)
- [9) Mini-resumen de comandos](#9-mini-resumen-de-comandos)

---

## 0) Prerrequisitos (una vez)
- **Instalar**: Git, Python 3.11+, VS Code
- **Extensiones VS Code**: Python, Jupyter, Pylance
- **Windows**: habilitar rutas largas (PowerShell **Administrador**):
  ```powershell
  reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
Acceso a GitHub:

HTTPS (simple): se abre el navegador al primer git push.

SSH (estable): configura llave SSH y usa URL git@github.com:....

1) Clonar el repositorio (una vez)
powershell
Copiar
Editar
# HTTPS
git clone https://github.com/JorgeAndujoV/Application-of-multivariate-methods-in-data-science.git
cd Application-of-multivariate-methods-in-data-science

# (Opcional) SSH si ya configuraste llave:
# git clone git@github.com:JorgeAndujoV/Application-of-multivariate-methods-in-data-science.git
2) Crear tu rama personal
Usa tu nombre (p.ej., Jorge) o Nombre/feature-xyz. Trabaja siempre en tu rama.

powershell
Copiar
Editar
git switch -c Jorge      # reemplaza "Jorge" por tu nombre
git push -u origin Jorge
3) Entorno virtual y dependencias (una vez por repo)
powershell
Copiar
Editar
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install -U pip

# Dependencias del proyecto (definidas por el repo)
pip install -e .[dev]

# Si lo anterior no existe en tu entorno, usa:
# pip install -e .
# pip install ipykernel ruff black pytest pytest-cov pre-commit nbstripout mypy
Kernel de Jupyter del proyecto:

powershell
Copiar
Editar
python -m ipykernel install --user --name app-mvm --display-name "Python (app-mvm)"
Hooks de pre-commit:

powershell
Copiar
Editar
pre-commit install
nbstripout --install
En VS Code:

Intérprete Python: .\.venv\Scripts\python.exe

En notebooks: kernel Python (app-mvm)

4) Datos locales (no se suben)
Los datasets no se versionan; se descargan localmente a data/raw/.

powershell
Copiar
Editar
python scripts\get_data.py           # descarga todo (según data/datasets.yml)
# o solo algunos:
# python scripts\get_data.py iris wine
5) Flujo de trabajo diario
Antes de empezar:

powershell
Copiar
Editar
git switch Jorge
git fetch origin
git merge origin/main               # (o: git rebase origin/main)

. .\.venv\Scripts\Activate.ps1
# si cambió pyproject/requirements:
pip install -e .[dev]
# si cambió data/datasets.yml:
python scripts\get_data.py
Trabajar:

Código reutilizable en src/app_mvm/...

Notebooks en notebooks/ (con kernel del proyecto)

No subir data/raw/

Validar:

powershell
Copiar
Editar
ruff check .
black --check .
pytest
# (opcional) mypy
mypy
(Para autoformatear si falla black --check):

powershell
Copiar
Editar
black .
Commit & push:

powershell
Copiar
Editar
git status
git add -A
git commit -m "feat: agrega pipeline PCA y scree plot"
git push
6) Pull Request (PR)
Abrir PR de tu rama → main en GitHub.

Esperar CI en verde (lint/tests) y revisión.

Tras el merge:

powershell
Copiar
Editar
git switch main
git pull
git branch -d Jorge                 # borrar rama local (opcional)
git push origin --delete Jorge      # borrar rama remota (opcional)
git switch -c Jorge                 # crear rama nueva para la siguiente tarea
git push -u origin Jorge
7) Añadir nuevas dependencias
Pedir al mantenedor que agregue el paquete en pyproject.toml.

Luego reinstalar:

powershell
Copiar
Editar
. .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
8) Problemas comunes (FAQ)
<details> <summary><strong>HTTPS empuja con la cuenta equivocada / 403</strong></summary>
powershell
Copiar
Editar
git credential-manager erase https://github.com
git push   # reautentica en el navegador con la cuenta correcta
</details> <details> <summary><strong>No module named ipykernel</strong></summary>
powershell
Copiar
Editar
. .\.venv\Scripts\Activate.ps1
pip install ipykernel
python -m ipykernel install --user --name app-mvm --display-name "Python (app-mvm)"
</details> <details> <summary><strong>Rutas demasiado largas (Windows)</strong></summary>
Habilitar Long Paths (PowerShell Administrador):

powershell
Copiar
Editar
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
Y preferir rutas cortas sin espacios/acentos (ej. C:\code\proyecto).

</details> <details> <summary><strong>El notebook usa el Python equivocado</strong></summary>
En VS Code, cambia el kernel a Python (app-mvm). Verifica además:

powershell
Copiar
Editar
where python
where pip
python -c "import sys; print(sys.executable)"  # debe apuntar a .\.venv\Scripts\python.exe
</details> <details> <summary><strong>Conflictos de merge</strong></summary>
Edita archivos con <<<<<<<, =======, >>>>>>>.

Marca resuelto y commitea:

powershell
Copiar
Editar
git add -A
git commit
</details>
9) Mini-resumen de comandos
powershell
Copiar
Editar
# primera vez
git clone https://github.com/JorgeAndujoV/Application-of-multivariate-methods-in-data-science.git
cd Application-of-multivariate-methods-in-data-science
git switch -c MiNombre
git push -u origin MiNombre

python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -e .[dev]
python -m ipykernel install --user --name app-mvm --display-name "Python (app-mvm)"
pre-commit install
nbstripout --install
python scripts\get_data.py

# cada día
git switch MiNombre
git fetch origin
git merge origin/main
. .\.venv\Scripts\Activate.ps1
pip install -e .[dev]         # si cambió pyproject
python scripts\get_data.py     # si cambió datasets.yml

# trabajar, validar y subir
ruff check . && black --check . && pytest
git add -A
git commit -m "feat: mi cambio"
git push
# abrir PR → revisión → merge

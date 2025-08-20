Team Setup & Workflow (Windows/PowerShell)
0) Prerequisitos (una sola vez por persona)

Instalar Git, Python 3.11+, VS Code.

Habilitar rutas largas (PowerShell Administrador):

reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f


(Reiniciar Windows). Opcional:

git config --global core.longpaths true


Extensiones VS Code: Python, Jupyter, Pylance.

Acceso a GitHub

HTTPS (simple): en el primer git push se abre el navegador para iniciar sesión.

SSH (estable): configurar llave SSH y usar URLs git@github.com:....
Si ya usas SSH, perfecto.

1) Clonar el repositorio (una sola vez)
# HTTPS
git clone https://github.com/JorgeAndujoV/Application-of-multivariate-methods-in-data-science.git
cd Application-of-multivariate-methods-in-data-science

# (Opcional) SSH, si ya tienes llave configurada:
# git clone git@github.com:JorgeAndujoV/Application-of-multivariate-methods-in-data-science.git

2) Crear tu rama personal (por nombre)

Ejemplos: Jorge, Ana, Luis.

Si prefieres, usa Nombre/feature-xyz.

git switch -c Jorge   # cambia "Jorge" por tu nombre
git push -u origin Jorge


A partir de aquí trabaja siempre en tu rama (no en main).

3) Crear y activar entorno virtual (por repo, una sola vez)

En la raíz del repo:

python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install -U pip


Instalar dependencias del proyecto (definidas por el mantenedor):

# runtime + herramientas de desarrollo
pip install -e .[dev]


Si ese comando no existe, usa:

pip install -e .
pip install ipykernel ruff black pytest pytest-cov pre-commit nbstripout mypy


Registrar el kernel de Jupyter de este entorno:

python -m ipykernel install --user --name app-mvm --display-name "Python (app-mvm)"


Instalar hooks de pre-commit (formato/lint automáticos):

pre-commit install
nbstripout --install

4) Datos (no se suben al repo)

Descargar datasets localmente con el script del proyecto:

python scripts\get_data.py      # descarga todo lo definido en data/datasets.yml
# o solo algunos:
# python scripts\get_data.py iris wine


Los datos se guardan en data/raw/ y están ignorados por Git.

5) Flujo de trabajo diario
5.1 Antes de empezar cada día
# en la raíz del repo
git switch Jorge                      # tu rama personal
git fetch origin
git merge origin/main                 # trae cambios de main a tu rama (o: git rebase origin/main)

. .\.venv\Scripts\Activate.ps1        # activar el entorno
# si cambió pyproject/requirements:
pip install -e .[dev]
# si cambió datasets.yml:
python scripts\get_data.py


En VS Code:

Selecciona intérprete: .\.venv\Scripts\python.exe

En notebooks, kernel Python (app-mvm) (arriba a la derecha).

5.2 Hacer cambios

Código reutilizable en src/app_mvm/...

Notebooks en notebooks/ (outputs limpios gracias a nbstripout).

No subas datos crudos (data/raw/).

5.3 Validar localmente
ruff check .
black --check .
pytest
# (opcional) mypy
mypy


Si black --check falla, puedes autoformatear:

black .

5.4 Commit & push

Usa mensajes tipo Conventional Commits (feat:, fix:, docs:, test:, etc.):

git status
git add -A
git commit -m "feat: agrega pipeline PCA y scree plot"
git push

6) Abrir Pull Request (PR)

En GitHub: abre un PR de tu rama → main.

El CI corre (lint/tests). Corrige si falla.

Pide revisión a un compañero.

Cuando aprueben: merge.

Tras el merge:

git switch main
git pull
git branch -D Jorge           # borra tu rama local (opcional)
git push origin --delete Jorge  # borra la rama remota (opcional)
# crea una nueva rama para la siguiente tarea
git switch -c Jorge
git push -u origin Jorge

7) Añadir dependencias nuevas (si lo necesitas)

Pídele al mantenedor que agregue el paquete en pyproject.toml (sección dependencies o optional-dependencies.dev).

Luego cada integrante:

. .\.venv\Scripts\Activate.ps1
pip install -e .[dev]

8) Resolución de problemas comunes

A) 403 / cuenta equivocada en GitHub (HTTPS)

git remote -v
git credential-manager erase https://github.com
git push   # reautentica en navegador con tu cuenta correcta


B) No module named ipykernel

. .\.venv\Scripts\Activate.ps1
pip install ipykernel
python -m ipykernel install --user --name app-mvm --display-name "Python (app-mvm)"


C) Rutas demasiado largas (Windows)

Asegura LongPathsEnabled = 1 (ver sección 0).

Evita carpetas con espacios/acentos o usa una ruta corta (ej. C:\code\proyecto).

D) El notebook usa el Python equivocado

En VS Code: cambia el kernel a Python (app-mvm).

Verifica:

where python
where pip
python -c "import sys; print(sys.executable)"
# Deben apuntar a .\.venv\Scripts\...


E) Conflictos de merge

Abre los archivos con marcas <<<<<<<, =======, >>>>>>>.

Resuelve manualmente, guarda.

git add -A
git commit

9) Checklist rápido (para cada integrante)

 Cloné el repo y creé mi rama (git switch -c MiNombre + git push -u origin MiNombre).

 Creé y activé .venv, instalé dependencias (pip install -e .[dev]).

 Registré kernel Python (app-mvm) y lo uso en notebooks.

 Descargué datos con python scripts\get_data.py.

 Antes de cada día: git fetch, merge origin/main, activar venv, reinstalar si cambió.

 Antes de cada commit: pre-commit run --all-files, pytest.

 Abrí PR a main, CI en verde, revisión aprobada, merge.

Mini-resumen de comandos (copiable)
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
pip install -e .[dev]        # si cambió pyproject
python scripts\get_data.py    # si cambió datasets.yml

# trabajar, validar y subir
ruff check . && black --check . && pytest
git add -A
git commit -m "feat: mi cambio"
git push
# abrir PR → revisión → merge

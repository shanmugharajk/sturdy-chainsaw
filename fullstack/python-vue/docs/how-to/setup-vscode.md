# Setting up vscode

The following settings are recommended (settings.json)

```json
{
  // == Python settings ==
  "python.venvPath": "${env:VENV_PATH}",
  "python.pythonPath": "${env:VENV_PATH}/bin/python",
  "python.languageServer": "Pylance",
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Path": "${env:VENV_PATH}/bin/flake8",
  "python.formatting.blackPath": "${env:VENV_PATH}/bin/black",
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "100"],
  "python.linting.enabled": true,
  "python.analysis.extraPaths": ["./src/todos"],

  //== Editor settings ==
  "editor.tabSize": 4,
  "editor.formatOnSave": true
}
```

`VENV_PATH` in that an environment variable pointing to the virtual environment path.

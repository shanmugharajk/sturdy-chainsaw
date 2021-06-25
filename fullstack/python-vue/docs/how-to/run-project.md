# How to run project

## Using terminal

To run the python project,

1. First set the python path to `src` directory. Run `export PYTHONPATH=./src`.

2. Then the start the fastapi server run `uvicorn todos.main:app --reload` in the project root.

Since we are making `todos` as module we need to adjust the `PYTHONPATH` incase if we run the project from the root directory (ie. where the `src` lies on).

## Using vscode

To run from vscode we need to have the recommended settings. Refer [here](./setup-vscode.md).

Create a `launch.json` file inside `.vscode` folder.

```json
{
  "configurations": [
    {
      "name": "Server Debug",
      "type": "python",
      "request": "launch",
      "env": {
        "PYTHONPATH": "src"
      },
      "program": "${workspaceFolder}/bin/run.py"
    }
  ]
}
```

After this setup is completed, press F5 and see the project up and running.

# where to start
- uv's website at https://docs.astral.sh/uv/

# how to install
- follow uv's website instructions at https://docs.astral.sh/uv/getting-started/installation/
- in ubuntu, copy and paste this to the terminal - you have to have curl installed
```curl -LsSf https://astral.sh/uv/install.sh | sh```

# how to check uv's installed version
- in the terminal
```uv --version```

# how to update uv
- in the terminal
```uv self update```

# how to start a project
- create a folder for the project
- cd to that folder
- start the project with uv init. An example, using python 3.12 and the project named myProject
```uv init -p 3.12 --name myProject```

# how to add packages/ dependencies to the project
- in the terminal, example adding the pandas package
```uv add pandas```


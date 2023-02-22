# Kurs for it.gruppen med Bouvet


<p align="center">
  <img src="static/bouvet_data.jpg" width="70%"/>
</p>
## Setup for kurset

Installer `requirements.txt` filen i et python virtualenv. Har du brukt Anaconda før kan du bruke det hvis du er komfortabel med det. Forslag til `IDE` er Visual Studio Code kort VSCode.

### Windows

1. Åpne `Powershell/cmd` eller `IDE` i denne mappen
2. 
```pwsh
py -m venv .venv

.venv\Scripts\activate
# ev.
.venv\Scripts\Activate

pip install -r requirements.txt
```

### Mac/Linux

Stegvis fremgangsmåte

1. Åpne `Terminal` eller `IDE` i denne mappen
2. 
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Starte Jupyter Lab

Når du har installert requirements filen og startet venv/virtualenv, skriver du følgende i termninal/cmd-prompten du akkurat jobbet i:

```shell
jupyter lab
```

Jupyter Lab vil åpne seg i standardnettleseren din


## Azure functions (kun for del 2 av kurset)

```
Det er ikke nødvendig å laste ned før kursets del 2
```

Her vil du trenge Azure CLI og Azure Function core tools:


Azure CLI:

```
https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli
```


Azure Function Core tools:

```
https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools
```


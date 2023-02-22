# Kurs for it.grruppen med bouvet

## Setup for kurset

Installer `requirements.txt` filen i et python virtualenv. Bruker du Anaconda kan du gjøre det hvis du vil

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

### Mac

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
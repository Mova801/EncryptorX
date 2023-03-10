# EncryptorX

__README NEED UPDATE__

![python](https://img.shields.io/static/v1?label=python&message=3.11&color=green&style=for-the-badge&logo=python) ![version](https://img.shields.io/static/v1?label=version&message=0.0.3-alpha&color=green&style=for-the-badge) ![author](https://img.shields.io/static/v1?label=author&message=Mova801&color=blue&style=for-the-badge) ![author](https://img.shields.io/static/v1?label=license&message=MIT&color=success&style=for-the-badge)

## Requirements

Per permettere il corretto funzionamento dell'app è necessario installare alcune librerie di python. Qui sono riportati
due modi.

---

### `installazione locale`

Aprire il terminale, spostarsi nella cartella in cui è presente l'app e inserire il seguente comando:

```shell
C:\...\appfolder> pip install -r requirements.txt
```

Una volta conclusa l'operazione le librerie saranno installate sul computer e sarà possibile eseguire l'applicazione.

---

### `virtual environment`

Aprire il terminale, spostarsi nella cartella in cui è presente l'app e installare la libreria `virtualenv` con il
comando:

```shell
C:\...\appfolder> pip install virtualenv
```

Una volta conclusa l'operazione inserire la seguente sequenza di comandi:

```shell
C:\...\appfolder> virtualenv nome_ambiente_virtuale
C:\...\appfolder> nome_ambiente_virtuale\Scripts\activate
(nome_ambiente_virtuale) C:\..\appfolder> pip install -r requirements.txt 
```

Quando nel terminale vediamo scritto `(nome_ambiente_virtuale)` accanto al percorso in cui si troviamo significa che
l'ambiente è attivo.

Adesso l'ambiente virtuale è pronto e l'app può essere avviata.

```shell
(nome_ambiente_virtuale) C:\..\appfolder> run.py
```

Per deattivare l'ambiente virtuale inserire nel terminale il comando:

```shell
(nome_ambiente_virtuale) C:\..\appfolder> nome_ambiente_virtuale\Scripts\deactivate
```

---

## Application folder structure

- `controller`: package contenente la parte di app che gestisce `model` e `view`.
- `model`: package contenente logica da eseguire quando l'utente interagisce con l'app.
- `view`: package contenente l'interfaccia grafica dell'app e le sue impostazioni.
- `resource`: package contenente alcune parti della logica dell'app; personalizzabili dall'utente.
- `util`: package contenente librerie di supporto.
- `logger`: package contenente la logica di logging dell'app.
- `logs`: cartella contenente i log riguardo all'utilizzo dell'app (azioni ed errori).
- `run.py`: modulo python per eseguire l'applicazione.
- `EXTRA`: app info.

__Nota:__ _in caso di errori e malfunzionamenti avvisare lo sviluppatore._

---


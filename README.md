# SimpleGUIApplication

![python](https://img.shields.io/static/v1?label=python&message=3.10&color=green&style=for-the-badge) ![version](https://img.shields.io/static/v1?label=version&message=0.0.1-alpha&color=green&style=for-the-badge) ![author](https://img.shields.io/static/v1?label=author&message=Mova801&color=blue&style=for-the-badge) ![author](https://img.shields.io/static/v1?label=license&message=MIT&color=important&style=for-the-badge)


- [SimpleGUIApplication](#simpleguiapplication)
  - [Requirements](#requirements)
    - [`installazione locale`](#installazione-locale)
    - [`virtual environment`](#virtual-environment)
  - [Application folder structure](#application-folder-structure)
  - [Application `resources` folder](#application-resources-folder)
  - [General Application info](#general-application-info)


## Requirements

Per permettere il corretto funzionamento dell'app è necessario installare alcune librerie di python.
Qui sono riportati due modi.

---

### `installazione locale`

Aprire il terminale, spostarsi nella cartella in cui è presente l'app e inserire il seguente comando:

```shell
C:\...\appfolder> pip install -r requirements.txt
```

Una volta conclusa l'operazione le librerie saranno installate sul computer e sarà possibile eseguire l'applicazione.

---

### `virtual environment`

Aprire il terminale, spostarsi nella cartella in cui è presente l'app e installare la libreria `virtualenv` con il comando:

```shell
C:\...\appfolder> pip install virtualenv
```

Una volta conclusa l'operazione inserire la seguente sequenza di comandi:

```shell
C:\...\appfolder> virtualenv nome_ambiente_virtuale
C:\...\appfolder> nome_ambiente_virtuale\Scripts\activate
(nome_ambiente_virtuale) C:\..\appfolder> pip install -r requirements.txt 
```

Quando nel terminale vediamo scritto `(nome_ambiente_virtuale)` accanto al percorso in cui si troviamo significa che l'ambiente è attivo.

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

- `controller`: package contenente logica da eseguire quando l'utente interagisce con l'app.
- `gui`: package contenente l'interfaccia grafica dell'app e le sue impostazioni.
- [`resource`](#resources): package contenente alcune parti della logica dell'app.
- `util`: package contenente librerie di supporto.
- `log`: cartella contenente informazioni sull'ultimo utilizzo dell'app.
- `run.py`: modulo python per eseguire l'applicazione.
- `EXTRA`: app info.

---

## Application `resources` folder

SimpleGUIApplication al click del pulsante `COMPUTE` esegue qualsiasi cosa sia presente nella funzione `main` del modulo `elaborate.py`.

Il risultato della funzione __DEVE__ necessariamente essere una stringa, altrimenti il programma non considera il risultato corretto. Se il risultato è corretto viene mostrato nell'app.

Il modulo da importare è specificato nella variabile `MODULE_TO_IMPORT` contenuta nel modulo `constants`.

```python
MODULE_TO_IMPORT: str = "nome_modulo_da_importare"
```

_La modifica del modulo da importare è sconsigliata; si suggerisce di modificare il modulo di default scrivendo nella funzione `main`._

---

## General Application info

L'app appena avviata dovrebbe apparire così

<img alt="just started app" src="EXTRA\app_layout.png" title="started app" width="600"/>

Non ci sono ancora molti controlli sugli input. In ogni caso, finché l'utente non inserisce del testo nel textbox di input il pulsante `COMPUTE` rimane disattivato.

<img alt="just started app" src="EXTRA\app_layout2.png" title="started app" width="600"/>

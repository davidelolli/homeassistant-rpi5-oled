# RPi5 OLED Monitor - Documentazione

## Descrizione

Questo addon mostra informazioni di sistema in tempo reale su un display OLED I2C collegato al Raspberry Pi 5.

## Informazioni visualizzate

- **CPU:** Utilizzo percentuale e frequenza corrente
- **Memoria RAM:** Utilizzo e totale disponibile
- **Temperatura:** Temperatura del processore
- **Storage:** Spazio disponibile su disco
- **Rete:** Indirizzo IP locale

## Prerequisiti obbligatori

### 1. Hardware
- Raspberry Pi 5 con Home Assistant OS
- Display OLED I2C compatibile (indirizzo 0x2D)
- Display collegato correttamente ai pin I2C del Raspberry Pi

### 2. Abilitazione I2C

**IMPORTANTE:** Prima di installare questo addon, **devi abilitare I2C** sul tuo sistema.

#### Procedura per abilitare I2C:

1. Vai su **Supervisor → Add-on Store → Menu (⋮) → Repositories**
2. Aggiungi questo repository: `https://github.com/Poeschl/Hassio-Addons`
3. Cerca e installa **"HassOS I2C Configurator"**
4. Avvia l'addon
5. **FONDAMENTALE:** Esegui uno **spegnimento completo** (non solo riavvio):
   - Vai su **Impostazioni → Sistema → Spegni**
   - Scollega fisicamente l'alimentazione per 10 secondi
   - Ricollega e lascia riavviare
   - **Ripeti questa operazione una seconda volta** (richiesto per applicare le modifiche)
6. Verifica che I2C sia attivo collegandoti via SSH: `ls -l /dev/i2c-0`

Se vedi il device `/dev/i2c-0`, I2C è abilitato correttamente! ✅

## Installazione

1. Aggiungi questo repository in Home Assistant:
   - **Supervisor → Add-on Store → Menu (⋮) → Repositories**
   - Incolla: `https://github.com/davidelolli/homeassistant-rpi5-oled`
   - Clicca "Aggiungi"

2. Cerca **"RPi5 OLED Monitor"** nella lista degli addon

3. Clicca **"Installa"**

4. Attendi il completamento dell'installazione

5. Clicca **"Avvia"**

## Configurazione

L'addon non richiede configurazione aggiuntiva. Funziona immediatamente dopo l'avvio se I2C è stato abilitato correttamente.

## Avvio automatico

Per far partire l'addon automaticamente all'avvio di Home Assistant:
- Nella pagina dell'addon, attiva l'opzione **"Avvia all'avvio"**

## Risoluzione problemi

### Il display rimane spento

**Causa:** I2C non è abilitato o il display non è collegato correttamente.

**Soluzione:**
1. Verifica la connessione fisica del display
2. Controlla che I2C sia attivo: `ls /dev/i2c-0`
3. Scansiona il bus I2C: `i2cdetect -y 0` (dovresti vedere `2d`)

### Errore durante l'installazione

**Causa:** Problema con la build Docker.

**Soluzione:**
1. Verifica la tua connessione internet
2. Riprova l'installazione
3. Controlla i log dell'addon per dettagli specifici

### Display mostra informazioni errate

**Causa:** Script Python non aggiornato o problema di comunicazione I2C.

**Soluzione:**
1. Riavvia l'addon
2. Verifica che il display funzioni correttamente con `i2cdetect`

## Supporto

Per segnalare problemi o richiedere funzionalità, apri una issue su:
`https://github.com/davidelolli/homeassistant-rpi5-oled/issues`

## Crediti

Addon sviluppato da Davide Lolli per la community di Home Assistant.

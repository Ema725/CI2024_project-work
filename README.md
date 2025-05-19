# Algoritmo Genetico per Symbolic Regression

il notebook (`symreg.ipynb`) implementa un **algoritmo genetico** per risolvere problemi di _symbolic regression_. A partire da un dataset di esempi \(`x`, `y`\), l’obiettivo è trovare un’espressione simbolica che approssimi la relazione sottostante.

---

## 📋 Contenuti

1. **Import delle librerie**  
2. **Definizione degli operatori “sicuri”**  
   - Divisione, logaritmo, radice quadrata, reciproco  
3. **Costruzione e valutazione degli alberi sintattici**  
   - Rappresentazione con `Node` da `gxgp.node`  
   - Funzione di fitness basata su errore quadratico medio  
4. **Generazione casuale di alberi**  
   - Profondità massima parametrizzabile  
5. **Operatori genetici**  
   - Mutazioni: _point_, _subtree_, _hoist_  
   - Crossover su sottografi (swap di sottalberi)  
6. **Selezione**  
   - Torneo  
   - Elitismo  
7. **Controllo del bloat**  
   - Limitazione della lunghezza massima dell’albero (`MAX_LEN`)  
   - Riinizializzazione parziale se stagnazione (`MAX_COUNTER`)  
8. **Esecuzione dell’algoritmo**  
   - Parametri configurabili: dimensione popolazione, numero di generazioni, tasso di mutazione, ecc.  
   - Stampa a video della migliore espressione trovata e del suo fitness  

---

## 🚀 Requisiti

- Python 3.7+  
- `numpy`  
- `tqdm`  
- `icecream`  
- Pacchetto `gxgp` (contiene `gp_common` e `node`)  
- (Opzionale) `matplotlib`, se volete estendere il notebook con grafici  

Puoi installare le librerie con:

```bash
pip install numpy tqdm icecream gxgp

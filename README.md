# Primo monitoraggio sull'uso di Sempl.it in una pubblica amministrazione
Giuliana Fiorentino, Marco Russodivito


## Abstract
Il contributo presenta i risultati preliminari sull’uso di SEMPL-IT, uno strumento basato sull’Intelligenza Artificiale per la semplificazione automatica di testi amministrativi italiani, sviluppato nell’ambito del progetto PRIN VerbACxSS. La sperimentazione, articolata in tre fasi (formazione iniziale, utilizzo autonomo e valutazione finale), ha coinvolto un gruppo di dipendenti tecnico-amministrativi dell’Università degli Studi del Molise, invitati a utilizzare SEMPL-IT per quattro settimane durante le normali attività lavorative. Ciò ha permesso di analizzare l’usabilità del sistema, i benefici percepiti, le criticità emerse e le modalità di integrazione dello strumento nei processi di redazione amministrativa. I risultati evidenziano una valutazione complessivamente positiva di SEMPL-IT. Lo strumento è stato apprezzato sia come supporto iniziale alla semplificazione linguistica, sia come mezzo per migliorare la leggibilità dei testi. Tuttavia, rimane centrale il ruolo del controllo umano, soprattutto nei passaggi caratterizzati da maggiore densità tecnico-giuridica. L’analisi conferma che SEMPL-IT non è percepito come un sostituto della competenza redazionale, ma come uno strumento di supporto in grado di stimolare una maggiore consapevolezza linguistica e favorire pratiche di scrittura amministrativa più chiare, accessibili e orientate al destinatario.


## Setup
Create a virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```


## Replication Package Content
* `assets`: folder that contains the experimental corpora in `.csv` format
* `filtered`: folder that contains the filtered experimental corpora in `.xlsx` format.
* `metrics`: folder that contains the metrics extracted from filtered experimental corpora in `.csv` and `.json` format.
* `1_filter.py`: script to filter the experimental corpora.
* `2_metrics_extractor.py`: script to extract metrics from the filtered experimental corpora. It employs [italian-ats-evaluator](https://github.com/RedHitMark/italian-ats-evaluator).
* `3_1_metrics_text.ipynb`, `3_2_metrics_comparison.ipynb` and `3_3_metrics_simplification.ipynb`: jupyter notebook used to analyze the metrics extracted from the filtered experimental corpora.
* `4_1_analysis_feature.ipynb`, `4_2_analysis_text.ipynb`, `4_3_analysis_comparison.ipynb` and `4_4_analysis_simplification.ipynb`: jupyter notebook used to analyze the results.
* `focus_group`: folder that contains the files related to the focus group activity.


## Acknowledgements
This contribution is a result of the research conducted within the framework of the PRIN 2020 (Progetti di Rilevante Interesse Nazionale) "VerbACxSS: on analytic verbs, complexity, synthetic verbs, and simplification. For accessibility" (Prot. 2020BJKB9M), funded by the Italian Ministero dell'Università e della Ricerca.
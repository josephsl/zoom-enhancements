# Îmbunătățiri accesibilitate Zoom

* Authors: Mohamad Suliman, Eilana Benish

Acest supliment îmbunătățește experiența de utilizare a Zoom pentru utilizatorii NVDA prin furnizarea de comenzi rapide de la tastatură pentru Gestionarea alertelor pentru diferite evenimente În timpul unei întâlniri, faceți procesul de control de la distanță mult mai accesibil și mai ușor și multe altele.

## comenzi rapide de la tastatură pentru controlul alertelor În întâlniri 

* NVDA + Shift + A: deplasează între diferite moduri de raportare a alertelor. Sunt disponibile următoarele moduri:
	* Modul Raportare toate alertele, unde toate alertele sunt raportate ca de obicei
	* Bip pentru alerte, unde NVDA va reda un bip scurt pentru fiecare alertă afișată în Zoom
	* Opriți toate alertele, unde NVDA va ignora toate alertele
	* Modul personalizat, unde utilizatorul poate personaliza ce alerte doresc să aibă și care nu. Acest lucru se poate face folosind dialogul de setări al suplimentului sau folosind comenzile rapide de la tastatură dedicate pentru asta

Următoarele comenzi rapide pot fi folosite pentru a activa/dezactiva anunțurile fiecărui tip de alertă (rețineți că acest lucru va fi eficient atunci când este selectat modul personalizat):

* NVDA + Ctrl + 1: Participantul s-a alăturat/a părăsit întâlnirea (numai gazda)
* NVDA + Ctrl + 2: Participantul s-a alăturat/a părăsit sala de așteptare (numai gazda)
* NVDA + Ctrl + 3: Audio dezactivat de gazdă
* NVDA + Ctrl + 4: Video oprit de gazdă
* NVDA + Ctrl + 5: Partajarea ecranului a fost începută/oprită de un participant
* NVDA + Ctrl + 6: Permisiune de înregistrare acordată/revocată
* NVDA + Ctrl + 7: Chat public în cadrul întâlnirii primit
* NVDA + Ctrl + 8: Chat privat în cadrul întâlnirii primit
* NVDA + Ctrl + 9: Încărcarea fișierului în cadrul întâlnirii a fost finalizată
* NVDA + Ctrl + 0: Privilegiul gazdă acordat/Revocat
* NVDA + Shift + Ctrl + 1: Participantul a ridicat/a coborât mâna (numai gazda)
* NVDA + Shift + Ctrl + 2: Permisiune de control de la distanță acordată/revocată
* NVDA + Shift + Ctrl + 3: mesaj de chat IM primit

Rețineți că trebuie să lăsați selectat raportarea tuturor tipurilor de alerte (în setările de accesibilitate Zoom) pentru a avea funcția de supliment așa cum așteptați.

## Comandă rapidă de la tastatură pentru deschiderea dialogului add-on-ului 

NVDA + Z Deschide dialogul add-on-ului!

Folosind acest dialog puteți:

* Vedeți ce alerte sunt anunțate și care nu
* Selectați tipurile de alerte pe care doriți să fie anunțate
* Alegeți modul de raportare a alertelor
* Salvați modificările personalizate

## Control de la distanță 

după ce se acordă permisiunea de control de la distanță, NVDA + O va muta focalizarea în/În afara ecranului de control de la distanță

Rețineți că modul formular ar trebui să fie pe una dintre comenzile întâlnirii pentru a putea controla de la distanță celălalt ecran

## O notă importantă

În prezent, funcția modului de alerte personalizate în care utilizatorul poate alege ce alerte dorește să primească și care nu funcționează cu Zoom doar atunci când limba interfeței cu utilizatorul este setată la engleză.

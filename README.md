# IncrementalRecommenderSystem

## Kratak opis

Sistemi preporuka bi idelano trebalo da imaju mogućnost da se prilagodjavaju promenama. Korisničke preference mogu se često menjati zavisno od godišnjeg doba, budžeta, trenutnih trendova i mogih drugih faktora. Takođe, dodaju se novi proizvodi i dolaze novi korisnici za koje nemamo istorijske podatke. Ideja inkrementalnih modela je da se oni stalno ažuriraju tako da kada god imamo nove podatke oni budu koršćeni, bez dodatnih prolazaka kroz skup podataka.

Ovaj projekat bavi se inkrementalnim sistemima preporuka koji su zasnovani na dekompoziciji matrica, ideja se zasniva na tome da je za implementaciju sistema preporuke dovoljno posmatrati samo pozitivne fidbeke, oni nam govore da se korisniku nešto svidelo, dok negativne fidbeke i nedostatak fidbeka zanemarujemo. Pozitivnim fidbekom se smatra ocena 5 na skali od 1-5, odnosno u relaksiranom slučaju možemo pozitivnim smatrati sve ocene veće od 4, kao što je opisano u [Building an incremental recommender system](https://towardsdatascience.com/building-an-incremental-recommender-system-8836e30afaef). Dodatno implementiran je algoritam inkrementalni stohastički gradijentni spust (ISGD - Incremental Stochastic Gradient Descent) koji je opisan u radu ["Online bagging for recommendation with incremental matrix factorization"](https://ceur-ws.org/Vol-2069/STREAMEVOLV2.pdf) autora Joao Vinegare, Alipio Mario Jorge i Joao Gama gde je ISGD korišćen kao algoritam kojim je radjeno inkrementalno ažuriranje podataka matrice u slučaju posmatranja samo pozitivnih fidbeka.
![image](https://user-images.githubusercontent.com/48031805/187544028-e1cb2e7e-0454-47fb-a0ad-159d39bf5b41.png)


## Programski jezici i tehnologije

Rad je izrađen u programskom jeziku Python uz korišćenje sledećih biblioteka:
  * numpy
  * pandas
  * matplotlib
  * tqdm
  * torch
  * cf_step
 
od kojih su sve osim biblioteke cf_step dostupne u okviru instalacije Anaconde.

Biblioteka cf_step moze se instalirati na sledeci nacin:
  * pip install cf_step

Korišćeni skup podataka: [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/). Testiranje je pokušano i na većim skupovima podataka, ali zbog ograničenja same mašine na kojoj je izvršavan kod nije bilo moguće raditi sa većim skupovima podataka u trentku izrade ovog projekta. Za pregledanje je dovoljno pogledati svesku MainFinal.ipynb koja sadrži sav kod uz dodatne komentare za prezentaciju, odnosno druga verijanta može biti da se pregledanje vrši pregledanjem sveske Main.ipynb i SGD.py koji je importovan u Main svesku i korišćen u prvoj verziji odradjenoj prošle školske godine.

## Autor
  Natalija Drašković natalija.draskovic@outlook.com, @NatalijaDraskovic

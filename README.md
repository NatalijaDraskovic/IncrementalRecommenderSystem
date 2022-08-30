# IncrementalRecommenderSystem

## Kratak opis

Sistemi preporuka bi idelano trebalo da imaju mogućnost da se prilagodjavaju promenama. Korisnićke preference mogu se često menjati zavisno od godišnjeg doba, budžeta, trenutnih trendova i mogih drugih faktora. Takođe, dodaju se novi proizvodi i dolaye novi korisnici za koje nemamo istorijske podatke. Ideja inkrementalnih modela je da se oni stalno ažuriraju tako da kada god imamo nove podatke oni budu koršćeni, bez dodatnih prolazaka kroy skup podataka.

Ovaj projekat bavi se inkrementalnim sistemima preporuka koji su zasnovani na dekompoziciji matrica, odnosno na pristupu opisanom u radu “Fast incremental matrix factorization for recommendation with positive-only feedback” autora João Vinagre. Ideja se yasniva na tome da je za implementaciju sistema preporuke dovoljno posmatrati samo pozitivne fidbeke, oni nam govore da se korisniku nešto svidelo, dok negativne fidbeke i nedostatak fidbeka zanemarujemo. Poyitivnim fidbekom se smatra ocena 5 na skali od 1-5, odnosno u relaksiranom slučaju možemo pozitivnim smatrati sve ocene veće od 4.

Algoritam koji je korišćen je inkrementalni stohastićki gradijentni spust (ISGD - Incremental Stochastic Gradient Descent= koji je i prezentovan u pomenutom radu.
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

Korišćeni skup podataka: https://grouplens.org/datasets/movielens/1m/. Testiranje je pokušano i na većim skupovima podataka, ali nažalost mašina na kojoj je izvršavan kod nije mogla da podnese rad sa većim skupovima podataka.

## Autor
  Natalija Drašković natalija.draskovic@outlook.com, @NatalijaDraskovic

import pandas as pd
import numpy as np
from tqdm import tqdm

class Incremental_SGD:
    # Inicijalizacija
    def __init__(self, dataset, n_users, n_movies, k, l2_reg=0.01, learning_rate=0.05):
        self.dataset = dataset[['user_code', 'movie_code', 'rating']].copy()
        self.n_users = n_users
        self.n_movies = n_movies
        self.k = k
        self.l2_reg = l2_reg
        self.learning_rate = learning_rate
        self.known_users = np.array([])
        self.known_movies = np.array([])
        self.A = np.random.normal(0., 0.1, (n_users, self.k))
        self.B = np.random.normal(0., 0.1, (n_movies, self.k))
        self.history_m = np.zeros((n_users, n_movies))

    # Azuriramo novim podacima
    def update(self, user, movie, rating, train=False):
        # Proveravamo da li korisnik vec postoji u listi poznatih korisnika i dodajemo ga ukoliko ne postoji
        if user not in self.known_users: 
            self.known_users = np.append(self.known_users, user)
        user_v = self.A[user]
        # Proveravamo da li film vec postoji u listi poznatih filmova i dodajemo ga ukoliko ne postoji
        if movie not in self.known_movies: 
            self.known_movies = np.append(self.known_movies, movie)
        movie_v = self.B[movie]
        # Ukoliko smo u fazi treniranja padaci se vec nalaze u datasetu
        if not train:
            # Dodajemo podatak u dataset
            self.dataset.loc[len(self.dataset)] = [user, movie, rating]
        err = 1. - np.dot(user_v, movie_v)
        self.A[user] = user_v + self.learning_rate * (err * movie_v - self.l2_reg * user_v)
        self.B[movie] = movie_v + self.learning_rate * (err * user_v - self.l2_reg * movie_v)
        self.history_m[user, movie] = 1

    # Predvidjamo n najboljih preporuka
    def recommend(self, user, n):
        # Ako korisnik nije vec poznat preporucujemo mu n najbolje ocenjenih filmova
        if user not in self.known_users: 
            return self.dataset['movie_code'].value_counts().head(n)
        # Lista filmova koje treba preporuciti korisniku
        recommendations = []
        scores = np.abs(1. - np.dot(np.array([self.A[user]]), self.B.T)).reshape(self.B.shape[0])
        i = 0
        for movie in np.argsort(scores):
            # Ukoliko je korisnik vec gledao film preskacemo ga
            if self.history_m[user, movie] == 1: 
                continue
            recommendations.append(movie)
            i += 1
            # Ukoliko imamo n najboljih filmova koje korisnik nije pogledao prekidamo
            if i == n: 
                break
        return recommendations
    
    # Treniramo model na pocetnom skupu podataka
    def train(self):
        n = self.dataset.shape[0]
        for i in tqdm(range(n)):
            user, movie, rating = self.dataset.iloc[i]
            self.update(user, movie, rating, train=True)
    
    # Racunamo preporuku za datog korisnika i azuriramo podatke
    def step(self, user, movie, rating, N):
        recommendations = self.recommend(user, N)
        self.update(user, movie, rating)
        return recommendations
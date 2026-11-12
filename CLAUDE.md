# Six Heures — procédure de l'édition quotidienne

Site statique servi par Cloudflare (Workers static assets, `wrangler.jsonc` → `public/`).
Chaque push sur `main` redéploie automatiquement.

## Chaque matin (date = aujourd'hui, Europe/Paris)
1. Lire `data/history.md` (sujets déjà traités) et la dernière édition dans `public/editions/`.
2. Rechercher l'actualité des dernières 24 h (WebSearch mode extended + WebFetch des articles) :
   - **Monde** : géopolitique, guerres, diplomatie, marchés (S&P, Nasdaq, Dow, CAC 40, or, pétrole, bitcoin, taux), GAFAM / tech, crypto.
   - **France** : politique, Parlement, lois, social, économie, entreprises.
   - **Savoirs** : culture G variée (géopolitique, économie, art, histoire, sport, langue) + sciences / ingénierie / énergie / informatique / IA, de préférence reliés à l'actualité, expliqués avec chiffres et ordres de grandeur.
3. Ne pas répéter : un sujet déjà traité ne revient que s'il y a un fait nouveau, et alors avec l'angle nouveau uniquement.
4. Écrire `public/editions/AAAA-MM-JJ.json` en suivant exactement le schéma de l'édition existante
   (date, weekday, saint, headline, chapters[monde|france|savoirs] avec lede[3], articles[{kicker,title,minutes,chapo,body[],critique,sources[]}],
   board (monde uniquement, dernières clôtures), boardNote, estimate, flashcards[6-7], quiz[5]).
   - ~10 min de lecture par chapitre (≈1 600-2 000 mots), 4 à 6 articles.
   - Vision critique : un encadré `critique` sur les articles majeurs (angle mort, intérêts des acteurs, limite des chiffres).
   - Uniquement des faits sourcés ; chaque article liste ses sources (URL réelles consultées). En cas de doute, ne pas inclure.
   - Français soigné, phrases complètes, guillemets « ».
5. Ajouter l'édition en tête de `public/editions/index.json` ({date, headline}).
6. Ajouter les sujets à `data/history.md`.
7. Valider le JSON (`python3 -m json.tool`), commit `Édition du AAAA-MM-JJ`, push sur `main`.

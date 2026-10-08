# Avant la mise en ligne et la soumission

Ce fichier liste ce qui reste à faire, et ce que je ne peux pas faire à ta place.

## 1. Bloquant : à remplir par toi

- [ ] **Mentions légales** (`mentions-legales.html`) : forme juridique, capital, siège, registre du commerce, identifiant fiscal, directeur de la publication, durée de conservation. Les champs en orange sont les seuls à compléter.
- [ ] **Numéro WhatsApp** dans `config.js` (`whatsapp`), au format `2135XXXXXXXX`. Sans lui, le lien WhatsApp reste caché.
- [ ] **Service d'envoi du formulaire** dans `config.js` (`formEndpoint`), par exemple Formspree. Sans lui, le formulaire ouvre la messagerie de la personne. Pour une candidature, c'est mieux avec un envoi réel.
- [ ] **Une preuve réelle** : une agence qui utilise l'outil, un témoignage signé, ou un chiffre vérifiable (nombre d'agents, de leads traités, de mandats suivis). Le site n'en contient aucun, volontairement.

## 2. Décisions à confirmer

- [ ] **Nom du produit** : le site présente le produit comme « Relance Pro », édité par « AMI Immobilier ». C'est le nom affiché dans l'application (manifeste). Confirme, ou dis-moi le nom à utiliser.
- [ ] **Présence en Algérie** : le site dit « CRM des agences immobilières en Algérie ». Confirme que c'est bien le positionnement.
- [ ] **Tarifs** : le site dit « sur demande ». Si tu veux afficher des prix ou une offre d'essai, dis-moi lesquels.

## 3. Affirmations à vérifier (vraies d'après le code, à confirmer par toi)

- [ ] « Nous ne revendons pas vos données » et « nous ne partageons pas les données à des fins commerciales ».
- [ ] « Nous n'entraînons aucun modèle sur vos données ».
- [ ] « Des droits par rôle » : chaque membre n'ouvre que les écrans de son rôle. Les rôles existent ; l'étendue exacte reste à confirmer.
- [ ] « L'IA n'envoie pas de message à un prospect, ne signe aucun mandat et ne fixe aucun prix » (page Notre usage de l'IA).
- [ ] « L'outil s'installe sur l'écran d'accueil du téléphone » : le manifeste le permet, mais teste-le sur un vrai téléphone.
- [ ] « L'export des leads et des rappels se définit à la mise en place » : seul l'export de la comptabilité (Excel, CSV) est vérifié.
- [ ] Modules « Production vidéo » et « Synchronisation avec Google Agenda » : présents dans le code, à montrer en démonstration.

## 4. Sujets sensibles pour une candidature

- [ ] **Collecte d'annonces** : le site ne nomme ni Facebook ni Ouedkniss. Le produit collecte des annonces de particuliers sur des plateformes ; ces plateformes ont des conditions d'utilisation. À régler avant de le mettre en avant.
- [ ] **Chaîne de fournisseurs d'IA** : le site liste OpenRouter, Google (Gemini), Moonshot (Kimi) et Anthropic (Claude). C'est la réalité du code. Dans la candidature, dis-le tel quel : utiliser Claude via un intermédiaire n'est pas un problème, le cacher le serait.

## 5. Mise en ligne (chez Hostinger)

Envoie dans `public_html` uniquement ces fichiers :

`index.html`, `services.html`, `ia.html`, `faq.html`, `contact.html`, `mentions-legales.html`, `styles.css`, `menu.js`, `config.js`, `logo.png`, `robots.txt`, `sitemap.xml`

Ne mets pas `build.py` ni ce fichier sur le serveur. Remplace la page parking par `index.html`.

## 6. Après un changement de texte

Modifie `build.py`, puis lance `python build.py` dans ce dossier. Cela régénère les pages HTML, le plan du site et `robots.txt`. Ne modifie pas les pages HTML à la main : elles seraient écrasées.

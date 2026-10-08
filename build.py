# -*- coding: utf-8 -*-
"""Génère les pages du site Relance Pro (amiimmobilier.pro).

Pour modifier un texte, éditer ce fichier puis lancer :  python build.py
Les pages HTML générées ne doivent pas être éditées à la main.
"""
import json
import pathlib

SITE = "https://amiimmobilier.pro"
ICI = pathlib.Path(__file__).resolve().parent
PRODUIT = "Relance Pro"
EDITEUR = "AMI Immobilier"
MAIL = "contact@amiimmobilier.pro"


# ── Gabarits communs ───────────────────────────────────────────────────────────
NAV = [
    ("index.html", "Accueil", "accueil"),
    ("accompagnement.html", "Accompagnement", "accompagnement"),
    ("services.html", "Modules", "modules"),
    ("ia.html", "Notre usage de l'IA", "ia"),
    ("faq.html", "Questions", "faq"),
]


def donnees_structurees():
    d = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": PRODUIT,
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        "inLanguage": "fr",
        "description": ("CRM pour agences immobilières en Algérie, éprouvé chez AMI Immobilier à Alger, avec "
                        "audit des process, mise en place et formation des équipes. Assistant IA dont chaque "
                        "écriture est validée par l'agent."),
        "url": SITE,
        "publisher": {"@type": "Organization", "name": EDITEUR, "url": SITE, "email": MAIL},
    }
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"


def tete(titre, desc, chemin):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{chemin}">
<meta name="theme-color" content="#104360">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{PRODUIT}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{chemin}">
<link rel="icon" href="logo.png">
<link rel="stylesheet" href="styles.css">
{donnees_structurees()}
</head>
<body>
<a class="saut" href="#contenu">Aller au contenu</a>
"""


def entete(actif):
    liens = []
    for href, texte, cle in NAV:
        classe = ' class="actif"' if cle == actif else ""
        liens.append(f'<a href="{href}"{classe}>{texte}</a>')
    liens = "\n".join(liens)
    return f"""<header class="entete">
<div class="conteneur entete-ligne">
<a href="index.html" class="marque" aria-label="{PRODUIT}, accueil">
<img src="logo.png" alt="" width="40" height="40"><span class="marque-texte"><b>{PRODUIT}</b><small>par {EDITEUR}</small></span></a>
<nav class="nav" id="nav" aria-label="Principal">
{liens}
<a href="contact.html" class="bouton bouton-petit">Demander une démo</a>
</nav>
<button class="menu-bouton" id="menu" aria-label="Ouvrir le menu" aria-controls="nav" aria-expanded="false">Menu</button>
</div>
</header>
"""


def pied():
    return f"""<footer class="pied">
<div class="conteneur">
<div class="pied-grille">
<div>
<a href="index.html" class="marque"><img src="logo.png" alt="" width="40" height="40"><span class="marque-texte"><b>{PRODUIT}</b><small>par {EDITEUR}</small></span></a>
<p>Le CRM éprouvé dans une agence d'Alger, avec l'audit des process et la formation des équipes.</p>
</div>
<div>
<h4>Produit</h4>
<ul>
<li><a href="services.html">Modules</a></li>
<li><a href="ia.html">Notre usage de l'IA</a></li>
<li><a href="faq.html">Questions fréquentes</a></li>
<li><a href="contact.html">Demander une démonstration</a></li>
</ul>
</div>
<div>
<h4>Contact</h4>
<ul>
<li><a href="mailto:{MAIL}">{MAIL}</a></li>
<li><a href="mentions-legales.html">Mentions légales</a></li>
<li><a href="mentions-legales.html#confidentialite">Confidentialité</a></li>
</ul>
</div>
</div>
<div class="pied-bas">© 2026 {EDITEUR}. {PRODUIT} est un produit d'{EDITEUR}. Siège : Alger-Centre, Algérie.</div>
</div>
</footer>
"""


def page(titre, desc, chemin, actif, corps, scripts=""):
    return (tete(titre, desc, chemin) + entete(actif)
            + '<main id="contenu">\n' + corps + "\n</main>\n"
            + pied() + '<script src="menu.js"></script>\n' + scripts + "</body>\n</html>\n")


# ── Composants ─────────────────────────────────────────────────────────────────
def icone(chemin_svg):
    return f'<div class="icone" aria-hidden="true"><svg viewBox="0 0 24 24">{chemin_svg}</svg></div>'


ICONES = {
    "prospects": '<circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/><path d="M21 21v-2a4 4 0 0 0-3-3.87"/>',
    "rappel": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "recherche": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "agenda": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "mandat": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "compta": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h8"/>',
    "video": '<rect x="2" y="5" width="14" height="14" rx="2"/><path d="m16 10 6-3v10l-6-3"/>',
    "ia": '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v3"/>',
}


def carte(cle, titre, texte):
    return f'<article class="carte">{icone(ICONES[cle])}<h3>{titre}</h3><p>{texte}</p></article>'


def etapes(liste):
    items = []
    for i, (titre, texte) in enumerate(liste, 1):
        items.append(f'<li class="etape"><span class="num">{i:02d}</span><h3>{titre}</h3><p>{texte}</p></li>')
    return '<ol class="etapes">' + "".join(items) + "</ol>"


def mockup():
    lignes = [
        ("Samia K. · F3 à Kouba", "Rappel · assigné à Yacine", "p-rappel", "10 h 00"),
        ("Mourad B. · villa à Birkhadem", "Visite confirmée", "p-visite", "Jeudi 14 h"),
        ("Nadia L. · local à Hydra", "Nouveau lead · téléphone reçu", "p-nouveau", "Nouveau"),
        ("Karim H. · F4 à Bab Ezzouar", "Pré-mandat à faire signer", "p-rappel", "Demain"),
    ]
    rangees = "".join(
        f'<div class="ligne"><div><strong>{a}</strong><small>{b}</small></div><span class="pastille {c}">{d}</span></div>'
        for a, b, c, d in lignes)
    return f"""<div class="apercu" role="img" aria-label="Aperçu de l'interface : rappels du jour, données fictives">
<div class="apercu-barre"><i></i><i></i><i></i><span>Aperçu · données fictives</span></div>
<div class="apercu-corps">
<div class="apercu-menu"><div class="on">Prospects</div><div>Rappels</div><div>Agenda</div><div>Mandats</div><div>Comptabilité</div></div>
<div class="apercu-zone">
<div class="apercu-titre"><b>Rappels du jour</b><small>4 à traiter</small></div>
{rangees}
</div>
</div>
<div class="apercu-pied">Exemple illustratif. Aucune donnée réelle.</div>
</div>"""


# ── Pages ──────────────────────────────────────────────────────────────────────
def accueil():
    corps = f"""
<section class="heros" aria-labelledby="titre">
<div class="conteneur heros-grille">
<div>
<p class="etiquette">CRM et accompagnement pour agences immobilières en Algérie</p>
<h1 id="titre">Le CRM qui fait tourner notre agence, installé dans la vôtre.</h1>
<p class="lead">{PRODUIT} a été construit et éprouvé chez {EDITEUR}, agence immobilière à Alger. Nous l'installons dans votre agence, nous auditons vos process, et nous formons vos équipes jusqu'à ce qu'elles l'utilisent seules.</p>
<div class="boutons">
<a href="contact.html" class="bouton">Demander une démonstration</a>
<a href="#fonctionnement" class="bouton secondaire">Voir comment ça marche</a>
</div>
<p class="note-petite">Démonstration de 30 minutes. Tarifs sur demande, selon le nombre d'agents.</p>
</div>
{mockup()}
</div>
</section>

<section aria-labelledby="probleme">
<div class="conteneur">
<div class="entete-section">
<p class="etiquette">Pourquoi les dossiers se perdent</p>
<h2 id="probleme">Une agence ne manque pas de prospects. Elle perd ceux qu'elle a.</h2>
<p>Les prospects sont dans un tableur, des messages WhatsApp et des carnets. Personne ne sait plus qui a rappelé qui, ni quand.</p>
</div>
<div class="grille">
{carte("prospects", "Des prospects dispersés", "L'historique d'un prospect est réparti entre un tableur, des messages et des notes. Ici, une seule fiche par prospect, avec tous les échanges.")}
{carte("rappel", "Des rappels qui dépendent de la mémoire", "Un rappel oublié est un mandat perdu. Chaque rappel est daté, assigné à un agent et apparaît dans sa liste du jour.")}
{carte("recherche", "Une prospection faite à la main", "Les annonces de particuliers sont collectées et triées automatiquement. Les doublons, les agences et le hors-sujet sont écartés avant que l'agent n'appelle.")}
</div>
</div>
</section>

<section class="alt" aria-labelledby="preuve">
<div class="conteneur separe">
<div>
<p class="etiquette">Éprouvé sur le terrain</p>
<h2 id="preuve">Pas un logiciel de bureau d'études. L'outil de travail d'une vraie agence.</h2>
<p class="lead petit">{PRODUIT} est l'outil sur lequel {EDITEUR} travaille chaque jour à Alger. Chaque écran a été ajusté par des agents qui appellent, visitent et signent des mandats.</p>
</div>
<div>
<p class="chiffre"><b>1 100+</b><span>appels suivis dans le centre d'appels de notre agence depuis novembre 2025</span></p>
<ul class="coches">
<li>Process de prospection, de relance et de signature testés sur nos propres dossiers.</li>
<li>Statuts, rappels et files de travail réglés sur les contraintes du métier, pas sur une théorie.</li>
<li>Ce que nous installons chez vous, nous l'utilisons d'abord chez nous.</li>
</ul>
</div>
</div>
</section>

<section aria-labelledby="accompagnement-titre">
<div class="conteneur">
<div class="entete-section">
<p class="etiquette">Notre accompagnement</p>
<h2 id="accompagnement-titre">Un outil ne suffit pas. Nous installons aussi la méthode.</h2>
<p>Un CRM mal utilisé reste un tableur. Nous partons de vos process, nous les corrigeons, puis nous formons l'équipe sur l'outil.</p>
</div>
<div class="grille">
<article class="carte"><span class="num-carte">01</span><h3>Audit de vos process</h3><p>Du premier appel au mandat signé : nous observons comment votre agence traite un prospect, et nous repérons où les dossiers se perdent.</p></article>
<article class="carte"><span class="num-carte">02</span><h3>Mise en place de {PRODUIT}</h3><p>Statuts, files de travail, rôles et modules réglés sur vos process corrigés. Vos fichiers existants sont repris.</p></article>
<article class="carte"><span class="num-carte">03</span><h3>Formation des équipes</h3><p>Une formation par profil, agent, responsable, comptable, jusqu'à ce que chacun travaille seul sur l'outil.</p></article>
</div>
<div class="boutons"><a href="accompagnement.html" class="bouton secondaire">Voir l'accompagnement en détail</a></div>
</div>
</section>

<section class="alt" aria-labelledby="differences">
<div class="conteneur">
<div class="entete-section">
<p class="etiquette">Ce qui le distingue</p>
<h2 id="differences">Conçu pour le marché algérien, dès le départ.</h2>
<p>Pas un outil étranger adapté à la main. Les annonces, les langues et les pratiques de l'agence sont celles d'ici.</p>
</div>
<div class="grille deux">
<article class="carte etendue"><h3>Des annonces algériennes</h3><p>La prospection part des plateformes d'annonces algériennes et des annonces de particuliers. Chaque annonce garde son lien d'origine, pour vérifier à la source.</p></article>
<article class="carte etendue"><h3>Le tri lit l'arabe et la darija</h3><p>Une annonce écrite en arabe ou en darija est lue et jugée comme une annonce en français. Les agences et les demandes d'acheteurs sont écartées dans les deux langues.</p></article>
<article class="carte etendue"><h3>Une seule fiche par dossier</h3><p>Leads, rappels, mandats, visites, pièces comptables et vidéos partagent les mêmes fiches. Une information saisie une fois sert partout.</p></article>
<article class="carte etendue"><h3>Un assistant qui agit depuis le téléphone</h3><p>Message vocal ou écrit depuis Telegram. L'assistant propose l'action, l'agent valide, et seulement alors le CRM est mis à jour.</p></article>
</div>
</div>
</section>

<section id="fonctionnement" aria-labelledby="fonctionnement-titre">
<div class="conteneur">
<div class="entete-section">
<p class="etiquette">Comment ça marche</p>
<h2 id="fonctionnement-titre">Trois temps : le prospect arrive, l'équipe travaille, la comptabilité suit.</h2>
</div>
{etapes([
    ("Le prospect arrive", "Saisie directe, dictée à l'assistant, ou annonce de particulier triée par la prospection. Une seule fiche est créée."),
    ("L'équipe travaille", "Chaque agent ouvre sa liste du jour : rappels, appels, visites et mandats à faire signer, avec le détail du dossier."),
    ("La comptabilité suit", "Les pièces sont rattachées au mois concerné. Les exports en Excel et CSV sont prêts pour l'expert-comptable."),
])}
</div>
</section>

<section class="bande-ia-zone" aria-labelledby="ia-titre">
<div class="conteneur">
<div class="bandeau">
<div>
<p class="etiquette">Assistant IA</p>
<h2 id="ia-titre">Vous dictez. L'assistant prépare. Vous validez.</h2>
<p>Depuis Telegram, l'agent envoie un message vocal ou écrit. L'assistant propose l'action : un lead, un rendez-vous, un rappel. Rien n'est enregistré avant le geste de validation.</p>
<p class="lien-bande"><a href="ia.html">Voir comment l'IA est utilisée, modèle par modèle</a></p>
</div>
<ol class="pas">
<li><div><b>Un message depuis le téléphone</b><span>Vocal ou écrit, sans ouvrir l'ordinateur.</span></div></li>
<li><div><b>L'assistant propose</b><span>Il montre ce qu'il va enregistrer, et pose une question si une information manque.</span></div></li>
<li><div><b>Vous validez d'un geste</b><span>Il ne supprime jamais rien et ne peut pas annuler un rendez-vous, seulement le déplacer.</span></div></li>
</ol>
</div>
</div>
</section>

<section aria-labelledby="engagements">
<div class="conteneur">
<div class="entete-section">
<p class="etiquette">Nos engagements</p>
<h2 id="engagements">Ce que nous ne faisons pas.</h2>
</div>
<div class="grille">
<article class="carte"><h3>Nous n'enregistrons rien sans validation</h3><p>Aucune action proposée par l'assistant n'est écrite dans le CRM sans l'accord explicite de l'agent.</p></article>
<article class="carte"><h3>Nous ne revendons pas vos données</h3><p>Les leads, les rappels et les comptes de votre agence ne sont ni vendus ni partagés à des fins commerciales.</p></article>
<article class="carte"><h3>Nous n'entraînons aucun modèle sur vos données</h3><p>Les modèles d'IA utilisés ont leurs propres conditions, détaillées sur la page <a href="ia.html">Notre usage de l'IA</a>.</p></article>
</div>
</div>
</section>

<section class="alt" aria-labelledby="pour-qui">
<div class="conteneur separe">
<div>
<p class="etiquette">Pour qui</p>
<h2 id="pour-qui">Une agence qui travaille à plusieurs.</h2>
<p class="lead petit">{PRODUIT} sert les agences où les prospects, les visites et les mandats passent entre plusieurs personnes.</p>
</div>
<ul class="coches">
<li>Les agences à plusieurs agents, qui se partagent les prospects et les visites.</li>
<li>Les responsables qui veulent voir l'activité de chacun sans relancer tout le monde.</li>
<li>Les agences qui gèrent des mandats de vente, de location et de recherche.</li>
<li>Les agences qui produisent des vidéos de leurs biens et doivent suivre les montages.</li>
</ul>
</div>
</section>

<section class="appel-zone appel-espace">
<div class="conteneur">
<div class="appel">
<h2>Parlons du fonctionnement de votre agence.</h2>
<p>Un échange de trente minutes. Si nous pouvons vous aider, vous recevez une proposition écrite : outil, audit, formation. Sans engagement.</p>
<div class="boutons centre">
<a href="contact.html" class="bouton bouton-clair">Demander une démonstration</a>
</div>
</div>
</div>
</section>
"""
    return page(f"{PRODUIT} — CRM et accompagnement des agences immobilières en Algérie",
                "Le CRM qui fait tourner une agence d'Alger, installé dans la vôtre : audit de vos process, mise en place et formation de vos équipes. Démonstration sur demande.",
                "index.html", "accueil", corps)


def modules():
    def module(num, titre, accroche, pour, points):
        lis = "".join(f"<li>{p}</li>" for p in points)
        return f"""<article class="module">
<div class="module-tete">
<p class="etiquette">Module {num}</p>
<h2>{titre}</h2>
<p class="lead petit">{accroche}</p>
<p class="pour"><b>Pour :</b> {pour}</p>
</div>
<ul class="coches">{lis}</ul>
</article>"""
    liste = [
        module("01", "Leads et prospects",
               "Une fiche par prospect : ce qu'il cherche ou propose, son statut, et l'historique de chaque échange.",
               "les agents qui suivent des acheteurs ou des vendeurs au long cours",
               ["Statuts de suivi configurables selon votre process",
                "Historique des échanges conservé sur la fiche",
                "Recherche et filtres par agent, commune et type de bien",
                "File dédiée aux leads entrants, à traiter par l'équipe"]),
        module("02", "Rappels et centre d'appels",
               "Chaque agent voit ce qu'il doit faire aujourd'hui. Rien ne reste dans une note oubliée.",
               "les équipes qui relancent beaucoup de prospects dans la journée",
               ["Rappels datés, assignés à un agent",
                "Liste du jour et appels à passer",
                "Suivi des leads à rappeler et de ceux qui sont traités"]),
        module("03", "Prospection d'annonces",
               "Les annonces de particuliers sont collectées sur les plateformes, puis triées. L'agent ne reçoit que ce qui mérite un appel.",
               "les agences qui veulent des vendeurs directs, sans passer par les agences concurrentes",
               ["Écartement des agences, des doublons et du hors-immobilier",
                "Tri en français, en arabe et en darija",
                "Lien d'origine conservé pour chaque annonce",
                "Journal de chaque passage, consultable à tout moment"]),
        module("04", "Mandats et pré-mandats",
               "Du premier échange au mandat signé. Le suivi reste lié au prospect d'origine.",
               "les agences qui signent des mandats de vente, de location ou de recherche",
               ["Pré-mandats, avec leur détail et leur suivi",
                "Mandats de vente, de location et de recherche",
                "Biens du portefeuille et leurs calendriers de visite"]),
        module("05", "Agenda et visites",
               "Rendez-vous et visites dans un calendrier partagé, rattachés au prospect et au bien concerné.",
               "les agents et les responsables qui planifient des visites à plusieurs",
               ["Vue par agent",
                "Fiche de visite par bien",
                "Synchronisation avec Google Agenda",
                "Calendrier de visite que le client peut consulter"]),
        module("06", "Comptabilité",
               "Une vue mensuelle de l'activité, avec les pièces justificatives rattachées au mois concerné.",
               "la personne qui tient la comptabilité de l'agence, et l'expert-comptable",
               ["Vue par mois, par trimestre ou par année",
                "Pièces jointes par mois",
                "Exports en Excel et en CSV pour l'expert-comptable"]),
        module("07", "Production vidéo des biens",
               "Les agents déposent les rushes d'un bien, et le suivi du montage reste dans le même dossier.",
               "les agences qui présentent leurs biens en vidéo",
               ["Dépôt des rushes depuis le téléphone ou l'ordinateur",
                "Suivi de l'état de chaque production",
                "Montages consultables depuis le dossier du bien"]),
        module("08", "Assistant IA",
               "Un assistant qui aide l'agent à aller plus vite, sans jamais écrire à sa place.",
               "les agents qui ont peu de temps entre deux visites",
               ["Messages vocaux ou écrits envoyés depuis Telegram",
                "Création de leads, de rendez-vous et de rappels, proposée puis validée",
                "Questions de précision quand une information manque",
                "Aucune suppression, aucune annulation de rendez-vous"]),
    ]
    corps = f"""
<section class="page-tete">
<div class="conteneur">
<p class="etiquette">Modules</p>
<h1>Huit modules, une seule fiche par dossier.</h1>
<p class="lead">Chaque module répond à une étape du travail d'une agence. Une information saisie une fois sert à la prospection, au suivi, aux visites et à la comptabilité.</p>
</div>
</section>
<section class="alt">
<div class="conteneur">
{''.join(liste)}
</div>
</section>
<section class="appel-zone">
<div class="conteneur">
<div class="appel">
<h2>Voyons les modules qui comptent pour votre agence.</h2>
<p>Nous adaptons la démonstration à votre équipe : nombre d'agents, process actuel, priorités.</p>
<div class="boutons centre"><a href="contact.html" class="bouton bouton-clair">Demander une démonstration</a></div>
</div>
</div>
</section>
"""
    return page(f"Modules — {PRODUIT}",
                "Les modules de Relance Pro : leads, rappels, prospection d'annonces, mandats, agenda, production vidéo, comptabilité et assistant IA.",
                "services.html", "modules", corps)


def ia():
    lignes = [
        ("Assistant de l'agent (Telegram) : comprendre une demande et proposer une action",
         "Claude Sonnet, d'Anthropic, appelé via OpenRouter",
         "Le message de l'agent, et les informations du CRM que l'assistant consulte pour répondre",
         "Oui. Chaque écriture attend la validation de l'agent."),
        ("Transcription des messages vocaux",
         "Gemini, de Google, via OpenRouter",
         "L'enregistrement vocal envoyé par l'agent",
         "Oui. La proposition qui en découle est validée par l'agent."),
        ("Tri des annonces de prospection : particulier ou agence, immobilier ou non",
         "Gemini Flash, de Google. Kimi K2, de Moonshot, en secours.",
         "Titres et descriptions d'annonces publiées par les vendeurs",
         "Non. Les annonces écartées sont comptées et tracées."),
        ("Lecture des annonces en arabe ou en darija",
         "Gemini Flash, de Google",
         "Texte d'annonces publiques",
         "Non. La traduction sert au tri ; les données enregistrées restent celles de l'annonce d'origine."),
        ("Note indicative de l'état des photos d'un bien",
         "Modèle de vision, via OpenRouter",
         "Photos publiques de l'annonce",
         "Non. La note est indicative et affichée comme telle."),
    ]
    rangees = "".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in lignes)
    corps = f"""
<section class="page-tete">
<div class="conteneur">
<p class="etiquette">Notre usage de l'IA</p>
<h1>Quel modèle fait quoi, ce qu'il reçoit, et qui valide.</h1>
<p class="lead">{PRODUIT} utilise plusieurs modèles d'IA. Cette page les décrit un par un. Elle est mise à jour quand un modèle change.</p>
</div>
</section>
<section>
<div class="conteneur">
<div class="defile">
<table class="tableau">
<caption class="sr-seul">Les fonctions d'IA de {PRODUIT}</caption>
<thead><tr><th scope="col">Fonction</th><th scope="col">Modèle</th><th scope="col">Ce qui est envoyé</th><th scope="col">Validation humaine</th></tr></thead>
<tbody>{rangees}</tbody>
</table>
</div>
</div>
</section>
<section class="alt">
<div class="conteneur separe">
<div>
<p class="etiquette">Principes</p>
<h2>Ce que l'IA peut faire, et ce qu'elle ne fera pas.</h2>
</div>
<ul class="coches">
<li><b>Une écriture, un accord.</b> L'assistant propose ; l'agent valide. L'assistant ne supprime rien et ne peut pas annuler un rendez-vous.</li>
<li><b>Pas d'entraînement de notre côté.</b> Nous n'entraînons aucun modèle sur les données de votre agence.</li>
<li><b>Les fournisseurs gardent leurs conditions.</b> Les requêtes passent par OpenRouter, qui les transmet au fournisseur du modèle. Ces fournisseurs appliquent leurs propres conditions d'utilisation.</li>
<li><b>L'IA peut se tromper.</b> Chaque fiche proposée montre ce qu'elle va enregistrer, pour être corrigée avant validation.</li>
<li><b>Ce que l'IA ne fait pas.</b> Elle n'envoie pas de message à un prospect, elle ne signe aucun mandat et ne fixe aucun prix.</li>
</ul>
</div>
</section>
<section class="appel-zone">
<div class="conteneur">
<div class="appel">
<h2>Une question sur l'utilisation de vos données ?</h2>
<p>Écrivez-nous : nous répondons précisément, modèle par modèle.</p>
<div class="boutons centre"><a href="mailto:{MAIL}" class="bouton bouton-clair">{MAIL}</a></div>
</div>
</div>
</section>
"""
    return page(f"Notre usage de l'IA — {PRODUIT}",
                "Les modèles d'IA de Relance Pro : ce qu'ils font, ce qu'ils reçoivent, qui valide chaque action.",
                "ia.html", "ia", corps)


def accompagnement():
    def volet(num, titre, accroche, obtenu, faits):
        lis = "".join(f"<li>{f}</li>" for f in faits)
        return f"""<article class="module">
<div class="module-tete">
<p class="etiquette">Étape {num}</p>
<h2>{titre}</h2>
<p class="lead petit">{accroche}</p>
<p class="pour"><b>Vous obtenez :</b> {obtenu}</p>
</div>
<ul class="coches">{lis}</ul>
</article>"""
    volets = [
        volet("01", "Audit de vos process",
              "Avant de toucher à un outil, nous regardons comment votre agence travaille vraiment.",
              "un compte rendu des pertes repérées et le process cible, étape par étape.",
              ["Suivi d'un prospect réel, du premier appel au mandat signé",
               "Échanges avec les agents, le responsable et la personne qui tient la comptabilité",
               "Repérage des pertes : rappels oubliés, doublons, informations dispersées entre plusieurs outils"]),
        volet("02", f"Mise en place de {PRODUIT}",
              "L'outil est réglé sur votre process corrigé, pas l'inverse.",
              "un outil prêt à l'emploi, configuré pour votre agence.",
              ["Statuts de suivi, files de travail et rôles réglés sur le process cible",
               "Modules activés selon vos besoins : prospection, mandats, visites, comptabilité, vidéo",
               "Reprise de vos fichiers existants"]),
        volet("03", "Formation de vos équipes",
              "Un outil n'est utile que s'il est utilisé. Nous formons chaque profil sur les écrans qui le concernent.",
              "une équipe qui travaille seule sur l'outil.",
              ["Une session par profil : agent, responsable, comptable",
               "Exercices sur vos propres dossiers, pas sur des exemples",
               "Suivi des premières semaines pour ajuster ce qui coince"]),
    ]
    corps = f"""
<section class="page-tete">
<div class="conteneur">
<p class="etiquette">Accompagnement</p>
<h1>Nous installons l'outil, et la méthode qui va avec.</h1>
<p class="lead">Un CRM ne range pas une agence tout seul. Nous auditons vos process, nous installons {PRODUIT} sur des process corrigés, et nous formons vos équipes. C'est la méthode de notre propre agence, {EDITEUR}, à Alger.</p>
<div class="boutons"><a href="contact.html" class="bouton">Parler de votre agence</a></div>
</div>
</section>
<section class="alt">
<div class="conteneur">
{''.join(volets)}
</div>
</section>
<section aria-labelledby="pourquoi">
<div class="conteneur separe">
<div>
<p class="etiquette">Pourquoi nous</p>
<h2 id="pourquoi">Nous avons d'abord organisé notre propre agence.</h2>
<p class="lead petit">{EDITEUR} est une agence immobilière à Alger. Avant de proposer {PRODUIT} à d'autres, nous l'avons utilisé, corrigé et ajusté sur nos propres dossiers, avec nos propres agents.</p>
</div>
<ul class="coches">
<li>Nous connaissons vos contraintes : les prospects qui ne répondent pas, les annonces en arabe et en darija, les mandats à faire signer.</li>
<li>Nos recommandations viennent de ce qui a marché chez nous, pas d'un modèle générique.</li>
<li>Vous parlez à des gens du métier, qui ont tenu un centre d'appels et une comptabilité d'agence.</li>
</ul>
</div>
</section>
<section class="appel-zone">
<div class="conteneur">
<div class="appel">
<h2>Commençons par votre process actuel.</h2>
<p>Un échange de trente minutes pour comprendre votre agence. Si nous pouvons vous aider, vous recevez une proposition écrite.</p>
<div class="boutons centre"><a href="contact.html" class="bouton bouton-clair">Parler de votre agence</a></div>
</div>
</div>
</section>
"""
    return page(f"Accompagnement — {PRODUIT}",
                "Audit des process, mise en place de Relance Pro et formation des équipes : la méthode d'une agence d'Alger, appliquée à la vôtre.",
                "accompagnement.html", "accompagnement", corps)


def faq():
    questions = [
        ("À qui s'adresse Relance Pro ?",
         "Aux agences immobilières qui travaillent à plusieurs et qui veulent suivre leurs prospects, leurs rappels, leurs mandats et leur comptabilité dans un seul outil."),
        ("Qui est derrière Relance Pro ?",
         "AMI Immobilier, agence immobilière à Alger. Relance Pro est l'outil sur lequel notre agence travaille chaque jour ; nous le déployons aujourd'hui dans d'autres agences."),
        ("Que comprend l'accompagnement ?",
         "Un audit de vos process, la mise en place de Relance Pro réglé sur ces process, puis la formation de vos équipes par profil. Le détail est sur la page <a href=\"accompagnement.html\">Accompagnement</a>."),
        ("Pourquoi un outil conçu pour l'Algérie ?",
         "Parce que les annonces, les langues et les pratiques de l'agence sont algériennes : les plateformes d'annonces, l'arabe et la darija, les wilayas et les communes. Un outil générique oblige à tout adapter à la main."),
        ("Comment fonctionne l'assistant IA ?",
         "L'agent envoie un message vocal ou écrit à l'assistant, depuis Telegram. L'assistant comprend la demande et propose l'action : un lead, un rendez-vous ou un rappel. L'agent valide d'un geste, et seulement alors l'action est enregistrée."),
        ("L'IA peut-elle enregistrer ou modifier quelque chose sans mon accord ?",
         "Non. Chaque écriture proposée attend une validation explicite. L'assistant ne supprime jamais rien et ne peut pas annuler un rendez-vous, seulement le déplacer."),
        ("D'où viennent les annonces de la prospection ?",
         "Des annonces publiées par des particuliers sur les plateformes d'annonces. Chaque annonce garde son lien d'origine. Les annonces d'agences, les doublons et le hors-sujet sont écartés avant d'arriver chez l'agent."),
        ("Mes données servent-elles à entraîner une IA ?",
         "Non, de notre côté : nous n'entraînons aucun modèle sur les données de votre agence. Les modèles utilisés sont ceux de fournisseurs tiers, avec leurs propres conditions. Tout est détaillé sur la page <a href=\"ia.html\">Notre usage de l'IA</a>."),
        ("Puis-je utiliser l'outil sur mon téléphone ?",
         "Oui. L'outil fonctionne dans le navigateur et s'installe sur l'écran d'accueil du téléphone, comme une application. L'assistant IA s'utilise depuis Telegram."),
        ("Puis-je exporter mes données ?",
         "La comptabilité s'exporte en Excel et en CSV. L'export des leads et des rappels se définit lors de la mise en place, selon vos besoins."),
        ("Combien ça coûte ?",
         "Le prix dépend du nombre d'agents, des modules activés et de l'accompagnement choisi. Après l'échange, vous recevez une proposition écrite, sans engagement."),
        ("Comment se déroule la mise en place ?",
         "Une démonstration de 30 minutes sur votre fonctionnement, puis une proposition écrite, puis le réglage des statuts et des modules, et une formation par profil : agent, responsable, comptable."),
    ]
    blocs = "".join(
        f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>"
        for i, (q, a) in enumerate(questions))
    corps = f"""
<section class="page-tete">
<div class="conteneur centre">
<p class="etiquette">Questions fréquentes</p>
<h1>Les réponses avant la démonstration.</h1>
<p class="lead centre-bloc">Vous ne trouvez pas la vôtre ? <a href="contact.html">Écrivez-nous</a>.</p>
</div>
</section>
<section class="faq-zone">
<div class="conteneur">
<div class="faq">{blocs}</div>
</div>
</section>
<section class="appel-zone">
<div class="conteneur">
<div class="appel">
<h2>Une question sur votre cas ?</h2>
<p>Décrivez votre agence en quelques lignes. Nous répondons par e-mail.</p>
<div class="boutons centre"><a href="contact.html" class="bouton bouton-clair">Nous écrire</a></div>
</div>
</div>
</section>
"""
    return page(f"Questions fréquentes — {PRODUIT}",
                "Questions fréquentes sur Relance Pro : assistant IA, prospection, données, téléphone, export et mise en place.",
                "faq.html", "faq", corps)


def contact():
    corps = f"""
<section class="page-tete">
<div class="conteneur contact-grille">
<div>
<p class="etiquette">Démonstration</p>
<h1>Parlons de votre agence.</h1>
<p class="lead">Dites-nous votre agence en quelques lignes. Nous revenons vers vous pour fixer une démonstration de trente minutes.</p>
<ul class="coches petit-coches">
<li>Une démonstration sur votre process, pas sur un modèle.</li>
<li>Une proposition écrite après l'échange, sans engagement.</li>
<li>Vos données ne servent qu'à préparer cet échange.</li>
</ul>
<div class="coordonnees">
<p><b>E-mail</b><br><a href="mailto:{MAIL}">{MAIL}</a></p>
<p><b>Téléphone</b><br><a href="tel:+213773254539">+213 773 25 45 39</a></p>
<p id="whatsapp-bloc" hidden><b>WhatsApp</b><br><a id="whatsapp-lien" href="#" target="_blank" rel="noopener">Écrire sur WhatsApp</a></p>
</div>
</div>

<form id="formulaire" class="formulaire" novalidate>
<div class="duo">
<div class="champ">
<label for="nom">Nom et prénom <abbr title="obligatoire">*</abbr></label>
<input id="nom" name="nom" type="text" autocomplete="name" required>
</div>
<div class="champ">
<label for="agence">Nom de l'agence <abbr title="obligatoire">*</abbr></label>
<input id="agence" name="agence" type="text" autocomplete="organization" required>
</div>
</div>
<div class="duo">
<div class="champ">
<label for="telephone">Téléphone ou WhatsApp <abbr title="obligatoire">*</abbr></label>
<input id="telephone" name="telephone" type="tel" autocomplete="tel" required>
</div>
<div class="champ">
<label for="courriel">E-mail <span class="facultatif">(facultatif)</span></label>
<input id="courriel" name="courriel" type="email" autocomplete="email">
</div>
</div>
<div class="duo">
<div class="champ">
<label for="taille">Nombre d'agents</label>
<select id="taille" name="taille">
<option value="">Choisir</option>
<option>1 à 3</option>
<option>4 à 10</option>
<option>Plus de 10</option>
</select>
</div>
<div class="champ">
<label for="besoin">Ce qui vous occupe le plus</label>
<select id="besoin" name="besoin">
<option value="">Choisir</option>
<option>Suivi des prospects et des rappels</option>
<option>Prospection d'annonces</option>
<option>Mandats et visites</option>
<option>Comptabilité</option>
<option>Audit et organisation de l'agence</option>
<option>Formation des équipes</option>
<option>Autre</option>
</select>
</div>
</div>
<div class="champ">
<label for="message">Votre message <span class="facultatif">(facultatif)</span></label>
<textarea id="message" name="message" placeholder="Taille de l'équipe, outils utilisés aujourd'hui, ce que vous voulez améliorer en premier…"></textarea>
</div>
<button class="bouton bouton-plein" type="submit">Envoyer ma demande</button>
<p class="erreur" id="erreur" role="alert"></p>
<div class="confirmation" id="confirmation" role="status">
<b>Demande bien reçue.</b> Nous revenons vers vous pour fixer la démonstration.
</div>
<p class="note">Vos informations ne servent qu'à préparer la démonstration. Voir la <a href="mentions-legales.html#confidentialite">politique de confidentialité</a>.</p>
</form>
</div>
</section>
"""
    return page(f"Démonstration — {PRODUIT}",
                "Demandez une démonstration de Relance Pro pour votre agence immobilière. Trente minutes, sans engagement.",
                "contact.html", "contact", corps,
                scripts='<script src="config.js"></script>\n')


def mentions():
    corps = f"""
<section class="page-tete">
<div class="conteneur legal">
<p class="etiquette">Informations légales</p>
<h1>Mentions légales et confidentialité</h1>

<h2>Éditeur du site</h2>
<ul>
<li>Éditeur : {EDITEUR}</li>
<li>Forme juridique : entreprise unipersonnelle à responsabilité limitée (EURL)</li>
<li>Siège social : 7, rue Mokhtar Abdellatif, Alger-Centre, wilaya d'Alger, Algérie</li>
<li>Registre du commerce : 16/00-1243785 B 26</li>
<li>Numéro d'identification fiscale (NIF) : 00261612437854700000</li>
<li>Téléphone : <a href="tel:+213773254539">+213 773 25 45 39</a></li>
<li>Directeur de la publication : Racim Si Smail</li>
<li>Contact : <a href="mailto:{MAIL}">{MAIL}</a></li>
</ul>

<h2>Hébergement</h2>
<p>Le site est hébergé par GitHub Pages, service de GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis. Le nom de domaine est enregistré chez Hostinger.</p>

<h2>Propriété intellectuelle</h2>
<p>Les textes, logos et éléments graphiques sont la propriété d'{EDITEUR}. Toute reproduction sans autorisation écrite est interdite. {PRODUIT} est un produit d'{EDITEUR}.</p>

<h2 id="confidentialite">Politique de confidentialité</h2>
<p>Cette page explique quelles données ce site collecte, pourquoi, et comment les faire corriger ou supprimer.</p>

<h3>Données collectées</h3>
<p>Par le formulaire de démonstration : nom, nom de l'agence, téléphone ou WhatsApp, e-mail (facultatif), nombre d'agents, besoin principal et message (facultatif). Le site ne collecte rien d'autre.</p>

<h3>Finalité</h3>
<p>Répondre à votre demande et préparer une démonstration. Aucune autre utilisation, aucune revente.</p>

<h3>Cookies et mesure d'audience</h3>
<p>Le site ne dépose aucun cookie de suivi publicitaire et n'utilise aucun outil de mesure d'audience. Son hébergeur conserve des journaux techniques (dont l'adresse IP des visiteurs) pour la sécurité du service.</p>

<h3>Envoi de la demande</h3>
<p>Le formulaire ouvre votre messagerie avec le texte prérempli, adressé à {MAIL}. Rien n'est transmis tant que vous n'envoyez pas l'e-mail vous-même.</p>

<h3>Durée de conservation</h3>
<p>Les demandes sont conservées le temps de la discussion commerciale, puis supprimées sur demande, et au plus tard trois ans après le dernier échange.</p>

<h3>Vos droits</h3>
<p>Vous pouvez demander l'accès à vos données, leur correction ou leur suppression en écrivant à <a href="mailto:{MAIL}">{MAIL}</a>.</p>
</div>
</section>
"""
    return page(f"Mentions légales et confidentialité — {PRODUIT}",
                f"Mentions légales et politique de confidentialité de {PRODUIT}, édité par {EDITEUR}.",
                "mentions-legales.html", "", corps)


# ── Écriture ───────────────────────────────────────────────────────────────────
PAGES = {
    "index.html": accueil,
    "accompagnement.html": accompagnement,
    "services.html": modules,
    "ia.html": ia,
    "faq.html": faq,
    "contact.html": contact,
    "mentions-legales.html": mentions,
}

if __name__ == "__main__":
    for nom, fabrique in PAGES.items():
        (ICI / nom).write_text(fabrique(), encoding="utf-8")
        print("écrit :", nom)
    urls = list(PAGES.keys())
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f"<url><loc>{SITE}/{'' if u == 'index.html' else u}</loc></url>")
    sitemap.append("</urlset>")
    (ICI / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    (ICI / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("écrit : sitemap.xml, robots.txt")

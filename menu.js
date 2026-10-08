// Menu mobile, lien WhatsApp et formulaire de démonstration.
// Si config.js renseigne formEndpoint, la demande est envoyée à ce service.
// Sinon, la messagerie s'ouvre avec le texte prérempli.
(function () {
  var config = window.AMI_CONFIG || {};

  var bouton = document.getElementById("menu");
  var nav = document.getElementById("nav");
  if (bouton && nav) {
    bouton.addEventListener("click", function () {
      var ouvert = nav.classList.toggle("ouvert");
      bouton.setAttribute("aria-expanded", ouvert ? "true" : "false");
    });
  }

  var whatsappBloc = document.getElementById("whatsapp-bloc");
  var whatsappLien = document.getElementById("whatsapp-lien");
  if (whatsappBloc && whatsappLien && config.whatsapp) {
    whatsappLien.href = "https://wa.me/" + String(config.whatsapp).replace(/\D/g, "");
    whatsappBloc.hidden = false;
  }

  var formulaire = document.getElementById("formulaire");
  if (!formulaire) return;

  var erreur = document.getElementById("erreur");
  var confirmation = document.getElementById("confirmation");

  function valeur(nom) {
    var champ = formulaire.elements[nom];
    return champ ? String(champ.value || "").trim() : "";
  }

  function montrerErreur(texte) {
    erreur.textContent = texte;
    erreur.classList.add("visible");
  }

  formulaire.addEventListener("submit", function (e) {
    e.preventDefault();
    erreur.classList.remove("visible");
    confirmation.classList.remove("visible");

    var nom = valeur("nom");
    var agence = valeur("agence");
    var telephone = valeur("telephone");
    var courriel = valeur("courriel");

    if (!nom || !agence || !telephone) {
      montrerErreur("Renseignez le nom, l'agence et un numéro de téléphone pour que nous puissions vous répondre.");
      return;
    }
    if (courriel && !formulaire.elements.courriel.checkValidity()) {
      montrerErreur("Cette adresse e-mail semble incorrecte.");
      return;
    }

    var donnees = {
      nom: nom,
      agence: agence,
      telephone: telephone,
      courriel: courriel,
      taille: valeur("taille"),
      besoin: valeur("besoin"),
      message: valeur("message"),
      page: window.location.href
    };

    if (config.formEndpoint) {
      var bouton = formulaire.querySelector("button[type=submit]");
      bouton.disabled = true;
      fetch(config.formEndpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(donnees)
      }).then(function (reponse) {
        if (!reponse.ok) throw new Error("envoi refusé");
        formulaire.reset();
        confirmation.classList.add("visible");
      }).catch(function () {
        montrerErreur("L'envoi n'a pas abouti. Réessayez, ou écrivez directement à contact@amiimmobilier.pro.");
      }).finally(function () {
        bouton.disabled = false;
      });
      return;
    }

    var corps = [
      "Nom : " + donnees.nom,
      "Agence : " + donnees.agence,
      "Téléphone : " + donnees.telephone,
      "E-mail : " + (donnees.courriel || "non précisé"),
      "Nombre d'agents : " + (donnees.taille || "non précisé"),
      "Besoin principal : " + (donnees.besoin || "non précisé"),
      "",
      donnees.message || "(pas de message)"
    ].join("\n");
    window.location.href = "mailto:contact@amiimmobilier.pro"
      + "?subject=" + encodeURIComponent("Demande de démonstration : " + agence)
      + "&body=" + encodeURIComponent(corps);
  });
})();

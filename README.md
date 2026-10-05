# training.alexgirard.com — Formation IA agentique

Site Hugo de la formation professionnelle & continue en outils
agentiques IA (Alexandre Girard, Toulouse). Layout miroir de
[`alexgirard.com`](https://alexgirard.com) pour que le déploiement sur
le sous-domaine `training.alexgirard.com` reste trivial.

## Structure

- **Accueil** (`content/_index.md` + `layouts/index.html`) : hero,
  modules M1–M5, formulaire de contact (Formspree).
- **Catalogue** (`content/catalogue/`) : contenu détaillé des modules
  M1–M5, rendu inline sur `/catalogue/`.
- **Docs privées** : `private/` (business plan, e-mail de prospection) —
  volontairement **en dehors de l'arbre `content/`** et **jamais publié
  sur GitHub**. Ce dossier ne vit que dans le repo Gitea (privé) ; le
  repo GitHub est une copie de travail propre contenant uniquement le
  site public.

## Développement local

```sh
hugo --gc --minify --baseURL https://training.alexgirard.com/
# ou build de production (le serveur de preview sert ./public) :
python3 scripts/serve.py
```

## Déploiement — GitHub Pages

Le repo GitHub (`alx/training.alexgirard.com`, public) est construit
par `.github/workflows/hugo.yml` : Hugo 0.159, artefact `public/`,
déploiement via `actions/deploy-pages`. Le `baseURL` est injecté par
`actions/configure-pages` (URL project-page aujourd'hui ; domaine
personnel si un CNAME est rattaché plus tard) — rien n'est codé en dur.

Les docs privées (`private/`, `GAPS.md`) ne sont pas dans ce repo et ne
peuvent pas l'être par accident (l'historique git GitHub est une
première génération propre, sans ces fichiers).

## Provenance du contenu

Contenu porté tel quel depuis le repo `org` (commit `3a5fcd5`,
`projects/professional/training-formation/`). Tous les tarifs cités en
privé sont des **ESTIMES** ; aucun tarif n'est publié sur le site.

## Beads

Le travail est tracké par `bd` (beads) dans le repo `org` — bead
d'origine `org-ms31`.

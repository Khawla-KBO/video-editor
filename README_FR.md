# 🎬 Éditeur Vidéo Simple (Windows 11)
Petit éditeur vidéo développé en Python.
Permet de supprimer des intervalles spécifiques d’une vidéo MP4.

## ✅ Prérequis
- Python 3.8 ou plus récent
- FFmpeg
- moviepy (bibliothèque Python)

## 🔧 Étapes d’installation

### 1️⃣ Installer Python
1. Télécharger Python depuis :
   https://www.python.org/downloads/
2. Pendant l’installation :
   ✔ Cocher **"Add Python to PATH"**
3. Terminer l’installation.

Vérifier :
Ouvrir l’invite de commandes et taper :
python --version

### 2️⃣ Installer MoviePy
Dans l’invite de commandes :
pip install moviepy

### 3️⃣ Installer FFmpeg
1. Télécharger FFmpeg depuis :
   https://ffmpeg.org/download.html
   (Choisir version Windows)

2. Extraire le fichier ZIP (ex: `C:\ffmpeg`)

3. Ajouter FFmpeg au PATH :
   - Touche Windows
   - Rechercher **Variables d’environnement**
   - Cliquer sur **Modifier les variables d’environnement système**
   - Cliquer sur **Variables d’environnement**
   - Sélectionner **Path** → **Modifier**
   - Cliquer sur **Nouveau**
   - Ajouter :
     ```
     C:\ffmpeg\bin
     ```
   - Valider

4. Redémarrer l’invite de commandes et vérifier :
ffmpeg -version

## ▶️ Lancer l’application
Cliquer sur `video_editor.py`
OU BIEN
Ouvrir l’invite de commandes dans ce dossier et Exécuter :
python video_editor.py
L’interface graphique s’ouvrira.


## 🧭 Utilisation
1. Cliquer sur **Browse** → choisir la vidéo.
2. Cliquer sur **Add Interval**.
3. Entrer les temps au format : HH:MM:SS (Exemple : 00:01:30 → 00:02:10)
4. Cliquer sur **Save As**.
5. Cliquer sur **Process Video**.

La vidéo modifiée sera générée.




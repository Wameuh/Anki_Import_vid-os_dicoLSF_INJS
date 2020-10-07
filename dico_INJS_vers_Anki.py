import youtube_dl
import unicodedata
f = open('importanki.txt', 'w')
f.close() 
with open("liste_mots.txt", "r", encoding='utf-8') as entree:
    for mot in entree:
        mot_c = mot.strip()
        nom_fichier = unicodedata.normalize('NFD', mot_c).encode("ascii", "ignore").decode('ascii')
        nom_fichier = nom_fichier.replace("(","").replace(")","").replace(" ","_").replace("'","_")
        url_video=f"http://www.lsfdico-injsmetz.fr/video/{nom_fichier}.flv"
        with youtube_dl.YoutubeDL(\
        {
        "outtmpl": f"./media/{nom_fichier}.mp4",
        "format": "bestvideo/best",
        "postprocessors": [{"key": "FFmpegVideoConvertor",
        "preferedformat": "mp4"}],
        }) as ydl:
            try:
                ydl.download([url_video])
                print(f"vidéo {mot_c} téléchargée")
                with open("importanki.txt", "a", encoding="utf-8") as fichier_import:
                    fichier_import.write(f"{mot_c},[sound:injs_{nom_fichier}.mp4]\n")
            except youtube_dl.utils.DownloadError:
                pass

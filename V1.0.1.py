import syncedlyrics
import re

# Translation dictionary containing interface strings for all 21 requested languages
LOCALIZATION = {
    "en": {
        "title": "🎵 Synced Lyrics Finder 🎵",
        "exit_msg": "Goodbye! 👋",
        "song_prompt": "Enter the song name (or type 'exit' to quit): ",
        "artist_prompt": "Enter the artist name (optional): ",
        "searching": "Searching for lyrics for: '{}'...",
        "no_timestamps": "\n⚠️ Lyrics were found, but they do NOT have timestamps.",
        "plain_lyrics_prompt": "Would you still like to see and save the plain lyrics? (y/n): ",
        "restarting": "\nRestarting...",
        "found_header": "\n--- Lyrics Found! ---\n",
        "save_prompt": "Do you want to save these lyrics to a text file? (y/n): ",
        "saved_success": "✅ Lyrics successfully saved to {}",
        "not_found": "\n❌ Sorry, lyrics couldn't be found for this track.",
        "error_msg": "\nAn error occurred: {}",
        "loop_restart": "\n--- Restarting Search ---"
    },
    "pl": {
        "title": "🎵 Wyszukiwarka Zsynchronizowanych Tekstów 🎵",
        "exit_msg": "Do widzenia! 👋",
        "song_prompt": "Wpisz tytuł piosenki (lub wpisz 'exit', aby wyjść): ",
        "artist_prompt": "Wpisz wykonawcę (opcjonalnie): ",
        "searching": "Szukanie tekstu dla: '{}'...",
        "no_timestamps": "\n⚠️ Znaleziono tekst, ale NIE ma on znaczników czasu.",
        "plain_lyrics_prompt": "Czy nadal chcesz zobaczyć i zapisać czysty tekst? (t/n): ",
        "restarting": "\nRestartowanie...",
        "found_header": "\n--- Znaleziono Tekst! ---\n",
        "save_prompt": "Czy chcesz zapisać ten tekst do pliku tekstowego? (t/n): ",
        "saved_success": "✅ Tekst został pomyślnie zapisany w {}",
        "not_found": "\n❌ Niestety, nie znaleziono tekstu dla tego utworu.",
        "error_msg": "\nWystąpił błąd: {}",
        "loop_restart": "\n--- Restartowanie Wyszukiwania ---"
    },
    "zh": {
        "title": "🎵 同步歌词搜寻器 🎵",
        "exit_msg": "再见! 👋",
        "song_prompt": "输入歌曲名称（或输入 'exit' 退出）: ",
        "artist_prompt": "输入歌手名称（可选）: ",
        "searching": "正在搜寻歌词: '{}'...",
        "no_timestamps": "\n⚠️ 找到了歌词，但它们没有时间戳。",
        "plain_lyrics_prompt": "您仍然想查看并保存纯文本歌词吗？(y/n): ",
        "restarting": "\n正在重新开始...",
        "found_header": "\n--- 找到歌词！ ---\n",
        "save_prompt": "您想将这些歌词保存到文本文件中吗？(y/n): ",
        "saved_success": "✅ 歌词成功保存至 {}",
        "not_found": "\n❌ 抱歉，找不到这首歌曲的歌词。",
        "error_msg": "\n发生错误: {}",
        "loop_restart": "\n--- 重新开始搜寻 ---"
    },
    "hi": {
        "title": "🎵 सिंक किए गए लिरिक्स खोजक 🎵",
        "exit_msg": "अलविदा! 👋",
        "song_prompt": "गाने का नाम दर्ज करें (या बाहर निकलने के लिए 'exit' टाइप करें): ",
        "artist_prompt": "कलाकार का नाम दर्ज करें (वैकल्पिक): ",
        "searching": "'{}' के लिए लिरिक्स खोजे जा रहे हैं...",
        "no_timestamps": "\n⚠️ लिरिक्स मिल गए, लेकिन उनमें टाइमस्टैम्प नहीं हैं।",
        "plain_lyrics_prompt": "क्या आप अभी भी प्लेन लिरिक्स देखना और सहेजना चाहेंगे? (y/n): ",
        "restarting": "\nपुनः प्रारंभ हो रहा है...",
        "found_header": "\n--- लिरिक्स मिल गए! ---\n",
        "save_prompt": "क्या आप इन लिरिक्स को TEXT फ़ाइल में सहेजना चाहते हैं? (y/n): ",
        "saved_success": "✅ लिरिक्स सफलतापूर्वक {} में सहेजे गए",
        "not_found": "\n❌ क्षमा करें, इस ट्रैक के लिरिक्स नहीं मिल सके।",
        "error_msg": "\nएक त्रुटि हुई: {}",
        "loop_restart": "\n--- खोज पुनः प्रारंभ हो रही है ---"
    },
    "es": {
        "title": "🎵 Buscador de Letras Sincronizadas 🎵",
        "exit_msg": "¡Adiós! 👋",
        "song_prompt": "Introduce el nombre de la canción (o escribe 'exit' para salir): ",
        "artist_prompt": "Introduce el nombre del artista (opcional): ",
        "searching": "Buscando letra para: '{}'...",
        "no_timestamps": "\n⚠️ Se encontraron letras, pero NO tienen marcas de tiempo.",
        "plain_lyrics_prompt": "¿Aún así deseas ver y guardar la letra simple? (s/n): ",
        "restarting": "\nReiniciando...",
        "found_header": "\n--- ¡Letra Encontrada! ---\n",
        "save_prompt": "¿Quieres guardar esta letra en un archivo de texto? (s/n): ",
        "saved_success": "✅ Letra guardada con éxito en {}",
        "not_found": "\n❌ Lo sentimos, no se pudo encontrar la letra de esta pista.",
        "error_msg": "\nOcurrió un error: {}",
        "loop_restart": "\n--- Reiniciando Búsqueda ---"
    },
    "pt": {
        "title": "🎵 Buscador de Letras Sincronizadas 🎵",
        "exit_msg": "Adeus! 👋",
        "song_prompt": "Digite o nome da música (ou digite 'exit' para sair): ",
        "artist_prompt": "Digite o nome do artista (opcional): ",
        "searching": "Buscando letra para: '{}'...",
        "no_timestamps": "\n⚠️ As letras foram encontradas, mas NÃO possuem marcação de tempo.",
        "plain_lyrics_prompt": "Você ainda gostaria de ver e salvar a letra sem marcação? (s/n): ",
        "restarting": "\nReiniciando...",
        "found_header": "\n--- Letra Encontrada! ---\n",
        "save_prompt": "Deseja salvar esta letra em um arquivo de texto? (s/n): ",
        "saved_success": "✅ Letra salva com sucesso em {}",
        "not_found": "\n❌ Desculpe, a letra não foi encontrada para esta faixa.",
        "error_msg": "\nOcorreu um erro: {}",
        "loop_restart": "\n--- Reiniciando Busca ---"
    },
    "fr": {
        "title": "🎵 Recherche de Paroles Synchronisées 🎵",
        "exit_msg": "Au revoir ! 👋",
        "song_prompt": "Entrez le nom de la chanson (ou tapez 'exit' pour quitter) : ",
        "artist_prompt": "Entrez le nom de l'artiste (optionnel) : ",
        "searching": "Recherche des paroles pour : '{}'...",
        "no_timestamps": "\n⚠️ Des paroles ont été trouvées, mais elles n'ont PAS de horodatage.",
        "plain_lyrics_prompt": "Souhaitez-vous quand même voir et enregistrer les paroles simples ? (o/n) : ",
        "restarting": "\nRedémarrage...",
        "found_header": "\n--- Paroles Trouvées ! ---\n",
        "save_prompt": "Voulez-vous enregistrer ces paroles dans un fichier texte ? (o/n) : ",
        "saved_success": "✅ Paroles enregistrées avec succès dans {}",
        "not_found": "\n❌ Désolé, les paroles n'ont pas pu être trouvées pour ce titre.",
        "error_msg": "\nUne erreur est survenue : {}",
        "loop_restart": "\n--- Redémarrage de la Recherche ---"
    },
    "de": {
        "title": "🎵 Synchronisierter Songtext-Finder 🎵",
        "exit_msg": "Auf Wiedersehen! 👋",
        "song_prompt": "Songnamen eingeben (oder 'exit' zum Beenden): ",
        "artist_prompt": "Künstlernamen eingeben (optional): ",
        "searching": "Suche nach Songtext für: '{}'...",
        "no_timestamps": "\n⚠️ Songtext wurde gefunden, hat aber KEINE Zeitstempel.",
        "plain_lyrics_prompt": "Möchten Sie den einfachen Text trotzdem sehen und speichern? (j/n): ",
        "restarting": "\nNeustart...",
        "found_header": "\n--- Songtext Gefunden! ---\n",
        "save_prompt": "Möchten Sie diesen Songtext in einer Textdatei speichern? (j/n): ",
        "saved_success": "✅ Songtext erfolgreich in {} gespeichert",
        "not_found": "\n❌ Leider konnte kein Songtext für diesen Titel gefunden werden.",
        "error_msg": "\nEin Fehler ist aufgetreten: {}",
        "loop_restart": "\n--- Suche wird neu gestartet ---"
    },
    "uk": {
        "title": "🎵 Пошук Синхронізованих Текстів Пісень 🎵",
        "exit_msg": "До побачення! 👋",
        "song_prompt": "Введіть назву пісні (або 'exit' для виходу): ",
        "artist_prompt": "Введіть ім'я виконавця (опціонально): ",
        "searching": "Пошук тексту для: '{}'...",
        "no_timestamps": "\n⚠️ Текст знайдено, але він НЕ має часових міток.",
        "plain_lyrics_prompt": "Бажаєте переглянути та зберегти простий текст пісні? (y/n): ",
        "restarting": "\nПерезапуск...",
        "found_header": "\n--- Текст Знайдено! ---\n",
        "save_prompt": "Бажаєте зберегти цей текст у текстовий файл? (y/n): ",
        "saved_success": "✅ Текст пісні успешно збережено в {}",
        "not_found": "\n❌ Вибачте, текст для цього треку не знайдено.",
        "error_msg": "\nСталася помилка: {}",
        "loop_restart": "\n--- Перезапуск Пошуку ---"
    },
    "it": {
        "title": "🎵 Cercatore di Testi Sincronizzati 🎵",
        "exit_msg": "Arrivederci! 👋",
        "song_prompt": "Inserisci il nome della canzone (o digita 'exit' per uscire): ",
        "artist_prompt": "Inserisci il nome dell'artista (opzionale): ",
        "searching": "Ricerca del testo per: '{}'...",
        "no_timestamps": "\n⚠️ Il testo è stato trovato, ma NON ha marcature temporali.",
        "plain_lyrics_prompt": "Vuoi comunque visualizzare e salvare il testo semplice? (s/n): ",
        "restarting": "\nRiavvio...",
        "found_header": "\n--- Testo Trovato! ---\n",
        "save_prompt": "Vuoi salvare questo testo in un file .txt? (s/n): ",
        "saved_success": "✅ Testo salvato con successo in {}",
        "not_found": "\n❌ Spiacenti, non è stato possibile trovare il testo per questo brano.",
        "error_msg": "\nSi è verificato un errore: {}",
        "loop_restart": "\n--- Riavvio della Ricerca ---"
    },
    "ko": {
        "title": "🎵 동기화된 가사 찾기 🎵",
        "exit_msg": "안녕히 가세요! 👋",
        "song_prompt": "노래 제목을 입력하세요 (종료하려면 'exit' 입력): ",
        "artist_prompt": "아티스트 이름을 입력하세요 (선택 사항): ",
        "searching": "'{}'의 가사를 검색하는 중...",
        "no_timestamps": "\n⚠️ 가사를 찾았으나 타임스탬프가 없습니다.",
        "plain_lyrics_prompt": "일반 가사를 확인하고 저장하시겠습니까? (y/n): ",
        "restarting": "\n재시작하는 중...",
        "found_header": "\n--- 가사를 찾았습니다! ---\n",
        "save_prompt": "이 가사를 텍스트 파일로 저장하시겠습니까? (y/n): ",
        "saved_success": "✅ 가사가 {}에 성공적으로 저장되었습니다.",
        "not_found": "\n❌ 죄송합니다, 이 곡의 가사를 찾을 수 없습니다.",
        "error_msg": "\n오류가 발생했습니다: {}",
        "loop_restart": "\n--- 검색 재시작 ---"
    },
    "ja": {
        "title": "🎵 同期歌詞ファインダー 🎵",
        "exit_msg": "さようなら！ 👋",
        "song_prompt": "曲名を入力してください（終了するには 'exit' と入力）: ",
        "artist_prompt": "アーティスト名を入力してください（任意）: ",
        "searching": "「{}」の歌詞を検索中...",
        "no_timestamps": "\n⚠️ 歌詞は見つかりましたが、タイムスタンプがありません。",
        "plain_lyrics_prompt": "通常の歌詞を表示して保存しますか？ (y/n): ",
        "restarting": "\n再起動中...",
        "found_header": "\n--- 歌詞が見つかりました！ ---\n",
        "save_prompt": "この歌詞をテキストファイルに保存しますか？ (y/n): ",
        "saved_success": "✅ 歌詞が {} に正常に保存されました",
        "not_found": "\n❌ 残念ながら、この曲の歌詞は見つかりませんでした。",
        "error_msg": "\nエラーが発生しました: {}",
        "loop_restart": "\n--- 検索を再起動しています ---"
    },
    "ro": {
        "title": "🎵 Căutător de Versuri Sincronizate 🎵",
        "exit_msg": "La revedere! 👋",
        "song_prompt": "Introduceți numele melodiei (sau tastați 'exit' pentru a ieși): ",
        "artist_prompt": "Introduceți numele artistului (opțional): ",
        "searching": "Se caută versuri pentru: '{}'...",
        "no_timestamps": "\n⚠️ Versurile au fost găsite, dar NU au marcaje de timp.",
        "plain_lyrics_prompt": "Doriți totuși să vedeți și să salvați versurile simple? (y/n): ",
        "restarting": "\nSe repornește...",
        "found_header": "\n--- Versuri Găsite! ---\n",
        "save_prompt": "Doriți să salvați aceste versuri într-un fișier text? (y/n): ",
        "saved_success": "✅ Versuri salvate cu succes în {}",
        "not_found": "\n❌ Ne pare rău, versurile nu au putut fi găsite pentru această piesă.",
        "error_msg": "\nA apărut o eroare: {}",
        "loop_restart": "\n--- Se repornește căutarea ---"
    },
    "nl": {
        "title": "🎵 Gesynchroniseerde Songtekst Zoeker 🎵",
        "exit_msg": "Tot ziens! 👋",
        "song_prompt": "Voer de naam van het nummer in (of typ 'exit' om af te sluiten): ",
        "artist_prompt": "Voer de naam van de artiest in (optioneel): ",
        "searching": "Zoeken naar songtekst voor: '{}'...",
        "no_timestamps": "\n⚠️ Songtekst gevonden, maar deze heeft GEEN tijdstempels.",
        "plain_lyrics_prompt": "Wilt u de gewone songtekst nog steeds bekijken en opslaan? (j/n): ",
        "restarting": "\nOpnieuw opstarten...",
        "found_header": "\n--- Songtekst Gevonden! ---\n",
        "save_prompt": "Wilt u deze songtekst opslaan in een tekstbestand? (j/n): ",
        "saved_success": "✅ Songtekst succesvol opgeslagen in {}",
        "not_found": "\n❌ Helaas, er is geen songtekst gevonden voor dit nummer.",
        "error_msg": "\nEr is een fout opgetreden: {}",
        "loop_restart": "\n--- Zoekopdracht herstarten ---"
    },
    "sv": {
        "title": "🎵 Synkroniserad Textsökare 🎵",
        "exit_msg": "Hejdå! 👋",
        "song_prompt": "Ange låtens namn (eller skriv 'exit' för att avsluta): ",
        "artist_prompt": "Ange artistens namn (valfritt): ",
        "searching": "Söker efter låttext för: '{}'...",
        "no_timestamps": "\n⚠️ Låttexten hittades, men den saknar tidsstämplar.",
        "plain_lyrics_prompt": "Vill du ändå se och spara den vanliga texten? (j/n): ",
        "restarting": "\nStartar om...",
        "found_header": "\n--- Låttext Hittad! ---\n",
        "save_prompt": "Vill du spara denna låttext i en textfil? (j/n): ",
        "saved_success": "✅ Låttexten har sparats i {}",
        "not_found": "\n❌ Tyvärr gick det inte att hitta någon låttext för det här spåret.",
        "error_msg": "\nEtt fel uppstod: {}",
        "loop_restart": "\n--- Startar om sökningen ---"
    },
    "da": {
        "title": "🎵 Synkroniseret Sangtekst Finder 🎵",
        "exit_msg": "Farvel! 👋",
        "song_prompt": "Indtast sangens navn (eller skriv 'exit' for at afslutte): ",
        "artist_prompt": "Indtast kunstnerens navn (valgfrit): ",
        "searching": "Søger efter sangtekst til: '{}'...",
        "no_timestamps": "\n⚠️ Sangteksten blev fundet, men den har IKKE tidsstempler.",
        "plain_lyrics_prompt": "Vil du stadig se og gemme den almindelige tekst? (j/n): ",
        "restarting": "\nGenstarter...",
        "found_header": "\n--- Sangtekst Fundet! ---\n",
        "save_prompt": "Vil du gemme denne sangtekst i en tekstfil? (j/n): ",
        "saved_success": "✅ Sangtekst gemt i {}",
        "not_found": "\n❌ Beklager, sangteksten kunne ikke findes for dette nummer.",
        "error_msg": "\nDer opstod en fejl: {}",
        "loop_restart": "\n--- Genstarter søgning ---"
    },
    "no": {
        "title": "🎵 Synkronisert Sangtekstsøker 🎵",
        "exit_msg": "Ha det bra! 👋",
        "song_prompt": "Skriv inn sangnavn (eller skriv 'exit' for å avslutte): ",
        "artist_prompt": "Skriv inn artistnavn (valgfritt): ",
        "searching": "Søker etter sangtekst for: '{}'...",
        "no_timestamps": "\n⚠️ Sangteksten ble funnet, men den har IKKE tidsstempler.",
        "plain_lyrics_prompt": "Vil du likevel se og lagre den vanlige teksten? (j/n): ",
        "restarting": "\nStarter på nytt...",
        "found_header": "\n--- Sangtekst Funnet! ---\n",
        "save_prompt": "Vil du lagre denne sangteksten i en tekstfil? (j/n): ",
        "saved_success": "✅ Sangtekst lagret i {}",
        "not_found": "\n❌ Beklager, fant ikke sangteksten for dette sporet.",
        "error_msg": "\nDet oppstod en feil: {}",
        "loop_restart": "\n--- Starter søk på nytt ---"
    },
    "is": {
        "title": "🎵 Samstillt Textaleit 🎵",
        "exit_msg": "Bless! 👋",
        "song_prompt": "Sláðu inn nafn Missing (eða skrifaðu 'exit' til að hætta): ",
        "artist_prompt": "Sláðu inn nafn flytjanda (valfrjálst): ",
        "searching": "Leitar að texta fyrir: '{}'...",
        "no_timestamps": "\n⚠️ Texti fannst, en hann hefur EKKI tímamerki.",
        "plain_lyrics_prompt": "Viltu samt sjá og vista venjulega textann? (j/n): ",
        "restarting": "\nEndurræsir...",
        "found_header": "\n--- Texti fannst! ---\n",
        "save_prompt": "Viltu vista þennan texta í textaskrá? (j/n): ",
        "saved_success": "✅ Texti vistaður í {}",
        "not_found": "\n❌ Því miður fannst enginn texti fyrir þetta lag.",
        "error_msg": "\nVilla kom upp: {}",
        "loop_restart": "\n--- Leit endurræst ---"
    },
    "bg": {
        "title": "🎵 Търсач на Синхронизирани Текстове 🎵",
        "exit_msg": "Довиждане! 👋",
        "song_prompt": "Въведете име на песента (или напишете 'exit' за изход): ",
        "artist_prompt": "Въведете име на изпълнителя (по избор): ",
        "searching": "Търсене на текст за: '{}'...",
        "no_timestamps": "\n⚠️ Текстът беше намерен, но няма времеви маркери.",
        "plain_lyrics_prompt": "Искате ли все пак да видите и запазите обикновения текст? (y/n): ",
        "restarting": "\nРестартиране...",
        "found_header": "\n--- Текстът е Намерен! ---\n",
        "save_prompt": "Искате ли да запазите този текст в текстов файл? (y/n): ",
        "saved_success": "✅ Текстът е успешно запазен в {}",
        "not_found": "\n❌ За съжаление, текстът за тази песен не беше намерен.",
        "error_msg": "\nВъзникна грешка: {}",
        "loop_restart": "\n--- Рестартиране на търсенето ---"
    },
    "el": {
        "title": "🎵 Αναζήτηση Συγχρονισμένων Στίχων 🎵",
        "exit_msg": "Αντίο! 👋",
        "song_prompt": "Εισαγάγετε το όνομα του τραγουδιού (ή πληκτρολογήστε 'exit' για έξοδο): ",
        "artist_prompt": "Εισαγάγετε το όνομα του καλλιτέχνη (προαιρετικό): ",
        "searching": "Αναζήτηση στίχων για: '{}'...",
        "no_timestamps": "\n⚠️ Βρέθηκαν στίχοι, αλλά ΔΕΝ έχουν χρονική σήμανση.",
        "plain_lyrics_prompt": "Θέλετε παρόλα αυτά να δείτε και να αποθηκεύσετε τους απλούς στίχους; (y/n): ",
        "restarting": "\nΕπανεκκίνηση...",
        "found_header": "\n--- Οι Στίχοι Βρέθηκαν! ---\n",
        "save_prompt": "Θέλετε να αποθηκεύσετε αυτούς τους στίχους σε αρχείο κειμένου; (y/n): ",
        "saved_success": "✅ Οι στίχοι αποθηκεύτηκαν με επιτυχία στο {}",
        "not_found": "\n❌ Λυπούμαστε, δεν βρέθηκαν στίχοι για αυτό το κομμάτι.",
        "error_msg": "\nΠροέκυψε σφάλμα: {}",
        "loop_restart": "\n--- Επανεκκίνηση Αναζήτησης ---"
    },
    "tr": {
        "title": "🎵 Senkronize Şarkı Sözü Bulucu 🎵",
        "exit_msg": "Hoşça kal! 👋",
        "song_prompt": "Şarkı adını girin (veya çıkmak için 'exit' yazın): ",
        "artist_prompt": "Sanatçı adını girin (isteğe bağlı): ",
        "searching": "'{}' için şarkı sözü aranıyor...",
        "no_timestamps": "\n⚠️ Şarkı sözleri bulundu ancak zaman damgası İÇERMİYOR.",
        "plain_lyrics_prompt": "Düz şarkı sözlerini yine de görmek ve kaydetmek ister misiniz? (e/h): ",
        "restarting": "\nYeniden başlatılıyor...",
        "found_header": "\n--- Şarkı Sözleri Bulundu! ---\n",
        "save_prompt": "Bu şarkı sözlerini bir metin dosyasına kaydetmek ister misiniz? (e/h): ",
        "saved_success": "✅ Şarkı sözleri başarıyla {} dosyasına kaydedildi",
        "not_found": "\n❌ Üzgünüz, bu parça için şarkı sözü bulunamadı.",
        "error_msg": "\nBir hata oluştu: {}",
        "loop_restart": "\n--- Arama Yeniden Başlatılıyor ---"
    }
}

def choose_interface_language():
    # Fully expanded multilingual boot menu header and options string
    print("\nLanguage / Język / 语言 / भाषा / Idioma / Langue / Sprache / Мова / Lingua / 언어 / 言語 / Limbă / Taal / Språk / Sprog / Tungumál / Език / Γλώσσα / Dil")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("en - English")
    print("pl - Polish (Polski)")
    print("zh - Mandarin Chinese (中文)")
    print("hi - Hindi (हिन्दी)")
    print("es - Spanish (Español)")
    print("pt - Portuguese (Português)")
    print("fr - French (Français)")
    print("de - German (Deutsch)")
    print("uk - Ukrainian (Українська)")
    print("it - Italian (Italiano)")
    print("ko - Korean (한국어)")
    print("ja - Japanese (日本語)")
    print("ro - Romanian (Română)")
    print("nl - Dutch (Nederlands)")
    print("sv - Swedish (Svenska)")
    print("da - Danish (Dansk)")
    print("no - Norwegian (Norsk)")
    print("is - Icelandic (Íslenska)")
    print("bg - Bulgarian (Български)")
    print("el - Greek (Ελληνικά)")
    print("tr - Turkish (Türkçe)")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    prompt_string = (
        "Choice / Wybór / 选择 / विकल्प / Opción / Opção / Choix / Auswahl / Вибір / Scelta / 선택 / 選択 / Opțiune / Keuze / Val / Valg / Val / Val / Избор / Επιλογή / Seçim\n"
        "(default: en): "
    )
    
    while True:
        choice = input(prompt_string).strip().lower()
        if choice == "":
            return "en"
        if choice in LOCALIZATION:
            return choice
        print("Invalid choice, defaulting to English.")
        return "en"

def get_synced_lyrics():
    ui_lang = choose_interface_language()
    txt = LOCALIZATION[ui_lang]
    
    while True:
        print(f"\n{txt['title']}")
        
        song_name = input(txt['song_prompt']).strip()
        if song_name.lower() == 'exit':
            print(txt['exit_msg'])
            break
            
        artist_name = input(txt['artist_prompt']).strip()
        search_query = f"{song_name} {artist_name}".strip()
        
        print(txt['searching'].format(search_query))
        
        try:
            lrc_lyrics = syncedlyrics.search(search_query, providers=["Lrclib", "Musixmatch"])
            if not lrc_lyrics:
                lrc_lyrics = syncedlyrics.search(search_query)
            
            if lrc_lyrics:
                formatted_lines = []
                has_timestamps = False
                
                for line in lrc_lyrics.split('\n'):
                    if re.search(r"[\u4e00-\u9fff]", line):
                        if any(k in line for k in ["作词", "作曲", "贡献者", "编曲"]):
                            continue
                    
                    if any(k in line.lower() for k in ["contributor", "lyrics by", "composed by"]):
                        continue
                        
                    if re.search(r"\[\d{1,2}:\d{2}\.\d+\]", line):
                        has_timestamps = True
                        clean_line = re.sub(r"\[0?(\d+):(\d{2})\.\d+\]", r"[\1:\2]", line)
                        formatted_lines.append(clean_line)
                    else:
                        if not re.search(r"\[[a-zA-Z]+:.*\]", line) and line.strip():
                            formatted_lines.append(line)
                
                if has_timestamps:
                    final_lyrics = "\n".join([line for line in formatted_lines if line.startswith("[")])
                else:
                    print(txt['no_timestamps'])
                    choice = input(txt['plain_lyrics_prompt']).lower()
                    if choice not in ['y', 't', 's', 'o', 'j', 'j', 'e']:
                        print(txt['restarting'])
                        continue
                    final_lyrics = "\n".join(formatted_lines)

                print(txt['found_header'])
                print(final_lyrics)
                print("\n---------------------\n")
                
                save = input(txt['save_prompt']).lower()
                if save in ['y', 't', 's', 'o', 'j', 'j', 'e']:
                    safe_name = song_name.replace(' ', '_').replace('/', '_')
                    filename = f"{safe_name}_lyrics.txt"
                    
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(final_lyrics)
                    print(txt['saved_success'].format(filename))
            else:
                print(txt['not_found'])
                
        except Exception as e:
            print(txt['error_msg'].format(e))
            
        print(txt['loop_restart'])

if __name__ == "__main__":
    get_synced_lyrics()

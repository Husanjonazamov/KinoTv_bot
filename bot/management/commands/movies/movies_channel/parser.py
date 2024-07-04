def parse_movie_details(text):
    # Text formatini to'g'ri parselash
    # Masalan: "Title: Kino nomi - Genre: Janri - Year: Yili - Language: Tili - Country: Davlati - Quality: Sifat - FileID: file_id - Code: kodi"
    parts = text.split(' - ')
    title = parts[0].split(': ')[1]
    genre = parts[1].split(': ')[1]
    year = parts[2].split(': ')[1]
    language = parts[3].split(': ')[1]
    country = parts[4].split(': ')[1]
    quality = parts[5].split(': ')[1]
    file_id = parts[6].split(': ')[1]
    code = parts[7].split(': ')[1]
    return title, genre, year, language, country, quality, file_id, code

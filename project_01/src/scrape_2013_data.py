import xml.etree.ElementTree as ET

''' Parse wikipedia for movies '''
def parse_2013_wikipedia_movies(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    body = tree.find('body')
    content_div = body.findall('div')[2]
    body_content_div = content_div.findall('div')[2]
    mw_content_div = body_content_div.findall('div')[3]
    wikitable = mw_content_div.find('table')

    best_movie_row = wikitable.findall('tr')[2]
    best_movie_drama_col = best_movie_row.findall('td')[0]
    best_movies_drama = best_movie_drama_col.findall('.//a')

    best_movies_drama_list = []
    for itm in best_movies_drama:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        movie_name = val_split[0].strip()
        best_movies_drama_list.append(movie_name)

    best_movie_mus_or_com_col = best_movie_row.findall('td')[1]
    best_movies_mus_or_com = best_movie_mus_or_com_col.findall('.//a')

    best_movies_mus_or_com_list = []
    for itm in best_movies_mus_or_com:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        movie_name = val_split[0].strip()
        best_movies_mus_or_com_list.append(movie_name)

    best_actor_row = wikitable.findall('tr')[5]
    best_actor_drama_col = best_actor_row.findall('td')[0]
    best_actor_drama = best_actor_drama_col.findall('.//li')

    best_actor_drama_list = []
    for idx in range(0,len(best_actor_drama)):
        if idx is 0:
            val = best_actor_drama[idx].find('b').find('a')
        else:
            val = best_actor_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_drama_list.append(actor_name)

    best_actress_drama_col = best_actor_row.findall('td')[1]
    best_actress_drama = best_actress_drama_col.findall('.//li')

    best_actress_drama_list = []
    for idx in range(0,len(best_actress_drama)):
        if idx is 0:
            val = best_actress_drama[idx].find('b').find('a')
        else:
            val = best_actress_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_drama_list.append(actress_name)

    best_actor_com_mus_row = wikitable.findall('tr')[8]
    best_actor_com_mus__col = best_actor_com_mus_row.findall('td')[0]
    best_actor_com_mus = best_actor_com_mus__col.findall('.//li')

    best_actor_com_mus_list = []
    for idx in range(0,len(best_actor_com_mus)):
        if idx is 0:
            val = best_actor_com_mus[idx].find('b').find('a')
        else:
            val = best_actor_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_com_mus_list.append(actor_name)

    best_actress_com_mus__col = best_actor_com_mus_row.findall('td')[1]
    best_actress_com_mus = best_actress_com_mus__col.findall('.//li')

    best_actress_com_mus_list = []
    for idx in range(0,len(best_actress_com_mus)):
        if idx is 0:
            val = best_actress_com_mus[idx].find('b').find('a')
        else:
            val = best_actress_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_com_mus_list.append(actress_name)

    best_actor_supporting_row = wikitable.findall('tr')[11]
    best_actor_supporting_col = best_actor_supporting_row.findall('td')[0]
    best_actor_supporting = best_actor_supporting_col.findall('.//li')

    best_actor_supporting_list = []
    for idx in range(0,len(best_actor_supporting)):
        if idx is 0:
            val = best_actor_supporting[idx].find('b').find('a')
        else:
            val = best_actor_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_supporting_list.append(actor_name)

    best_actress_supporting_col = best_actor_supporting_row.findall('td')[1]
    best_actress_supporting = best_actress_supporting_col.findall('.//li')

    best_actress_supporting_list = []
    for idx in range(0,len(best_actress_supporting)):
        if idx is 0:
            val = best_actress_supporting[idx].find('b').find('a')
        else:
            val = best_actress_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_supporting_list.append(actress_name)

    best_director_row = wikitable.findall('tr')[13]
    best_director_col = best_director_row.findall('td')[0]
    best_director = best_director_col.findall('.//li')

    best_director_list = []
    for idx in range(0,len(best_director)):
        if idx is 0:
            val = best_director[idx].find('b').find('a')
        else:
            val = best_director[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        director_name = val_split[0].strip()
        best_director_list.append(director_name)

    best_screenplay_col = best_director_row.findall('td')[1]
    best_screenplay = best_screenplay_col.findall('.//li')

    best_screenplay_list = []
    for idx in range(0,len(best_screenplay)):
        if idx is 0:
            val = best_screenplay[idx].find('b').find('a')
        else:
            val = best_screenplay[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        screenplay_title = val_split[0].strip()
        best_screenplay_list.append(screenplay_title)

    best_music_row = wikitable.findall('tr')[15]
    best_music_col = best_music_row.findall('td')[0]
    best_score = best_music_col.findall('.//li')

    best_score_list = []
    for idx in range(0,len(best_score)):
        if idx is 0:
            val = best_score[idx].find('b').find('a')
        else:
            val = best_score[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        score_title = val_split[0].strip()
        best_score_list.append(score_title)

    best_song_col = best_music_row.findall('td')[1]
    best_song = best_song_col.findall('.//li')

    best_song_list = []
    for idx in range(0,len(best_song)):
        if idx is 0:
            val = best_song[idx].find('b').find('a')
        else:
            val = best_song[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        song_title = val_split[0].strip()
        best_song_list.append(song_title)

    best_other_row = wikitable.findall('tr')[17]
    best_other_col = best_other_row.findall('td')[0]
    best_animated_film = best_other_col.findall('.//li')

    best_animated_list = []
    for idx in range(0,len(best_animated_film)):
        if idx is 0:
            val = best_animated_film[idx].find('i').find('b').find('a')
        else:
            val = best_animated_film[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        animated_title = val_split[0].strip()
        best_animated_list.append(animated_title)

    best_other_col = best_other_row.findall('td')[1]
    best_foreign = best_other_col.findall('.//li')

    best_foreign_list = []
    for idx in range(0,len(best_foreign)):
        if idx is 0:
            val = best_foreign[idx].find('b').find('i').find('a')
        else:
            val = best_foreign[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        foreign_title = val_split[0].strip()
        best_foreign_list.append(foreign_title)

    return [
    best_movies_drama_list,
    best_movies_mus_or_com_list,
    best_actor_drama_list,
    best_actress_drama_list,
    best_actor_com_mus_list,
    best_actress_com_mus_list,
    best_actor_supporting_list,
    best_actress_supporting_list,
    best_director_list,
    best_screenplay_list,
    best_score_list,
    best_song_list,
    best_animated_list,
    best_foreign_list
    ]

''' Parse wikipedia for tv '''
def parse_2013_wikipedia_tv(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    body = tree.find('body')
    content_div = body.findall('div')[2]
    body_content_div = content_div.findall('div')[2]
    mw_content_div = body_content_div.findall('div')[3]
    wikitable = mw_content_div.findall('table')[2]

    best_tv_row = wikitable.findall('tr')[2]
    best_tv_drama_col = best_tv_row.findall('td')[0]
    best_tv_drama = best_tv_drama_col.findall('.//a')

    best_tv_drama_list = []
    for itm in best_tv_drama:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        tv_name = val_split[0].strip()
        best_tv_drama_list.append(tv_name)

    best_tv_mus_or_com_col = best_tv_row.findall('td')[1]
    best_tv_mus_or_com = best_tv_mus_or_com_col.findall('.//a')

    best_tv_mus_or_com_list = []
    for itm in best_tv_mus_or_com:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        tv_name = val_split[0].strip()
        best_tv_mus_or_com_list.append(tv_name)

    best_actor_row = wikitable.findall('tr')[5]
    best_actor_drama_col = best_actor_row.findall('td')[0]
    best_actor_drama = best_actor_drama_col.findall('.//li')

    best_actor_drama_list = []
    for idx in range(0,len(best_actor_drama)):
        if idx is 0:
            val = best_actor_drama[idx].find('b').find('a')
        else:
            val = best_actor_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_drama_list.append(actor_name)

    best_actress_drama_col = best_actor_row.findall('td')[1]
    best_actress_drama = best_actress_drama_col.findall('.//li')

    best_actress_drama_list = []
    for idx in range(0,len(best_actress_drama)):
        if idx is 0:
            val = best_actress_drama[idx].find('b').find('a')
        else:
            val = best_actress_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_drama_list.append(actress_name)

    best_actor_com_mus_row = wikitable.findall('tr')[8]
    best_actor_com_mus__col = best_actor_com_mus_row.findall('td')[0]
    best_actor_com_mus = best_actor_com_mus__col.findall('.//li')

    best_actor_com_mus_list = []
    for idx in range(0,len(best_actor_com_mus)):
        if idx is 0:
            val = best_actor_com_mus[idx].find('b').find('a')
        else:
            val = best_actor_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_com_mus_list.append(actor_name)

    best_actress_com_mus__col = best_actor_com_mus_row.findall('td')[1]
    best_actress_com_mus = best_actress_com_mus__col.findall('.//li')

    best_actress_com_mus_list = []
    for idx in range(0,len(best_actress_com_mus)):
        if idx is 0:
            val = best_actress_com_mus[idx].find('b').find('a')
        else:
            val = best_actress_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_com_mus_list.append(actress_name)

    best_actor_miniseries_row = wikitable.findall('tr')[11]
    best_actor_miniseries_col = best_actor_miniseries_row.findall('td')[0]
    best_actor_miniseries = best_actor_miniseries_col.findall('.//li')

    best_actor_miniseries_list = []
    for idx in range(0,len(best_actor_miniseries)):
        if idx is 0:
            val = best_actor_miniseries[idx].find('b').find('a')
        else:
            val = best_actor_miniseries[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_miniseries_list.append(actor_name)

    best_actress_miniseries_col = best_actor_miniseries_row.findall('td')[1]
    best_actress_miniseries = best_actress_miniseries_col.findall('.//li')

    best_actress_miniseries_list = []
    for idx in range(0,len(best_actress_miniseries)):
        if idx is 0:
            val = best_actress_miniseries[idx].find('b').find('a')
        else:
            val = best_actress_miniseries[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_miniseries_list.append(actress_name)


    best_actor_supporting_row = wikitable.findall('tr')[14]
    best_actor_supporting_col = best_actor_supporting_row.findall('td')[0]
    best_actor_supporting = best_actor_supporting_col.findall('.//li')

    best_actor_supporting_list = []
    for idx in range(0,len(best_actor_supporting)):
        if idx is 0:
            val = best_actor_supporting[idx].find('b').find('a')
        else:
            val = best_actor_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_supporting_list.append(actor_name)

    best_actress_supporting_col = best_actor_supporting_row.findall('td')[1]
    best_actress_supporting = best_actress_supporting_col.findall('.//li')

    best_actress_supporting_list = []
    for idx in range(0,len(best_actress_supporting)):
        if idx is 0:
            val = best_actress_supporting[idx].find('b').find('a')
        else:
            val = best_actress_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_supporting_list.append(actress_name)

    best_miniseries_row = wikitable.findall('tr')[16]
    best_miniseries_col = best_miniseries_row.findall('td')[0]
    best_miniseries = best_miniseries_col.findall('.//li')

    best_miniseries_list = []
    for idx in range(0,len(best_miniseries)):
        if idx is 0:
            val = best_miniseries[idx].find('i').find('b').find('a')
        else:
            val = best_miniseries[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        miniseries_title = val_split[0].strip()
        best_miniseries_list.append(miniseries_title)

    return [
    best_tv_drama_list,
    best_tv_mus_or_com_list,
    best_actor_drama_list,
    best_actress_drama_list,
    best_actor_com_mus_list,
    best_actress_com_mus_list,
    best_actor_miniseries_list,
    best_actress_miniseries_list,
    best_actor_supporting_list,
    best_actress_supporting_list,
    best_miniseries_list
    ]

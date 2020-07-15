from backend import app
from backend.models.mydictionary import MyDictionary
from flask import request, render_template, jsonify
import requests
import uuid
import re
# for reasons of security I created a module with external passwords to access apis that I've used here.
from backend import user_password_external


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_song')
def search_song():
    #lastfm api_key
    api_key = user_password_external.LASTFMAPIKEY
    song = request.args.get('song')
    rqt = requests.get(
        'http://ws.audioscrobbler.com/2.0/?method=track.search&track={}&api_key={}&format=json'.format(song, api_key))

    result = rqt.json()
    # print(result)
    results = []

    for i in result['results']['trackmatches']['track']:
        # print(result['results']['trackmatches']['track'])
        # print('Music :'+i['name']+' | Artist: '+i['artist']+'thumb :'+i['image'][0]['#text'])
        results.append({'Music': i['name'], 'Artist': i['artist'],
                        "thumb": i['image'][0]['#text']})  # , "thumb":i['image'][0]['#text']

    return jsonify({'results': results})


def bot_music(art, music):
    myjson = {

        "art": art,
        "mus": music,
        "apikey": f"{user_password_external.VAGALUMEAPIKEY}"
    }

    url = 'https://api.vagalume.com.br/search.php'
    bot = requests.post(url, data=myjson)

    result = bot.json()

    if result['type'] != 'notfound' and result['type'] != 'song_notfound':
        return result['mus'][0]['text']

    else:
        return result['type']


def yw_translate(words):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=pt'  # '&to=de&to=it'
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': user_password_external.MSCOGNITIVEAPIKEY,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = words
    reqt = requests.post(constructed_url, headers=headers, json=body)

    return reqt.json()


@app.route('/lyric')
def lyric():
    art = request.args.get('art')
    music = request.args.get('music')
    lyric = bot_music(art, music)


    song = ''

    for i in lyric.split('\n'):
        song = song + '<p>' + i + '</p>'

    name = "<h1>" + music + "</h1><br>"
    vocabulary = music_vocabulary(lyric)
    return jsonify({'lyric': name + song, 'vocabulary': vocabulary})


def music_vocabulary(lyric):
    total_palavras = None
    palavras_n_rep = None

    vocabulary_words = []

    all_words = []

    for word in lyric.split():
        word = word.split()
        for w in word:
            all_words.append(w)
            if w.lower() not in vocabulary_words:

                if w[-1] in ['?', '.']:
                    w = w[0:len(w) - 1]
                    vocabulary_words.append(w.lower())

                else:
                    w = w.lower()
                    vocabulary_words.append(w)

    total_palavras = 'total de palavras na musica = ' + str(len(all_words))

    musc = [re.sub(',', '', i.lower()) for i in vocabulary_words]
    musc
    musc = list(dict.fromkeys(musc))
    palavras_n_rep = 'total palavras não repetidas na música = ' + str(len(musc))

    musc.sort()
    result_local_transalte = []
    search_out = []

    for wword in musc:

        result = MyDictionary.query.filter_by(word=wword).first()

        if result != None:
            print(result)
            result_local_transalte.append(result)
        else:
            search_out.append(wword)

    new = ''

    new_format_to_api = []
    new_format_to_api2 = []
    # print(len(musc))
    # print(search_out)
    average = (len(result_local_transalte) / len(musc)) * 100
    average = str(round(average, 2)) + ' % das palavras desta música pertencem a lista das palavras mais usadas segundo Oxford'

    print(str(len(search_out)))
    for m in search_out:
        if len(new_format_to_api) <= 90:
            new_format_to_api.append({'text': m})
        else:
            new_format_to_api2.append({'text': m})

        # print(len(new_format_to_api), len(new_format_to_api2))
    for local_word in result_local_transalte:
        new = new + '<p>' + str(local_word) + '</p>'

    res = yw_translate(new_format_to_api)


    # print(res)
    for ii in res:
        new = new + '<p>' + search_out[res.index(ii)].capitalize() + ' = ' + ii['translations'][0]['text'].lower() + '</p>'

    if len(new_format_to_api2) > 0:

        res2 = yw_translate(new_format_to_api2)

        for iii in res2:
            new = new + '<p>' + search_out[res2.index(iii)].capitalize() + ' = ' + iii['translations'][0][
                'text'].lower() + '</p>'

    return "<h1>Vocabulario</h1> </br>" + new + "<strong><p>" + total_palavras + "</p>" + "<p>" + palavras_n_rep + "</p>" +"<p>"+ average +"</p> </strong>"



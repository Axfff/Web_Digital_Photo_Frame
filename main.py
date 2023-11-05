from flask import Flask, render_template, send_file

app1 = Flask(__name__)


@app1.route('/')
def mainPage():
    return render_template('mainPage.html')


@app1.route('/archive/JGA2023')
def JGA2023review():
    imgs = []
    with open('materials/Archive/JGA2023/showphotos/config.txt') as file:
        for photoInfo in file.read().split('\n'):
            # print(photoInfo)
            data = photoInfo.split('|')
            if not data or data == [""]:
                continue
            # print(data)
            imgs.append({'src': f'/archive/JGA2023/files/{data[0]}.jpg',
                         'lon': data[1], 'lat': data[2], 'bg': data[3], 'word': data[4]})

    return render_template('JGA2023review.html', imgs=imgs)


@app1.route('/archive/JGA2023/files/<fileName>')
def JGA2023review_file(fileName):
    if fileName == 'music':
        return send_file('materials/Archive/JGA2023/music.mp3', mimetype='audio/mpeg')
    else:
        return send_file(f'materials/Archive/JGA2023/showphotos/{fileName}', mimetype='image/jpeg')


if __name__ == '__main__':
    app1.run(debug=True, port=8000)

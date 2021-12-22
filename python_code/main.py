from flask import Flask, render_template, request, redirect
import os
import webbrowser
import movie
import random
import re


def sortVideo(videos: list):
    b = [re.findall('[0-9]+', el.split('.')[0])[0] for el in videos]
    result = dict(zip(b, videos))
    b.sort()
    return [result.get(el2) for el2 in b]


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/config-project/')
    TEMPLATE_DIR = os.path.abspath('template')
    STATIC_DIR = os.path.abspath('static')
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

    all_video = []
    all_video_path = []
    pathProject = ''

    all_video_order = []
    all_videoPath_order = []
    VIDEO_NAME = ''
    VIDEO_FPS = ''


    @app.route('/end/')
    def conf3():
        movie.createFilms(sortVideo(all_video_order), pathProject, VIDEO_NAME, VIDEO_FPS)
        return render_template('end.html')

    @app.route('/config-video/', methods=['GET', 'POST'])
    def conf2():
        all_color = ['#2a9d8f', '#e9c46a', '#e76f51']
        colors = [all_color[random.randint(0, 2)] for x in range(len(all_video))]

        if request.form:
            all_number = []
            inverse_video = {}
            ERROR = False

            for v in all_video:
                inverse_video[request.form[v]] = v
                all_number.append(request.form[v])

            all_number.sort()

            if len(set(all_number)) != len(all_number):
                ERROR = True
                print('error')
            else:
                ERROR = False
                for num in all_number:
                    value = inverse_video.get(num)
                    all_video_order.append(value)
                    all_videoPath_order.append(pathProject + '/Video/' + str(value))

                return redirect('/end')

            return render_template('index.html', all_video=sortVideo(all_video), all_video_path=all_video_path, Error=ERROR, color=colors)
        else:
            return render_template('index.html', all_video=sortVideo(all_video), all_video_path=all_video_path, color=colors)


    @app.route('/config-project/', methods=['GET', 'POST'])
    def conf():
        if request.form:

            if request.form['projectName'] and '/' in request.form['projectPath'] and request.form['videoName'] and request.form['videoFps']:
                projectName = str(request.form['projectName'])

                if str(request.form['projectPath'][-1]) != '/':
                    projectPath = str(request.form['projectPath']) + '/'
                else:
                    projectPath = str(request.form['projectPath'])

                global VIDEO_NAME, VIDEO_FPS
                VIDEO_NAME = str(request.form['videoName'])
                VIDEO_FPS = str(request.form['videoFps'])

                os.chdir(projectPath)
                try:
                    os.mkdir(projectName)
                    os.chdir(projectPath + projectName + '/')
                    os.mkdir('Video')
                    os.chdir('Video')
                except FileExistsError:
                    os.chdir(projectPath + projectName + '/')
                    os.chdir('Video')

                input("Click if all video are placed...")

                video_name = os.listdir(projectPath + projectName + '/Video/')

                for video in video_name:
                    all_video.append(video)
                    all_video_path.append(projectPath + projectName + '/Video/' + str(video))

                global pathProject
                pathProject = projectPath+projectName
                return redirect('/config-video')
            else:
                pathProject = ''
                pass

        return render_template("config.html")


    app.run(debug=True)


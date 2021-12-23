# import module
from flask import Flask, render_template, request, redirect
import os
import webbrowser
import movie
import random
import re
import cv2


# place the videos in ascending order (if there is a number in their name)
def sortVideo(videos: list):
    video = []
    for v in videos:
        if '/' in v:
            video.append(v.split('/')[-1])
        else:
            video.append(v)

    b = list(map(int, [re.findall('[0-9]+', el.split('.')[0])[0] for el in video]))
    result = dict(zip(b, videos))
    b.sort()
    return [result.get(el2) for el2 in b]


# pick the fist frame the video for display in the web site (with flask)
def pickFistFrame(VIDEO: list):
    count = 0
    pwd = "/home/guertinu/CODE/Python/FSV_editor/python_code/static/"
    for v in VIDEO:
        vidcap = cv2.VideoCapture(v)
        if not vidcap.isOpened():
            print('error dans l ouverture du fichier')
        elif vidcap.isOpened():
            success, image = vidcap.read()
            cv2.imwrite(pwd+"frame%d.jpg" % count, image)
            url_forTemplate.append(f"frame{count}.jpg")
        count += 1


# run main script
if __name__ == '__main__':

    # opens automatically the localhost flask (http://127.0.0.1:5000/)
    webbrowser.open('http://127.0.0.1:5000/config-project/')

    # save path for html/css/img/js file
    TEMPLATE_DIR = os.path.abspath('template')  # html save
    STATIC_DIR = os.path.abspath('static')  # css/img/js

    # create flask app
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

    # create default variable
    all_video = []
    all_video_path = []
    all_video_order = []
    all_videoPath_order = []
    url_forTemplate = []

    pathProject = ''
    VIDEO_NAME = ''
    VIDEO_FPS = ''

    all_color = ['#2a9d8f', '#e9c46a', '#e76f51']

    all_number = []
    inverse_video = {}

    # create "http://127.0.0.1:5000/end/"
    @app.route('/end/')
    def conf3():
        movie.createFilms(sortVideo(all_video_order), pathProject, VIDEO_NAME, VIDEO_FPS)
        return render_template('end.html')

    # create "http://127.0.0.1:5000/config-video/" + form (GET, POST)
    @app.route('/config-video/', methods=['GET', 'POST'])
    def conf2():
        pickFistFrame(sortVideo(all_video_path))

        # pick random color (just for the style of the website)
        colors = [all_color[random.randint(0, 2)] for x in range(len(all_video))]

        # if form is send
        if request.form:
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

                # move user -> "http://127.0.0.1:5000/end/"
                return redirect('/end')

            return render_template('index.html', all_video=sortVideo(all_video), all_video_path=all_video_path, Error=ERROR, color=colors, urlFor=url_forTemplate)

        # if not send
        else:
            return render_template('index.html', all_video=sortVideo(all_video), all_video_path=all_video_path, color=colors, urlFor=url_forTemplate)

    # create "http://127.0.0.1:5000/config-project/" + form (GET, POST)
    @app.route('/config-project/', methods=['GET', 'POST'])
    def conf():

        # delete all img who have an extension '.jpg'
        folder = (r'static/')
        file = os.listdir(folder)
        for imageJPG in file:
            if imageJPG.endswith('.jpg'):
                os.remove("static/"+imageJPG)

        # if form is send
        if request.form:

            # check if is not empty
            if request.form['projectName'] and '/' in request.form['projectPath'] and request.form['videoName'] and request.form['videoFps']:
                projectName = str(request.form['projectName'])

                # add end bar '/' in project path
                if str(request.form['projectPath'][-1]) != '/':
                    projectPath = str(request.form['projectPath']) + '/'
                else:
                    projectPath = str(request.form['projectPath'])

                # attribute a value to the variable
                global VIDEO_NAME, VIDEO_FPS
                VIDEO_NAME = str(request.form['videoName'])
                VIDEO_FPS = str(request.form['videoFps'])

                # change 'os' path
                os.chdir(projectPath)

                # if the project is not create (Create)
                try:
                    os.mkdir(projectName)
                    os.chdir(projectPath + projectName + '/')
                    os.mkdir('Video')
                    os.chdir('Video')

                # else if the project exist ignore
                except FileExistsError:
                    os.chdir(projectPath + projectName + '/')
                    os.chdir('Video')

                # pause script for put the video in "Video" folder
                input("Click if all video are placed...")

                # stock all video to the folder "Video"
                video_name = os.listdir(projectPath + projectName + '/Video/')

                # add to list
                for video in video_name:
                    all_video.append(video)
                    all_video_path.append(projectPath + projectName + '/Video/' + str(video))

                global pathProject
                pathProject = projectPath+projectName

                # move user "http://127.0.0.1:5000/config-video/"
                return redirect('/config-video')

            # if send is not good
            else:
                pathProject = ''
                pass

        # display the contained file 'config.html'
        return render_template("config.html")


    # run flask app
    app.run(threaded=True)


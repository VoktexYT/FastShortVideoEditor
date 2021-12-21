import os
import config_video


if __name__ == '__main__':
    INFO = config_video.confVideo()

    if INFO['projectPath'][-1] != '/':
        INFO['projectPath'] = str(INFO['projectPath'])+'/'

    os.chdir(INFO['projectPath'])
    os.mkdir(INFO['projectName'])
    os.chdir(INFO['projectPath']+INFO['projectName']+'/')
    os.mkdir('Video')
    os.chdir('Video')

    input("Click if all video are placed...")

    video_path = []
    video_name = os.listdir(INFO['projectPath'] + INFO['projectName'] + '/Video/')

    for video in video_name:
        video_path.append(INFO['projectPath'] + INFO['projectName'] + '/Video/'+str(video))
# import module for assembly the video
from moviepy.editor import *


def createFilms(all_video, project_path, video_name, video_FPS):

    # stock video duration
    video_clip_duration = [VideoFileClip(all_video[i]).duration for i, val in enumerate(all_video)]

    # stock video
    video_clip = [VideoFileClip(all_video[i]).subclip(0, videoTime) for i, videoTime in enumerate(video_clip_duration)]

    # stock concatenate all video 'video_clip'
    final_clip = concatenate_videoclips(video_clip)

    # upload video in project
    final_clip.write_videofile(project_path+'/'+video_name+".mp4", fps=int(video_FPS))
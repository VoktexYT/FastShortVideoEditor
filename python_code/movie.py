from moviepy.editor import *


def createFilms(all_video, project_path, video_name, video_FPS):
    print('all video:', all_video)
    print('project path:', project_path)
    print('video name:', video_name)
    print('video fps:', video_FPS)

    video_clip_stock = []
    video_clip_duration = []
    video_clip = []
    i = 0

    for video in all_video:
        video_clip_stock.append(video)
        video_clip_duration.append(VideoFileClip(video_clip_stock[i]).duration)
        i += 1

    i = 0
    for videoTime in video_clip_duration:
        video_clip.append(VideoFileClip(video_clip_stock[i]).subclip(0, videoTime))
        i += 1

    final_clip = concatenate_videoclips(video_clip)
    final_clip.write_videofile(project_path+'/'+video_name+".mp4", fps=int(video_FPS))
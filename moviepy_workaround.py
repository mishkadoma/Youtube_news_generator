from moviepy.editor import VideoFileClip

my_video = VideoFileClip("/home/mishkadoma/Desktop/test_sample.ts")


def hours_in_video(video):
    hoursinvideo = video.duration/60
    return "%.2f" % hoursinvideo


print("Video length is {} minutes and it is {} fps".
      format(hours_in_video(my_video), my_video.fps))

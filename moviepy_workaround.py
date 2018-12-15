from moviepy.editor import VideoFileClip

# my_video = VideoFileClip("/home/mishkadoma/Desktop/test_sample.ts")
my_video = VideoFileClip("/home/mishkadoma/Desktop/test_sample_2.mp4")


def hours_in_video(video):
    hoursinvideo = video.duration/60
    return "%.2f" % hoursinvideo


def cut_video(input_video, output_video, start, stop):
    result = input_video.subclip(start, stop)
    result.write_videofile("{}.mov".format(output_video),
                           codec="libx264", fps=my_video.fps)
    result.close()
    return result


print("Video length is {} minutes and it is {} fps".
      format(hours_in_video(my_video), my_video.fps))


print("".format(cut_video(my_video, "cutted_video", 33, 110)))

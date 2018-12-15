from moviepy.editor import VideoFileClip, TextClip

# my_video = VideoFileClip("/home/mishkadoma/Desktop/test_sample.ts")
my_video = VideoFileClip("/home/mishkadoma/Desktop/test_sample_2.mp4")


def hours_in_video(video):
    hoursinvideo = video.duration/60
    return "%.2f" % hoursinvideo


def cut_video(input_video, start, stop, output_video="cutted_video"):
    result = input_video.subclip(start, stop)
    result.write_videofile("{}.mp4".format(output_video),
                           codec="libx264", fps=my_video.fps)
    result.close()


def make_gif(input_video, start, stop, speed, output_gif="output.gif"):
    input_video.subclip(start, stop).speedx(speed).to_gif(output_gif)


print("Video length is {} minutes and it is {} fps".
      format(hours_in_video(my_video), my_video.fps))

#
# cut_video(my_video, 33, 110, "cutted_video")
# make_gif(my_video, 10, 12, 2)

my_video.save_frame("frame.jpeg")


# making clip out of the text

clip = TextClip("Sample text", font='Courier', fontsize=50, color="red")
clip.save_frame("text.png")
clip.duration = 10
clip.write_videofile("text.mov", codec="libx264", fps=10)

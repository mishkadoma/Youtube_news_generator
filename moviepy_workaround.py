from moviepy.editor import VideoFileClip
from moviepy.editor import TextClip
from moviepy.editor import concatenate_videoclips

# my_video = VideoFileClip("/home/mishkadoma/Desktop/test_sample.ts")
my_video = VideoFileClip("/home/mishkadoma/Desktop/test_sample_2.mp4")

clip1 = TextClip("Sample text",
                 font='Courier',
                 fontsize=150,
                 color="white",
                 size=(1920, 1080),
                 bg_color="blue")

clip2 = TextClip("Next paragraph",
                 font="Tahoma",
                 fontsize=350,
                 color="gray",
                 size=(1920, 1080),
                 bg_color="red")
clip3 = TextClip("It'll be awesome one day",
                 font="Times New Roman",
                 fontsize=90,
                 color="Yellow",
                 size=(1920, 1080),
                 bg_color="Black")


def hours_in_video(video):
    hoursinvideo = video.duration/60
    return "%.2f" % hoursinvideo


def cut_video(input_video, start, stop, output_video="cutted_video"):
    result = input_video.subclip(start, stop)
    result.write_videofile("{}.mp4".format(output_video),
                           codec="libx264", fps=input_video.fps)
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


clip1.save_frame("text.png")
clip1.duration = 5
clip2.save_frame("text2.png")
clip2.duration = 5
clip3.save_frame("text3.png")
clip3.duration = 5
# clip.write_videofile("text.mov", codec="libx264", fps=25)

final_clip = concatenate_videoclips([clip1, clip2, clip3])
final_clip.write_videofile("final_clip.mp4", fps=25)

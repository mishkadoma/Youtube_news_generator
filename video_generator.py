# from moviepy.editor import VideoFileClip
from moviepy.editor import TextClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import CompositeVideoClip
from moviepy.editor import ImageClip
from moviepy.editor import AudioFileClip


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


def main():
    image_clip_1 = ImageClip("planet.jpeg")
    image_clip_2 = ImageClip("ocean.jpeg")
    image_clip_3 = ImageClip("mountains.jpeg")
    background_music = AudioFileClip("Ticker.mp3").set_end(45)

    # TextClip template
    # clip = TextClip("Next paragraph",
    #                  font="Tahoma",
    #                  fontsize=350,
    #                  color="gray",
    #                  size=(1920, 1080),
    #                  bg_color="red")

    clip1 = TextClip("Sample text",
                     font='Courier',
                     fontsize=150,
                     color="white",
                     size=(1920, 1080))
    clip2 = TextClip("Next paragraph",
                     font="Tahoma",
                     fontsize=350,
                     color="gray",
                     size=(1920, 1080))
    clip3 = TextClip("It'll be awesome one day",
                     font="Times New Roman",
                     fontsize=90,
                     color="Yellow",
                     size=(1920, 1080))
    clip1_music = clip1.set_audio(background_music)

    #
    # cut_video(my_video, 33, 110, "cutted_video")
    # make_gif(my_video, 10, 12, 2)

    # making clip out of the text

    clip1.save_frame("text.png")
    clip1.duration = 5
    clip2.save_frame("text2.png")
    clip2.duration = 5
    clip3.save_frame("text3.png")
    clip3.duration = 5
    # clip.write_videofile("text.mov", codec="libx264", fps=25)

    # final_clip = concatenate_videoclips([clip1, clip2, clip3])
    # final_clip.write_videofile("final_clip.mp4", fps=25)

    alt_clip_1 = CompositeVideoClip([image_clip_1, clip1_music], size=(1920, 1080))
    alt_clip_1.duration = 15
    alt_clip_2 = CompositeVideoClip([image_clip_2, clip2], size=(1920, 1080))
    alt_clip_2.duration = 15
    alt_clip_3 = CompositeVideoClip([image_clip_3, clip3], size=(1920, 1080))
    alt_clip_3.duration = 15

    # alt_clip.write_videofile("image_clip.mp4", fps=25)
    # final_clip = concatenate_videoclips([alt_clip_1, alt_clip_2, alt_clip_3])
    final_clip = concatenate_videoclips([alt_clip_1, alt_clip_2, alt_clip_3])
    final_clip.write_videofile("final_clip.mp4", fps=25)
    print("Video length is {} minutes and it is {} fps".
          format(hours_in_video(final_clip), final_clip.fps))


if __name__ == '__main__':
    main()

from moviepy.editor import *
from gtts import gTTS



clip_1 = VideoFileClip("Assests/Travel/f1.mp4").subclip(00,4)
clip_2 = VideoFileClip("Assests/Travel/f1.mp4").subclip(00,4)
clip_3 = VideoFileClip("Assests/Travel/f1.mp4").subclip(00,4)
clip_4 = VideoFileClip("Assests/Travel/f1.mp4").subclip(00,4)






# through this coe we can convert an mp4 file into a gif file

# video = VideoFileClip("tests.mp4").subclip(00,5)
# video.write_gif("test1.gif")

# through this code we can spilt a screen of video

# clip_1 = VideoFileClip("tests.mp4").subclip(0,5)
# clip_2 = VideoFileClip("test2.mp4").subclip(5,10)
# clip_3 = VideoFileClip("test3.mp4").subclip(0,5)
# clip_4 = VideoFileClip("test4.mp4").subclip(0,5)

# combined = clips_array([[clip_1,clip_2],[clip_3,clip_4]])
# combined.write_videofile("final_test.mp4")

# through this we can add watermark to the video background


# clip = VideoFileClip("tests.mp4").subclip(0,10)

# txt_clip = TextClip("Wrath Gamerz",fontsize=20,color="white")
# txt_clip = txt_clip.set_position("center").set_duration(10)

# video = CompositeVideoClip([clip,txt_clip])
# video.write_videofile("final_tests.mp4")


# how to combine or merge videos

# clip_1 = VideoFileClip("tests.mp4").subclip(0,5)
# clip_2 = VideoFileClip("test2.mp4").subclip(5,10)
# clip_2 = clip_2.set_position(45,100)



final_video = concatenate_videoclips([clip_1,clip_2,clip_3,clip_4])
final_video.crossfadein(5.0)
final_video.write_videofile("Assests/finals_output.mp4")











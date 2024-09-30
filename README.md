# WeddingGallery_v1
First Trial of Wedding Gallery (subsidiary of Webbing Co.) at AR Wedding

![Demo of Website with random pictures](img_gh/gallery1.png)


## Successes:
- Used Google Drive as Storage for all the pictures
- Website automatically updated every time a picture was addedd
- Website displayed the pictures without screwing up the image ratios and still had the gallery look nice
- Also had functionality to add a small note/comment under each picture that could be seen on hovering


## Its not a bug, it's a feature!
- The website itself loads pretty quickly since all the images are actually thumbnails - because reading images from google drive through the API only allowed thumbnails? So yay, the website is very lightweight
- The website auto-loads the 20/30 most recent images from the drive. There's a load more button on the bottom that you can keep clicking as long as there are more pictures to load. Another way to keep it loghtweight and not have me set up a dedicated server for this wedding website.
- You can input pictures directly onto the google drive and have it show up on the gallery website. This is because setting up a method to upload pictures into google drive could only take 10/20 pictures at a time- not feasible for a wedding when each of my friends had 100 pictures to upload.
- Best used on laptop because on phone the sidebar is too big and doesn't scale well. Its a feature okay!

## Things I want to achieve in version 2:
- Upload feature on the website itself. There has to be a better way
- Caching
- Comment/Like option - so I can have a "Most Liked Picture" or contests and stuff, that would be cool
- Better UI. It looks great and all, but I can do better. (Especially if I start more than 4 days before the wedding)
- Facial recognition feature so everyone can find their own pictures as a set
- Maybe better data management system, but everything is paid, so this is a maybe for v3

## Notes for execution:
- you have to get `credentials.json` by setting up the Google Drive API
- `token.json` is created automatically at first run
- In `app.py`
  - a list of hyperlinks pertaining to all images in the respective google drive folder is obtained and stored.
  - This list of hyperlinks is specifically link to the thumbnails of the images in GDrive. Thumbnails are the only one that worked properly, I then resized it - hack I found somewhere.
  -  `gallery.html` then displays eveyrthing nicely
  -  Use chatgpt to edit the `styles.css` file because it is just too long and annoying.
- Execution : `python app.py` in cmd
![Demo of Website with random pictures](img_gh/gallery2.png)


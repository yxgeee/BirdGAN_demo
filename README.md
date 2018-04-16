# Generate Bird Images by Text

**Screen Shot**
![screenshot](https://github.com/gyxoned/bird_demo/blob/master/static/img/screen.png)

Web demo for generating bird images by description. 
The web framework is built up on Django, and the generation function of backend system is written by pytorch. (costs about 900M GPU memory)
Thanks for [AttnGAN](https://github.com/taoxugit/AttnGAN).

### Dependencies
- `python 2.7`
- `Pytorch`
- `Django 1.11`

### Download required packages and pretrained models
described in AttnGAN/README.md

### Run the server
``python manage.py runserver 0.0.0.0:8000``,
and then visit your web by ``http://localhost:8000/``,
you can change 8000 to any other port as you want.
# Generate Bird Images by Text
  

Web demo for generating bird images by description. 
The web framework is built up on Django, and the generation function of backend system is written by pytorch. (costs about 900M GPU memory)  
Thanks for [AttnGAN](https://github.com/taoxugit/AttnGAN).

![screenshot](https://github.com/gyxoned/bird_demo/blob/master/static/img/screen.png)

### Dependencies
- `python 2.7`
- `Pytorch`
- `Django 1.11`

### Download required packages and pretrained models
described in AttnGAN/README.md

### Run the server
run ``python manage.py runserver 0.0.0.0:8000`` in the root directory, 
and then visit your web by ``http://localhost:8000/``, 
also you can change ``8000`` to any other port as you want.
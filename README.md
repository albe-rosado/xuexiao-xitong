# IMNU Postgraduate Mathematics Competition Papers Submission System


IMNU Postgraduate Mathematics Competition Papers Submission System is a web app that provides the tools for hosting competitions like [China's National Mathematical Modeling Competition](http://www.mcm.edu.cn/) (中国国家数学建模比赛). The interface is in Chinese, as it was made for chinese collegue students. For a better idea about the uses of the app , take a look to this [document](https://pan.baidu.com/s/1kVE00cv).


### Tech
The app was built with Flask, and make use of:
* [Material Theme](https://getmdl.io/)
* [Twitter Bootstrap](https://getbootstrap.com/) - Great UI boilerplate for modern web apps
* [Flask-Turbolinks](https://github.com/lepture/flask-turbolinks) - Turbolinks for Flask
* [Flask-Cloudy](https://pypi.python.org/pypi/Flask-Cloudy) - Standalone library to upload and save files on S3, Google storage or other Cloud Storages.


### Installation
Clone the repository, install the dependencies and start the server.

```sh
$ git clone https://github.com/albe-rosado/xuexiao-xitong.git
$ cd xuexiao-xitong
$ pip install -r requirements.txt
$ ./run.py
```

### Todos
 - Write Tests
 - Add English language
 

### License
- [MIT](https://en.wikipedia.org/wiki/MIT_License)

---
Proudly powered by [Flask](http://flask.pocoo.org/)

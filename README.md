# project_projecter
projecter is a program for helping you to changing codes from everywhere :)

# installation
clone this project : 
``` bash
git clone https://github.com/ebad84/project_projecter.git
```
install the *pynput* library :
``` python
pip install pynput
```
for server, upload the **php.php** file in a *host* and than, change the ***http://localhost/pjc/php.php*** url in **uploader** function with your php.php url.

# running
for running, first create folder **files** next to the **pjc.py** file
**files** folder is for your codes. its waiting for change in your files and doing this commands auto :
``` bash
cd files
git init
git status
git add .
git commit -m 'time'
```
and after commit, its will be create a *zip* file next to the **pjc.py** file and after that, uploader that in your host with the **uploader** function.

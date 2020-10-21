import shutil
import os
import requests
from datetime import datetime
from subprocess import getoutput as gout
from pynput.keyboard import  Listener

__PATH__ = 'files'
__lname__ = ''

def change_dir(path):
    p = os.getcwd().split('\\')
    if p[len(p)-1] == path:
        pass
    else:
        os.chdir(path)

def git_init():
    gout('git init')

def keypress(Key):
    print(Key)

def git_commit():
    global __lname__
    __lname__ = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    gout("git commit -m '%s'" % __lname__)

def git_add():
    gout('git add .')

def git_status():
    return gout('git status')

def zipper():
    global __lname__
    __lname__ = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    shutil.make_archive(r'..\file_%s' % __lname__, 'zip', r'..\files')

def uploader():
    global __lname__
    out = requests.post("http://localhost/pjc/php.php",data={'name':'%s.zip' % __lname__,'data':open(r'..\file_%s.zip' % __lname__,'r').read()})
    print(out.text)
    #pass

change_dir(__PATH__)
git_init()
while True:
    data = git_status()
    if "Untracked files" in data or "Changes not staged" in data:
        git_add()
        print('added files')
        git_commit()
        print('commited')
        zipper()
        print('zipped')
        print('uploading...')
        uploader()
        print('uploaded')


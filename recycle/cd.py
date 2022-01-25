import os

basedir = './StudyLog'

dirlst = os.listdir(basedir)

for dir in dirlst:
    if '.' not in dir:
        print('move ' + os.getcwd() + '\\StudyLog\\' + dir + '\\*.py '+ os.getcwd() + '\\')
        os.system('move ' + os.getcwd() + '\\StudyLog\\' + dir + '\\*.py '+ os.getcwd() + '\\')


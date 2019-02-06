import subprocess

for i in range(40):
    curr_sleep = str((i + 20) * 300) # start with an hour and a forty minutes, five minute intervals
    print("Opening subprocesses for %s seconds" % curr_sleep)
    subprocess.Popen(['python3',
                      'sleepy.py',
                      curr_sleep])
    subprocess.Popen(['ruby',
                      'dd-ruby.rb',
                      curr_sleep])

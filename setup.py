import os
var = int(50)
try:
    while var > 0:
        os.system('cd')
        var = (var - 1)
    os.system("cd")
    os.system("sudo chmod a+x 000")
    os.system("echo Setup complete!")
except:
    os.system("echo Uh OH there was an error! (make sure you have access to sudo)")

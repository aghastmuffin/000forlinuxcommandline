import os
try:
  os.system("sudo chmod a+x 000")
  os.system("echo Setup complete!")
except:
  os.system("echo Uh OH there was an error! (make sure you have access to sudo)")
  

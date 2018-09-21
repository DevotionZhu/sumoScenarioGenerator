# Olaf Angelo Banse - 2018

# This script deletes .ZIP files older than 24hours
# This script should be called by a CRON JOB
import time
import os

epoch_now = time.time()
directory = os.getcwd() + "/cgi-bin" # PATH where the ZIP files are being stored
desired_time = epoch_now - (24 * 3600) # desired_time is epoch_now minus 24 hours (in seconds)

os.chdir(directory)

for zipFiles in os.listdir('.zip'):
    st = os.stat(zipFiles)
    mtime = st.st_mtime
    if mtime < epoch_now and zipFiles.endswith(".zip")
     os.remove(zipFiles)
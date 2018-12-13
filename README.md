#The Raspberry Pi 3B+ with the functions of PIR and mp3 played by mplayer

This is a project that uses a PIR sensor. When something/someone moves, it 
will play a mp3 file and light a LED.

STEPS:

1.setup MPlayer
$sudo apt-get update
$sudo apt-get -y install mplayer

2.create pi3_pir_and_openmp3.py

3.create pirmp3.sh

4.The last step is:
$sudo nano ~/.config/lxssession/LXDE-pi/autostart
Then add:
@sh /home/pi/pi3_pir_and_openmp3/pirmp3.sh

 

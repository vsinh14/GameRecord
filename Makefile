#basic program makefile
CC=python3
PL=vlc
run:
	$(CC) recorder.py
play:
	$(PL) Recording1.*
clean:
	rm -Rf .*.png *.avi *.mp4 *.png

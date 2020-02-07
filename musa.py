import tkinter
import tkinter as tk
import tkinter.messagebox

import pyaudio

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import wave
import os
import sys
#This is my project

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "voice.wav"

def record_user():

	# instantiate PyAudio (1)
	p = pyaudio.PyAudio()

	# define callback (2)
	def callback(in_data, frame_count, time_info, status):
		data = wf.readframes(frame_count)
		return (data, pyaudio.paContinue)

	# open stream using callback (3)
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)

	print ("recording...")
	frames = []

	# Record for RECORD_SECONDS
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
		
		
	print ("finished recording")


	# Stop Recording
	stream.stop_stream()
	stream.close()
	p.terminate()
""" ANiMATe"""

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def draw_waveform():
	spf = wave.open('voice.wav','r')

	#Extract Raw Audio from Wav File
	signal = spf.readframes(-1)
	signal = np.fromstring(signal, 'Int16')
	plt.figure(1)
	plt.title('Signal Wave...')
	plt.plot(signal)
	plt.show()
	
def animation_sound():
	ani = animation.FuncAnimation(
	fig, animate, init_func=init, interval=2, blit=True, save_count=50)

	plt.show()
	
def init():  # only required for blitting to give a clean slate.
	line.set_ydata([np.nan] * len(x))
	return line,


def animate(i):
	line.set_ydata(np.sin(x + i / 100))  # update the data.
	return line,




record_user()
draw_waveform()
#animation_sound();
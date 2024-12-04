from abc import ABC
import PySimpleGUI as sg

class Exception(ABC):
    def __init__(self, msg):
        sg.Popup(msg)
        
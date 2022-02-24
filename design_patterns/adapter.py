from __future__ import annotations

import speech_recognition as recognition
from enum import Enum
import ffmpy
import cv2


class Language(Enum):
    english = "en-US"
    ukrainian = "uk-UA"


class VoiceAssistant:
    def __init__(self, language: Language):
        self.recognizer = recognition.Recognizer()
        self.language = language.value

    def recognize_speech(self) -> str:
        speech_text = ""
        with recognition.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Please say something...")
            audio = self.recognizer.listen(source)
            print("Recognizing...")
            try:
                speech_text = self.recognizer.recognize_google(audio, language=self.language)
            except Exception as e:
                print(f"Error: {e}")
        return speech_text

    def recognize_and_save(self, file_name: str) -> None:
        with recognition.Microphone() as source:
            audio = self.recognizer.listen(source)
            with open(f"{file_name}.wav", "wb") as file:
                file.write(audio.get_wav_data())


class CameraAssistant:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        self.height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
        self.size = (self.width, self.height)
        self.camera_used = False

    def turn_on_camera(self):
        while True:
            _, frame = self.capture.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.camera_used = True
        self.capture.release()
        cv2.destroyAllWindows()

    def record_video(self, file_name: str):
        if self.camera_used:
            print("Reload Video Capture")
            self.capture = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        output_video = cv2.VideoWriter(f"{file_name}.avi", fourcc, 20.0, self.size)
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            output_video.write(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.camera_used = True
        self.capture.release()
        output_video.release()
        cv2.destroyAllWindows()


class Adapter(VoiceAssistant, CameraAssistant):
    def __init__(self, language: Language):
        super().__init__(language)

    @staticmethod
    def convert_avi_to_mp4(file_name: str):
        pass

    @staticmethod
    def convert_wav_to_mp3(file_name: str):
        pass

    def record_mp3(self):
        """
        Record audio and convert to mp3
        """
        pass

    def record_mp4(self):
        """
        Record video and convert to mp4
        """
        pass

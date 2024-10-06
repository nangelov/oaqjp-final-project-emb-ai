import unittest

from docutils.nodes import status

from emotion_detection import emotion_detector
import json

class EmotionDetectorTestCases(unittest.TestCase):
    def test_emotion_detector_of_joy(self):
        with self.subTest("Testing emotion detection for a joyful phrase"):
            text = "I am glad this happened"
            expected_dominant_emotion = 'joy'
            result = emotion_detector(text)
            result_dict = json.loads(result)
            self.assertEqual(result_dict['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_detection_of_anger(self):
        with self.subTest("Testing emotion detection for a angry phrase"):
            text = "I am really mad about this"
            expected_dominant_emotion = 'anger'
            result = emotion_detector(text)
            result_dict = json.loads(result)
            self.assertEqual(result_dict['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_detection_of_disgust(self):
        with self.subTest("Testing emotion detection for a disgusting phrase"):
            text = "I feel disgusted just hearing about this"
            expected_dominant_emotion = 'disgust'
            result = emotion_detector(text)
            result_dict = json.loads(result)
            self.assertEqual(result_dict['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_detection_of_sadness(self):
        with self.subTest("Testing emotion detection for a sad phrase"):
            text = "I am so sad about this"
            expected_dominant_emotion = 'sadness'
            result = emotion_detector(text)
            result_dict = json.loads(result)
            self.assertEqual(result_dict['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_detection_of_fear(self):
        with self.subTest("Testing emotion detection for a fearful phrase"):
            text = "I am really afraid that this will happen"
            expected_dominant_emotion = 'fear'
            result = emotion_detector(text)
            result_dict = json.loads(result)
            self.assertEqual(result_dict['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_detection_of_empty_input(self):
        with self.subTest("Testing emotion detection for a fearful phrase"):
            text = ""
            expected_dominant_emotion = 'None'
            result = emotion_detector(text)
            result_dict = json.loads(result)
            self.assertEqual(result_dict['dominant_emotion'], expected_dominant_emotion)

if __name__ == '__main__':
    unittest.main()

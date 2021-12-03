from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.image import Image
from kivy.lang import Builder
from kivy.config import Config
import random

Builder.load_file('BasisSchermLayout.kv')


class MyLayout(Widget):

  def press_it(self):
    current = self.ids.my_progress_bar.value
    current_question = self.ids.my_label.value

    if current == 1:
      current = 0

    if current_question == 5:
      current_question = 0
    
    current += .20
    current_question += 1

    self.question_choser()

    self.ids.my_progress_bar.value = current
    self.ids.my_label.value = current_question
    self.ids.my_label.text = f'Vraag {self.ids.my_label.value}'
  
  def question_choser(self):
    questions = ['vraag1: testen', 'vraag2: Hallo', 'vraag3: hoi', 'vraag4: doeg']

    while len(questions) > 0:
      index = random.choice(questions)
      self.ids.my_label_question.text = index
      questions.remove(index)
      print(questions)


class MyApp(App):
  def build(self):
    return MyLayout()


if __name__ == '__main__':
  Config.set('graphics', 'fullscreen', 'auto')
  Config.set('graphics', 'window_state', 'maximized')
  Config.write()
  MyApp().run()
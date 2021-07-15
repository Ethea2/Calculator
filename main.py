from kivy.app import App
from kivy.lang import Builder
from calculations import Calculator


class MainClass(App):
	def build(self):
		return Calculator()


if __name__ == "__main__":
	MainClass().run()
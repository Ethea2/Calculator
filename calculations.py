from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("calculator_kvlang.kv")

class Calculator(Widget):
	def clear_box(self):
		self.ids.number_box.text = "0"


	def number_insert(self, number):
		number_inside = self.ids.number_box.text

		if number_inside == "0":
			self.ids.number_box.text="" + f"{number}"
		else:
			if number == ".":
				number_split = number_inside.split("+")
				for number in number_split:
					if "." not in number:
						self.ids.number_box.text = f"{number_inside}."
					else:
						pass
			else:
				self.ids.number_box.text = f"{number_inside}{number}"


	def equals(self):
		number_inside = self.ids.number_box.text

		answer = eval(number_inside)
		self.ids.number_box.text = str(answer)


	def negative_command(self):
		number_inside = self.ids.number_box.text

		if number_inside.startswith("-"):
			self.ids.number_box.text = self.ids.number_box.text.replace(self.ids.number_box.text[0], "")
		else:
			self.ids.number_box.text = f"-{number_inside}"


	def backspace(self):
		number_inside = self.ids.number_box.text[:-1]

		self.ids.number_box.text = number_inside


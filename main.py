from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import pandas as pd 
import time
#kivy.requires("1.11.0")


circle_presses = []
square_presses = []

# Widget class and event handlers for the buttons
class ButtonGame(BoxLayout):

    def circle_press(self):
        # Keeping time stamp of whenver the button is pressed
        nowTime = time.asctime(time.localtime(time.time()))
        circle_presses.append(nowTime)
        square_presses.append(0)

    def square_press(self):
        nowTime = time.asctime(time.localtime(time.time()))
        square_presses.append(nowTime)
        circle_presses.append(0)

# The main app is run here
class MouseApp(App):
    def build(self):
        buttGame = ButtonGame()
        return buttGame
    
    # Event handler that creates the dataframe and outputs it when app closes
    def on_stop(self):
        #print(circle_presses)
        #print(square_presses)

        df = pd.DataFrame(
                {"Circle Presses": circle_presses,
                    "Square Presses": square_presses
                })

        # Export to csv
        df.to_csv("mouse_game_results.csv", index=False)

if __name__ == "__main__":
    try:
        MouseApp().run()
    except KeyboardInterrupt:
        print("Exiting due to keyboard")
        App.get_running_app().stop()

# temperature_converter.py
# a simple gui example using 'graphics.py' in the text book

from graphics import * 

def main():
    win = GraphWin("Celcius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0) 

    # draw interface 
    Text(Point(1,3), "  Celcius Temperature:").draw(win)
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
    inputText = Entry(Point(2.25, 3), 5) 
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "Convert it") 
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    # wait for a mouse click 
    win.getMouse()

    # convert input 
    celsius = float(inputText.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32 

    # display output and change button 
    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit") 

    # wait for click and then exit 
    win.getMouse()
    win.close()

main()



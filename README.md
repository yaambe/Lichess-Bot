# Lichess-Bot
 A chess bot for hyper speeds. Most people its impossible to use computer assistance at hyper speeds, well they are wrong.

we are using stockfish and google chrome for this automation

1. you need to have stockfish executable downloaded and know the path to it.
2. you need to have chromedriver executable downloaded and know the path to it.
3. to install the dependencies run the following command for mac.

pip3 install -r requirement.txt

for windows

pip install -r requirement.txt

4. you need to configure the executable path in webdriver.py file to your executable path
5. you need to configure the executable path in chess_engine.py file to your executable path
6. find the cordinates of the positions of the screen using get_positions.ipynb file (there is a difference in cordinates
    as when chrome is opened in automated mode there is a bar on top of the screen that shrinks everything on the y axis
    a little)
7. enter the cordinates to the positions.py file
8. run the main.py file

example games
1. https://lichess.org/NpWJJqlZsW4R (bot as white)
2. https://lichess.org/@/YellowFlash2023/all (bullet games by this user "YellowFlash2023"

# FourierSeriesImplementation
A programm that enables you to play around with the Fourier Series Algorithm


To get the program up and running you can follow the steps below:

1. Clone this repository to your local machine through running "git clone https://github.com/m-J-K-b/FourierSeriesImplementation.git" (You can get the URL through      viewing the main branch of this repo and clicking on the dropdown option called "code" in top right. There you can select how you want to clone the repository.) and executing the involved steps or download the Zip of the repo.
2. Next navigate into the folder the repository was cloned into and setup a virtual environment (for example: run "python -m venv {venv name}" for windows)
3. Install the requirements: "pip install -r requirements.txt"
4. Run the main.py file
5. Have fun :)

## How to use:

Once you started the program you should see the settings menu with a description of the program on the right and a few checkboxes on the left side of the screen. 
To exit the or enter Menu wenever you want, you can press "Escape".
Once you've pressed "Escape" you should be seeing a line beeing drawn on the screen. 
I advise you to turn on the checkboxes in the settings menu one after another and see what effect they have on the image.
Initially a few randomly placed points are being used as the input function for the algorithm. Through pressing "R" you can generate a new set of random points.
In the topleft the amount of sample points is displayed. If you want to approximate the function more precisely you can scroll your mousewheel up and down.
If you want to input your own drawing into the program you can press "Tab" and an overlay will appear on which you can draw whatever your heart desires with the left mouse button. 
With the right mouse button you can erase unwanted points. 
Through pressing "Tab" again you can see your magnificent Artwork being drawn by the Program using the Algorithm.
Note that pressing "Escape" when you are in drawing mode will cause you to open the settings menu and loose what you drew.


"Escape" - open or close the settings menu.

"R" -- generate a bunch of random points to be used as the input function for the Algorithm.

"Tab" -- open a drawing interface on which you can draw with the left mouse button and erase with the right mouse button.

"Mouse Sroll Wheel" / "Up key" or "Down key" -- increase or decrease the amount of samples that the program uses to approximate the input function.

### references

1. Wikipedia Fourier Transform: https://en.wikipedia.org/wiki/Fourier_transform
2. Wikipedia Fast Fourier Transform: https://en.wikipedia.org/wiki/Fast_Fourier_transform
3. The coding train, "Coding Challenge 125: Fourier Series": https://www.youtube.com/watch?v=Mm2eYfj0SgA
4. The coding train, "Coding Challenge #130.1: Drawing with Fourier Transform and Epicycles": https://www.youtube.com/watch?v=MY4luNgGfms
5. The coding train, "Coding Challenge #130.2: Fourier Transform User Drawing": https://www.youtube.com/watch?v=n9nfTxp_APM
6. 3Blue1Brown, "But what is a Fourier series? From heat flow to drawing with circles | DE4": https://www.youtube.com/watch?v=r6sGWTCMz2k
7. 3Blue1Brown, "What is a Fourier-Transform? A Visual introduction": https://www.youtube.com/watch?v=spUNpyF58BY

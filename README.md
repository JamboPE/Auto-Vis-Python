# Automatic Visualisation for University Radio York Studio Red (in Python)

This project aims to provide automatic visualizations for the University Radio York Studio Red using Python.

## Description

The purpose of this Python script is to automate visualised radio shows or podcasts in Studio Red by changing the live camera based on who is speaking and switching to visualisation timelord automatically during songs or the news to prevent copyright strikes.

## Configure Companion Host

You will need a device running [Bitfocus Companion](https://bitfocus.io/companion) as Python libraries for controlling OBS and Blackmagic ATEMs are a little dicy but http requests to a program that can do it for me aren't. Set up connections in Companion to your OBS instance and to the ATEM. Next import the companion page config file `page99.companionconfig` to a page of your choice (making sure to set the page number in `credentials.py`)

## Installation

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/JamboPE/auto-vis-python.git` onto the studio PC.
2. Install the required dependencies: `pip install -r dependencies`
3. Configure the script credentials/settings: Edit `credentials.py` file and update the necessary parameters: adding your MyRadio API key, Bitfocus Companion host IP, Companion page and microphone audio input devices.
5. Run `test_threashold.py` to work out a good mic threshold to set in `credentials.py` to detect speech.
6. Delete anything not inside the folder `python program` as it is no longer needed.

## Usage

Run the script and pray to the python and linux audio gods: `python main.py`.

## Contributing

Contributions are welcome! If (for some reason) you would like to contribute to this project, please follow these steps:

1. Create a new branch: `git checkout -b feature/your-feature`
2. Make your changes and commit them: `git commit -m 'Add your feature'`
3. Push to the branch: `git push origin feature/your-feature`
4. Submit a pull request.

## Final Notes

There is a much better auto visualisation repository [here](https://github.com/UniversityRadioYork/autoviz) that includes features like clipping of your shows and more! I just made this as I don't understand typescript but I would recommend trying that project first before this one.

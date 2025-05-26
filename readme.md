# Installation & Setup
* TODO: add instructions for directory management
* You will need to install cmake prior to running these steps
* git clone https://github.com/arkorobotics/CW2OBS
* cd CW2OBS
* brew install blackhole-2ch
* brew install SDL2
* brew install python@3.10
* /usr/local/bin/python3.10 -m venv cwenv
* source cwenv/bin/activate
* pip install sounddevice numpy obs-websocket-py morse-audio-decoder scipy
* Next, you will need to build ggmorse 
    * For the next steps, to use newer version of `cmake` you will need to run it with the following flag: `cmake .. -DCMAKE_POLICY_VERSION_MINIMUM=3.5`
    * `cd ggmorse && mkdir build && cd build`
    * `cmake .. -DCMAKE_POLICY_VERSION_MINIMUM=3.5`
    * `make`
    * `cd ../..`
* Run `python3 -m sounddevice` and note the index of the audio stream you wish to decode
* Update the `AUDIO_DEV` variable in `cw_to_obs.py` with the audio index from the previous step

# Run

* Open OBS and create a Source "Text" with the name CWbanner 
* Run `python3 cw_to_obs.py`

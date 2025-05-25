* brew install blackhole-2ch
* brew install python@3.10
* /usr/local/bin/python3.10 -m venv cwenv
* source cwenv/bin/activate
* pip install sounddevice numpy obs-websocket-py morse-audio-decoder scipy
* Clone and build ggmorse
    * Note, to use cmake you will need to run it with the following flag: cmake .. -DCMAKE_POLICY_VERSION_MINIMUM=3.5
* build ggmorse-gui
* Run python3 cw_to_obs.py

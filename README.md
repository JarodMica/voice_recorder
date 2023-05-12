# voice_recorder
Simple voice recorder that uses your default microphone to record audio and output it to a folder called ```audio_files```

## How to use it
#### EXE
There is an exe version of it in the releases area, just go to the following link and download the exe file: https://github.com/JarodMica/voice_recorder/releases

If you're using the exe, your anti-virus may block it due to being an unknown exe file, you just have to allow it or use the python script version of it.

#### Python
Clone the repo with:

```git clone https://github.com/JarodMica/voice_recorder.git```

Once you have done that, navigate into the folder and install requirements.  I recommend you use a venv if you're familiar with them to prevent any package issues later on:
```
cd voice_recorder
pip install -r requirements.txt
```

Now that you have all the requirements, you should be able to just run the script either by using an IDE or by CMD with the following command (as long as you're in the voice_recorder folder path):
```python voice_recorder.py```

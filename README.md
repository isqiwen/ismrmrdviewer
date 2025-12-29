# ISMRMRD Viewer

ISMRMRDVIEWER is a python package to view ISMRMRD/MRD (vendor agnostic MRI data format) raw data (including xml, data, waveforms and trajectories) and images.

## Requirements
- Python 3.13 or newer.
- Latest PySide6 release (6.7 or newer) and the dependency versions defined in `requirements.txt`.

## Installation
```bash
pip install git+https://github.com/isqiwen/ismrmrdviewer.git
```

## Usage
```bash
ismrmrdviewer [optional-data-file.mrd]
```
Inside the UI:
- File → Open to choose a dataset if none was passed.
- Image series can be animated and interactively windowed.
- Raw data lines can be browsed individually or in multiples.

## Develop / Run Without Installing
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
git lfs install              # first-time setup (if Git LFS is installed)
git lfs pull                 # optional, fetches sample data in res/data
python -m ismrmrdviewer res/data/simple.h5
```
Replace the last argument with any `.mrd/.h5` file you want to view; omit it to launch an empty window and use File → Open.

If `git lfs` is not available, install Git LFS from https://git-lfs.com/ (e.g., `brew install git-lfs`, `choco install git-lfs`, `apt install git-lfs`, etc.) before running the commands above.

## Contributing
Features are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

# Real-Time Object Detection with YOLOv8

A webcam-based object detection project built with Ultralytics YOLOv8 and OpenCV. The application reads live video from the default camera, detects objects in each frame, draws bounding boxes and labels, and saves annotated frames whenever at least one object is detected.

## Overview

This project demonstrates a simple real-time computer vision pipeline:

1. Load a pretrained YOLOv8 model.
2. Open the computer's default webcam.
3. Read video frames continuously.
4. Run object detection on each frame.
5. Display the annotated result in a window.
6. Save frames that contain one or more detected objects.
7. Release the camera and close the display window when the user exits.

The project performs inference only. It does not train or fine-tune a model.

## Technologies Used

- **Python**: Application language.
- **Ultralytics YOLOv8**: Pretrained object detection model and inference API.
- **OpenCV (`cv2`)**: Webcam access, image display, and image saving.
- **YOLOv8n (`yolov8n.pt`)**: Bundled lightweight pretrained model. The `n` variant is optimized for speed and lower resource usage.
- **Operating system camera**: Default webcam accessed through OpenCV camera index `0`.

## Project Structure

```text
object_detection_project/
|-- detect.py                 # Main real-time detection script
|-- yolov8n.pt                # Pretrained YOLOv8 nano model
|-- test_images/              # Sample input images stored in the workspace
|   |-- img1.jpg
|   |-- img2.jpg
|   `-- img3.jpg
|-- saved_frames/             # Annotated frames saved during detection
|-- runs/detect/               # Ultralytics-generated prediction outputs
|-- .gitignore
`-- README.md
```

`test_images/` is not read by the current `detect.py`; the script currently uses the webcam as its input source.

## Requirements

- Python 3.8 or newer
- A working webcam
- Windows, macOS, or Linux
- Internet access during installation if the Python packages are not already installed
- Enough memory to load the YOLO model

A CPU can run the project, although inference will generally be faster with a compatible GPU and CUDA-enabled PyTorch installation.

## Setup

### 1. Open the project folder

```powershell
cd "c:\Users\Moulik Tiwari\OneDrive\Desktop\VIT\DEEP LEARNING\object_detection_project"
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

If PowerShell blocks activation, run the following once for the current user, then activate the environment again:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install ultralytics opencv-python
```

The model file is already included in the project, so no model download is required when `yolov8n.pt` is present.

## Run the Application

With the virtual environment activated, run:

```powershell
python detect.py
```

A window named `Real-Time Object Detection` will open. Point the webcam at objects supported by the pretrained model. Press **Q** while the display window is focused to stop the application.

## How It Works

The main implementation is in `detect.py`:

- `YOLO("yolov8n.pt")` loads the pretrained detector.
- `cv2.VideoCapture(0)` connects to the default webcam.
- `cap.read()` obtains one frame at a time.
- `model(frame)` runs YOLO inference on the frame.
- `results[0].plot()` creates a copy of the frame with detection boxes, class names, and confidence information.
- `cv2.imshow()` displays the annotated frame in real time.
- `len(results[0].boxes) > 0` checks whether any detections were returned.
- `cv2.imwrite()` saves detected frames as `saved_frames/frame_<number>.jpg`.
- `cap.release()` and `cv2.destroyAllWindows()` clean up camera and window resources when the loop ends.

The frame counter increases for every camera frame. Therefore, saved filenames represent processed frame numbers and may contain gaps when no object is detected.

## Output

During a run, detected frames are saved to:

```text
saved_frames/frame_0.jpg
saved_frames/frame_1.jpg
...
```

Each saved image contains the visual annotations produced by YOLOv8. Ultralytics may also create additional prediction artifacts under `runs/detect/` when its prediction utilities are used.

To start a fresh capture, remove or move the existing files in `saved_frames/` before running the script. The script will create the directory automatically if it does not exist.

## Configuration and Customization

### Use another camera

Change the camera index in `detect.py`:

```python
cap = cv2.VideoCapture(1)
```

Try `1` or another available index if the default webcam cannot be opened.

### Use a larger model

Replace the model filename with another compatible Ultralytics model, such as:

```python
model = YOLO("yolov8s.pt")
```

Larger models can improve accuracy but generally require more memory and processing time. If the replacement model is not already available locally, Ultralytics may download it when the script runs.

### Change the save location

Update the directory creation and output path in `detect.py` together. For example, replace `saved_frames` with another folder name in both places.

### Adjust detection behavior

The current script saves a frame when any box is returned. Confidence thresholds, class filtering, image size, and other inference options can be passed to the Ultralytics model call if more selective detection is needed.

## Troubleshooting

### Camera does not open

- Check that the webcam is connected and not being used by another application.
- Confirm that the operating system granted camera permission to Python or VS Code.
- Try a different camera index in `cv2.VideoCapture(...)`.

### `ModuleNotFoundError`

Activate the virtual environment and reinstall the packages:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install ultralytics opencv-python
```

### The display window is not responding

Make sure the display window is focused when pressing `Q`. OpenCV requires `cv2.waitKey()` to process window events, and the script calls it once per frame.

### Detection is slow

- Keep using `yolov8n.pt`, the smallest standard model in this project.
- Reduce camera resolution or inference image size if needed.
- Use a supported GPU and compatible CUDA/PyTorch setup.
- Close other applications using significant CPU or memory.

### No objects are detected

The model only recognizes the classes it was trained on. Improve lighting, move the object closer, and ensure it is visible in the camera frame. Detection confidence can also vary with object size and image quality.

## Limitations

- The current input source is only the default webcam.
- There is no command-line configuration or graphical settings panel.
- Frames are saved without a maximum count, so long sessions can consume substantial disk space.
- The project does not train a custom model or provide evaluation metrics.
- A saved frame can contain one or multiple detections, but only the annotated image is stored; detection metadata is not exported separately.

## License and Model Notice

This project code does not define a separate license. Review the Ultralytics and YOLOv8 model licensing and usage terms before distributing or deploying the project commercially.

import yaml

CFG_FILE = "/data/config.yaml"

config = {}
with open(CFG_FILE, "r") as f:
    config = yaml.safe_load(f)

# DEFAULT BASE DIRS
GENERAL_DISPLAY = config["GENERAL_DISPLAY"]
PYTHON_PATH = config["PYTHON_PATH"]
CONDA_ENV_NAME = config["CONDA_ENV_NAME"]
BIN_PATH = config["BIN_PATH"]

# LOG AND RESULTS CSV FILE
BASE_LOG_CSV_PATH = config["BASE_LOG_CSV_PATH"]
LOG_CSV_COLUMNS = config["LOG_CSV_COLUMNS"]
AXIS = config["AXIS"]

# DICOM -> NIFTI
BASE_DICOM_INPUT_DIR = config["BASE_DICOM_INPUT_DIR"]
BASE_NII_ORIGINAL_OUTPUT_DIR = config["BASE_NII_ORIGINAL_OUTPUT_DIR"]

# PHNN SEGMENTATION
PHNN_EXECUTABLE_PATH = config["PHNN_EXECUTABLE_PATH"]
BASE_SEGMENTED_OUTPUT_DIR = config["BASE_SEGMENTED_OUTPUT_DIR"]
PHNN_THRESHOLD = config["PHNN_THRESHOLD"]
PHNN_BATCH_SIZE = config["PHNN_BATCH_SIZE"]

# MITK
MITK_BACKGROUND_COLOR = config["MITK_BACKGROUND_COLOR"]
MITK_TRANSFER_FUNCTION_PATH = config["MITK_TRANSFER_FUNCTION_PATH"]

# DEFAULT VALUES FOR VIDEO CREATION
BASE_MITK_VIDEO_OUTPUT_DIR = config["BASE_MITK_VIDEO_OUTPUT_DIR"]
MITK_VIDEO_EXECUTABLE_PATH = config["MITK_VIDEO_EXECUTABLE_PATH"]
MITK_VIDEO_WIDTH = config["MITK_VIDEO_WIDTH"]
MITK_VIDEO_HEIGHT = config["MITK_VIDEO_HEIGHT"]
MITK_VIDEO_TIME = config["MITK_VIDEO_TIME"]
MITK_VIDEO_FPS = config["MITK_VIDEO_FPS"]

# DEFAULT VALUES FOR SLICES CREATION
BASE_MITK_CAMERA_SHOT_OUTPUT_DIR = config["BASE_MITK_CAMERA_SHOT_OUTPUT_DIR"]
MITK_CAMERA_SHOT_EXECUTABLE_PATH = config["MITK_CAMERA_SHOT_EXECUTABLE_PATH"]
MITK_CAMERA_SHOT_WIDTH = config["MITK_CAMERA_SHOT_WIDTH"]
MITK_CAMERA_SHOT_HEIGHT = config["MITK_CAMERA_SHOT_HEIGHT"]
MITK_CAMERA_SHOT_LENGTH = config["MITK_CAMERA_SHOT_LENGTH"]
MITK_CAMERA_SHOT_AXIS = config["MITK_CAMERA_SHOT_AXIS"]

# RESNET DEFAULT VALUES FOR LOAD AND EXECUTE MODEL FOR PREDICTIONS
PREDICTION_MODEL_PATH = config["PREDICTION_MODEL_PATH"]
PREDICTION_LEGEND_PATH = config["PREDICTION_LEGEND_PATH"]
PREDICTION_WIDTH = config["PREDICTION_WIDTH"]
PREDICTION_HEIGHT = config["PREDICTION_HEIGHT"]

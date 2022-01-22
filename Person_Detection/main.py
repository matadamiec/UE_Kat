import glob

from detection_service import run_detection

imagesToProcess = glob.glob('Samples/*.jpeg')
run_detection(imagesToProcess)

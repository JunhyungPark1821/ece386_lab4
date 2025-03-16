"""This is a benchmark for running Keras model.
Try to make this code as similar to litert_benchmark as possible,
for a fair comparison."""

# By: Junhyung Park and Rushaan Mahajan
# Date: 2/28/2025

"""This script loads a .keras model and continuously takes pictures with a webcam,
printing if the picture is of a cat or a dog."""

import cv2
import sys
from tensorflow.keras.saving import load_model  # type: ignore[import]
import tensorflow as tf
from io import BytesIO
import numpy as np


def convert_image_to_numpy(image) -> np.ndarray:
    """Converts an image from a webcam to a numpy array for model ingestion
    Args:
        image (cv2.VideoCapture): An image from a webcam feed
    Returns:
        np.ndarray: A numpy array representing the image"""
    resizedImage = cv2.resize(image, (150, 150))

    numpyArray = np.asarray(resizedImage)

    numpyArrayReshape = numpyArray.reshape(1, 150, 150, 3).astype(np.uint8)

    return numpyArrayReshape


# TODO: Function to conduct inference
def keras_inference(keras_model, imageArray) -> int:
    """Runs inference on a LiteRT SignatureRunner
    Args:
        runner (SignatureRunner): A LiteRT SignatureRunner
    Returns:
        int: cat or dog"""

    # Invoke inference
    prediction = keras_model.predict(imageArray)
    final_prediction = tf.where(prediction > 0.5, 1, 0)

    print(final_prediction)

    return final_prediction


def main():

    # Verify arguments
    if len(sys.argv) != 2:
        print("Usage: python litert.py <model_path.tflite>")
        exit(1)

    model_path = sys.argv[1]
    keras_model = load_model(model_path)

    # Init webcam
    webcam = cv2.VideoCapture(0)  # 0 is default camera index

    # TODO: Loop to take pictures and invoke inference. Should loop until Ctrl+C keyboard interrupt.
    for i in range(10):
        try:
            # Capture a frame
            ret, frame = webcam.read()

            if ret:
                # Convert BGR (OpenCV default) to RGB for TFLite
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert to a NumPy array
                img_array = convert_image_to_numpy(frame_rgb)
                print(
                    "Image shape:", img_array.shape
                )  # Ensure shape matches model input

                keras_inference(keras_model, img_array)

                # Preview the image
                # cv2.imshow("Captured Image", frame)
                # print("Press any key to exit.")
                # while True:
                #     # Window stays open until key press
                #     if cv2.waitKey(0):
                #         cv2.destroyAllWindows()
                #         break

            else:
                print("Failed to capture image.")

        except KeyboardInterrupt:
            break

    # Release the camera
    webcam.release()
    print("Program complete")


# Executes when script is called by name
if __name__ == "__main__":
    main()

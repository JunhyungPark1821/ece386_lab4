# By: Junhyung Park and Rushaan Mahajan
# Date: 2/28/2025

"""This script loads a .tflite model into LiteRT and continuously takes pictures with a webcam,
printing if the picture is of a cat or a dog."""

import cv2
from ai_edge_litert.interpreter import Interpreter, SignatureRunner
import sys
import numpy as np
import tensorflow as tf


def get_litert_runner(model_path: str) -> SignatureRunner:
    """Opens a .tflite model from path and returns a LiteRT SignatureRunner that can be called for inference
    Args:
        model_path (str): Path to a .tflite model
    Returns:
        SignatureRunner: An AI-Edge LiteRT runner that can be invoked for inference."""

    interpreter = Interpreter(model_path=model_path)
    # Allocate the model in memory. Should always be called before doing inference
    interpreter.allocate_tensors()
    print(f"Allocated LiteRT with signatures {interpreter.get_signature_list()}")

    # Create callable object that runs inference based on signatures
    # 'serving_default' is default... but in production should parse from signature
    return interpreter.get_signature_runner("serving_default")


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
def lite_inference(runner: SignatureRunner, imageArray) -> int:
    """Runs inference on a LiteRT SignatureRunner
    Args:
        runner (SignatureRunner): A LiteRT SignatureRunner
    Returns:
        int: cat or dog"""

    # Invoke inference
    output = runner(
        catdog_input=imageArray
    )  # Key matches top key from get_input_details()
    # Extract the result fom the batch returned
    result = output["output_0"][0][0]  # Key matches top key from get_output_details()

    final_prediction = tf.where(result > 0.5, 1, 0)

    print(final_prediction)

    return final_prediction


def main():

    # Verify arguments
    if len(sys.argv) != 2:
        print("Usage: python litert.py <model_path.tflite>")
        exit(1)

    # Create LiteRT SignatureRunner from model path given as argument
    model_path = sys.argv[1]
    runner = get_litert_runner(model_path)
    # Print input and output details of runner
    print(f"Input details:\n{runner.get_input_details()}")
    print(f"Output details:\n{runner.get_output_details()}")

    # Init webcam
    webcam = cv2.VideoCapture(0)  # 0 is default camera index

    # TODO: Loop to take pictures and invoke inference. Should loop until Ctrl+C keyboard interrupt.
    while True:
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

                lite_inference(runner, img_array)

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

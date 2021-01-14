def capture_image():
    # # Takes a picture using the webcam and saves it to disk in the images folder

    import cv2
    import numpy as np

    def draw_label(img, text, pos, bg_color):
        font_face = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.6
        color = (0, 0, 0)

        cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

    # setup the video capture source camera
    cap = cv2.VideoCapture(0)

    # read in a single frame from the camera
    while(True):
        ret,frame = cap.read()

        draw_label(frame, "Press 'a' to take picture or 'q' to close", (20,20), (255,0,0))

        cv2.imshow("video", frame)
    
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("a"):
            cv2.imwrite(r"C:\justins_files\Home\JFace\images\dlt.png", frame)
            break

    # When everything done, release the capture

    cv2.destroyAllWindows()

    cap.release()


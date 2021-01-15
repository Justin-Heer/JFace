def camera():
    # Takes either a picture or a video depending on the key input from the user

    import cv2

    def draw_label(img, text, pos, bg_color):
        # Void function for writing overlay text on camera window

        font_face = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.6
        color = (0, 0, 0)

        cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

    def take_picture():
        # takes in 1 new frame and takes picture, saves to file
        _, frame = cap.read()
        cv2.imshow("video", frame)
        cv2.imwrite(r"C:\\justins_files\\Home\\JFace\\media\\dlt.png", frame)

    def take_video():
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(r"C:\\justins_files\\Home\\JFace\\media\\output.avi", fourcc, 30.0,(1920,1080))

        while cap.isOpened():
            # takes in new frame
            _, frame = cap.read()

            # Resize frame to match webcam input
            frame = cv2.resize(frame, (1920,1080))

            # write to disk
            out.write(frame)

            #write text to window
            draw_label(frame, "Press 'q' to stop recording and close", (20,20), (255,0,0))

            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break


    # setup the video capture source camera
    try:
        cap = cv2.VideoCapture(0)
    except:
        print("Cannot find camera, maybe it isn't plugged in?")

    # read in a single frame from the camera
    while(True):
        # reads in a single frame
        _, frame = cap.read()
        # writes text to the frame
        draw_label(frame, "Press 'a' for picture, v for to start video recording, or 'q' to close", (20,20), (255,0,0))

        cv2.imshow("video", frame)
    
        key = cv2.waitKey(1)
        if key == ord("q"):
            # close camera
            print("closing camera")
            break

        elif key == ord("a"):
           take_picture()
           break

        elif key == ord("v"):
            take_video()
            break
    

    # When everything done, release the capture

    cv2.destroyAllWindows()

    cap.release()
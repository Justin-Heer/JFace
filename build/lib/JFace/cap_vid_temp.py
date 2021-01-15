import cv2 
# Initialize the video capture webcam instance
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('C:\justins_files\Home\JFace\media\\output.avi', fourcc, 30.0,(1920,1080))

# if/while video capture successfully opened the webcam
while cap.isOpened():
    # Get single frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Resize frame to match webcam input
    frame = cv2.resize(frame, (1920,1080))

    #show the current video frame
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    
    if key == ord("a"):
        while cap.isOpened():
            ret, frame = cap.read()
        
            frame = cv2.resize(frame, (1920,1080))
            # Resize frame to match webcam input
            frame = cv2.resize(frame, (1920,1080))
            out.write(frame)
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        break
    

# Close windows and release webcam and video writer
cap.release()
out.release()
cv2.destroyAllWindows()
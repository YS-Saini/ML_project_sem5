import cv2
import random
import os

def capture_random_snaps(video_path, output_folder, num_snaps=10):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Load the video
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Could not open video file.")
        return
    
    # Get video properties
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    duration = frame_count / fps  # Total duration of the video in seconds
    
    # Generate random times
    random_times = sorted(random.uniform(0, duration) for _ in range(num_snaps))
    
    for idx, time in enumerate(random_times):
        # Set the video to the corresponding frame
        video.set(cv2.CAP_PROP_POS_MSEC, time * 1000)  # Convert seconds to milliseconds
        
        success, frame = video.read()
        if success:
            # Save the frame
            output_path = os.path.join(output_folder, f"snap_{idx+1}.jpg")
            cv2.imwrite(output_path, frame)
            print(f"Snapshot saved: {output_path}")
        else:
            print(f"Warning: Unable to capture frame at {time:.2f} seconds.")
    
    video.release()
    print("Finished capturing snapshots.")

# Example usage
video_path = "D:\THAPAR\Sem_5\Machine_learning lab\ML_Project_ved.mov"  # Replace with your video file path
output_folder = "D:\THAPAR\Sem_5\Machine_learning lab\Clip_Snaper\snapshots"           # Replace with your desired folder path
capture_random_snaps(video_path, output_folder)

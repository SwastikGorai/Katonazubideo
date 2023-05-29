import os
from arguments import args as a
PATH = a.input_video

def is_directory_or_video(PATH):
    if os.path.isdir(PATH):
        vid_files =  list_video_files(PATH)
        selected_video = select_video(vid_files, PATH)
        return selected_video
        
    elif os.path.isfile(PATH):
        _, ext = os.path.splitext(PATH)
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.flv']
        if ext.lower() in video_extensions:
            print(f"Video file found {os.path.basename(PATH)})")
            selected_video = PATH
            return selected_video            
            
    return "Neither Directory nor Video"





def list_video_files(directory):
    video_files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            _, ext = os.path.splitext(file)
            video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.flv']
            if ext.lower() in video_extensions:
                video_files.append(file)
    return video_files




def select_video(video_files, directory):
    if not video_files:
        print("No video files found in the directory.")
        return None

    print("Select a video file:")
    for i, file in enumerate(video_files):
        print(f"{i+1}. {file}")

    while True:
        choice = input("Enter the number of the video file you want to select ( 'q' to quit): ")
        if choice.lower() == 'q':
            return None

        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(video_files):
                selected_video = os.path.join(directory, video_files[choice_index])
                return selected_video
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")


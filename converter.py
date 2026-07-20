import os
import sys
import subprocess

SUPPORTED_FORMATS = {
    ".mp3" : "audio",
    ".wav" : "audio",
    ".mp4" : "video",
    }

def get_route_ffmpeg():
    
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "ffmpeg.exe")


def convert(in_route, exit_format, output_folder = None):
    
    exit = os.path.splitext(in_route)[1].lower()
    
    if exit not in SUPPORTED_FORMATS:
        raise ValueError(f"Input Format ' {exit} ' Not Supported")
    
    filename = os.path.splitext(os.path.basename(in_route))[0]
    
    if output_folder:
        exit_route = os.path.join(output_folder, f"{filename}.{exit_format}")
    else:
        exit_route = os.path.splitext(in_route)[0] + f".{exit_format}"   
        
    ffmpeg_path = get_route_ffmpeg()
    
    command = [
        ffmpeg_path,
        "-y",
        "-i", in_route,
    ]
    
    input_type = SUPPORTED_FORMATS[exit]
    if input_type == "video":
        command.append("-vn")
    
    command.append(exit_route)
    
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        creationflags= subprocess.CREATE_NO_WINDOW
        
    )
    
    if result.returncode != 0:
        raise RuntimeError(f"Error of ffmpeg:\n{result.stderr} ")

    return exit_route

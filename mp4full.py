import os
import cv2

def calculate_total_duration(directory):
    total_duration = 0  # 合計再生時間を秒単位で初期化

    # 指定されたディレクトリ内のMP4ファイルを検索
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".mp4"):
                video_path = os.path.join(root, file)
                try:
                    video_capture = cv2.VideoCapture(video_path)
                    frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
                    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
                    duration = frames / fps
                    total_duration += duration
                except Exception as e:
                    print(f"エラー: {video_path} - {e}")
                finally:
                    video_capture.release()

    # 合計再生時間を分に変換
    total_duration_minutes = total_duration / 60

    return total_duration_minutes

if __name__ == "__main__":
    input_directory = r'C:\Users\n22010\Videos'  # MP4ファイルが格納されたディレクトリを指定

    total_duration_minutes = calculate_total_duration(input_directory)
    print(f"合計再生時間: {total_duration_minutes} 分")

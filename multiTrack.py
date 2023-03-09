import cv2
import threading
import import_pts


class VideoPlayer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    def play(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (1920,1080), cv2.INTER_AREA)
            cv2.imshow(self.video_path, frame)
            if cv2.waitKey(int(1000/self.fps)-5) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    print("ch")
    print(import_pts.import_json('D:/data/tracking/1.pts'))
    
    #local file
    video_list = ["D:/data/tracking/video/3082_210_270.mp4","D:/data/tracking/video/1st.mp4"]
    
    #RTSP mode
    # video_list = ['rtsp://admin:admin@10.82.5.129/3082_210_270.mp4']
    
    
    players = [VideoPlayer(video) for video in video_list]
    threads = [threading.Thread(target=player.play) for player in players]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


from flask import Flask, request, jsonify
import os

app = Flask(__name__)

VIDEO_STORE = "videos.json"
COMMENT_STORE = "comments.json"

@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files['video']
    video_name = video.filename
    video_path = os.path.join(os.getenv('VIDEO_UPLOAD()_PATH'), video_name)
    video.save(video_path)
    return jsonify({'message': 'Video uploaded successfully!', 'video_path': video_path})

@app.route('/videos', methods=['GET'])
def view_videos():
    videos_dir = os.getenv('VIDEO_UPLOAD_PATH')
    video_files = [video for video in os.listdir(videos_dir) if os.path.isfile(os.path.join(videos_dir, video))]
    return jsonify({'videos': video_files})

@app.route('/comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    video_id = data.get('video_id')
    comment = data.get('comment')
    try:
        with open(COMMENT_STORE, 'r+') as file:
            comments = json.load(file)
            if video_id in comments:
                comments[video_id].append(comment)
            else:
                comments[video_id] = [comment]
            file.seek(0)
            json.dump(comments, file)
    except FileNotFoundError:
        with open(COMMENT_STORE, 'w') as file:
            json.dump({video_id: [comment]}, file)
    return jsonify({'message': 'Comment added successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
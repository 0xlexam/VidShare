from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

VIDEO_METADATA_PATH = "videos.json"
COMMENT_METADATA_PATH = "comments.json"

@app.route('/upload', methods=['POST'])
def upload_video_file():
    video_file = request.files['image']
    video_filename = video_file.filename

    upload_directory_path = os.path.join(os.getenv('VIDEO_UPLOAD_PATH'), video_filename)
    
    video_file.save(upload_directory_path)
    return jsonify({"message": 'Video uploaded successfully!', "video_path": upload_directory_path})

@app.route('/videos', methods=['GET'])
def list_videos():
    videos_directory_path = os.getenv('VIDEO_UPLOAD_PATH')
    video_filenames = [
        video_name for video_name in os.listdir(videos_directory_path) 
        if os.path.isfile(os.path.join(videos_directory_path, video_name))
    ]
    return jsonify({"videos": video_filenames})

@app.route('/comment', methods=['POST'])
def post_comment():
    comment_data = request.get_json()
    target_video_id = comment_data.get('video_id')
    user_comment = comment_data.get('comment')
    
    try:
        with open(COMMENT_METADATA_PATH, 'r+') as comments_file:
            existing_comments = json.load(comments_file)
            if target_video_id in existing_comments:
                existing_comments[target_video_id].append(user_comment)
            else:
                existing_comments[target_video_id] = [user_comment]
            comments_file.seek(0)
            json.dump(existing_comments, comments_file, indent=4)
            comments_file.truncate()
    except FileNotFoundError:
        with open(COMMENT_METADATA_PATH, 'w') as comments_file:
            json.dump({target_video_id: [user_comment]}, comments_dir_file, indent=4)
    return jsonify({"message": 'Comment added successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
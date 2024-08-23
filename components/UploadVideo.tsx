import React, { useState } from 'react';

interface VideoUploadFormValues {
    title: string;
    description: string;
    videoFile: File | null;
}

const VideoUploadComponent: React.FC = () => {
    const [formValues, setFormValues] = useState<VideoUploadFormValues>({ title: '', description: '', videoFile: null });

    const handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value, files } = event.target;
        if (name === 'videoFile') {
            setFormValues(prevState => ({ ...prevState, videoFile: files ? files[0] : null }));
        } else {
            setFormValues(prevState => ({ ...prevState, [name]: value }));
        }
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append('title', formValues.title);
        formData.append('description', formValues.description);
        if (formValues.videoFile) formData.append('videoFile', formValues.videoFile);

        try {
            await fetch(`${process.env.REACT_APP_API_URL}/videos/upload`, {
                method: 'POST',
                body: formData,
            });
            alert('Video uploaded successfully');
        } catch (error) {
            console.error('Error uploading video:', error);
            alert('Error uploading video');
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="title">Title</label>
                    <input
                        type="text"
                        id="title"
                        name="title"
                        value={formValues.title}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label htmlFor="description">Description</label>
                    <textarea
                        id="description"
                        name="description"
                        value={formValues.description}
                        onChange={handleChange}
                    ></textarea>
                </div>
                <div>
                    <label htmlFor="videoFile">Video File</label>
                    <input
                        type="file"
                        id="videoFile"
                        name="videoFile"
                        onChange={handleChange}
                        accept="video/*"
                    />
                </div>
                <button type="submit">Upload Video</button>
            </form>
        </div>
    );
};

export default VideoUploadComponent;
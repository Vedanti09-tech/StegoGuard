import React, { useState } from 'react';
import { FilePond, registerPlugin } from 'react-filepond';
import 'filepond/dist/filepond.min.css';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css';

registerPlugin(FilePondPluginImagePreview);

const UploadPage = () => {
  const [files, setFiles] = useState([]);
  const [response, setResponse] = useState(null);

  const handleUpload = async (fieldName, file, metadata, load, error, progress, abort) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('http://localhost:5000/api/upload', {
        method: 'POST',
        body: formData
      });

      const result = await res.text(); // ✅ this is required
      if (res.ok) {
        setResponse(result);
        load(result); // ✅ FilePond needs load() to confirm upload
      } else {
        error("Upload failed");
        setResponse("Server error ❌");
      }
    } catch (err) {
      console.error(err);
      error("Upload error");
      setResponse("Server error ❌");
    }
  };

  return (
    <div className="p-6 max-w-lg mx-auto text-center">
      <h1 className="text-xl font-bold mb-4">Upload Image</h1>
      <FilePond
        files={files}
        onupdatefiles={setFiles}
        allowMultiple={false}
        server={{ process: handleUpload }}
        name="file"
        labelIdle='Drag & Drop your image or <span class="filepond--label-action">Browse</span>'
      />
      {response && <p className="mt-4 text-blue-600">{response}</p>}
    </div>
  );
};

export default UploadPage;

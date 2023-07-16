import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/",
});

export const uploadData = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await api.post("upload-data", formData);
    return response.data.message;
  } catch (error) {
    throw new Error("Error uploading data.");
  }
};

export const getData = async () => {
  try {
    const response = await api.get("get-data");
    return response.data;
  } catch (error) {
    throw new Error("Error fetching data.");
  }
};

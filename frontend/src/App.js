import React, { useState } from "react";
import { Button, Table } from "react-bootstrap";
import { uploadData, getData } from "./Api";

const App = () => {
  const [csvData, setCsvData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = async () => {
    try {
      const data = await getData();
      setCsvData(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    const file = e.target.files[0];

    setIsLoading(true);
    try {
      await uploadData(file);
      setIsLoading(false);
      alert("Data uploaded successfully!");
    } catch (error) {
      setIsLoading(false);
      console.error("Error uploading data:", error);
    }
  };

  return (
    <div className="container d-flex flex-column align-items-center mt-5">
      <h1>CSV Data Upload and Display</h1>
      <div>
        <input type="file" onChange={handleUpload} />
        {isLoading ? <span>Uploading...</span> : null}
      </div>
      <Button className="mt-3" onClick={fetchData}>
        Get Data
      </Button>
      {csvData.length > 0 && (
        <Table className="mt-3" striped bordered hover>
          <thead>
            <tr>
              <th>ID</th>
              <th>DateTime</th>
              <th>Close</th>
              <th>High</th>
              <th>Low</th>
              <th>Open</th>
              <th>Volume</th>
              <th>Instrument</th>
            </tr>
          </thead>
          <tbody>
            {csvData.map((row) => (
              <tr key={row.id}>
                <td>{row.id}</td>
                <td>{row.datetime}</td>
                <td>{row.close}</td>
                <td>{row.high}</td>
                <td>{row.low}</td>
                <td>{row.open}</td>
                <td>{row.volume}</td>
                <td>{row.instrument}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      )}
    </div>
  );
};

export default App;

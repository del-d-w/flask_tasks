import React, { useEffect } from "react";
import axios from "axios";
import jsPDF from "jspdf";

export default function App() {
  useEffect(() => {
    // Make an API request to fetch the data
    axios
      .get("https://jsonplaceholder.typicode.com/posts")
      .then((response) => {
        const data = response.data;

        // Generate PDF
        const doc = new jsPDF();
        doc.setFont("calibri", "normal");
        data.forEach((post, index) => {
          const text = `${index + 1}. ${post.title}\n${post.body}\n\n `;
          doc.text(text, 10, 10 + index * 40);
        });

        // Save the PDF file
        doc.save("api_data.pdf");
      })
      .catch((error) => {
        console.log("Error:", error);
      });
  }, []);

  return <div></div>;
}

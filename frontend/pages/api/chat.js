import axios from 'axios';

export default async function handler(req, res) {
   if (req.method === 'POST') {
      const { message } = req.body;

      try {
         // Send the user's message to the Flask API
         const response = await axios.post('http://localhost:5000/api/chat', { message });

         // Send the Flask bot response back to the frontend
         const botResponse = response.data.reply; // Get the reply from Flask

         res.status(200).json({ reply: botResponse });
      } catch (error) {
         console.error("Error communicating with the backend:", error);
         res.status(500).json({ message: 'Something went wrong' });
      }
   } else {
      res.status(405).json({ message: 'Method not allowed' });
   }
}

 


  
# 🤖 GenAIus KT Frontend UI

This repository contains the frontend code for **GenAIus KT**, a chatbot developed using **Next.js**. GenAIus KT serves as an onboarding buddy, offering a professional and user-friendly chat interface with support for light and dark themes.

## 🌟 Features

- **💬 Dynamic Chat Interface**: The chat window displays messages in real-time, with a smooth auto-scroll feature.
- **🌓 Theme Toggle**: Easily switch between light and dark modes with a single button.
- **📜 Persistent Chat History**: View past conversations by selecting from the chat history panel.
- **📱 Responsive Design**: Optimized for various screen sizes, maintaining a professional look and feel.

## 🚀 Getting Started

### ✅ Prerequisites

- 🛠 **Node.js** (v14 or higher)
- 📦 **npm** (v6 or higher)

### 🛠 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/GenAIus-KT-Frontend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GenAIus-KT-Frontend
   ```

3. Install the dependencies:

   ```bash
   npm install
   ```

### ▶️ Running the Application

To run the application locally:

```bash
npm run dev
```

The application will be available at [http://localhost:3000](http://localhost:3000) 🌐.

### 🔗 Connecting to the Backend

Ensure that your backend Flask API is running on [http://localhost:5000/api/chat](http://localhost:5000/api/chat) ⚙️. The frontend is configured to communicate with this endpoint for chatbot responses.

## 📂 Project Structure

- **📄 pages/**: Contains the main entry points for the application.
- **🧩 components/**: Contains the reusable UI components, such as the chatbot interface.
- **🖼 public/**: Contains static assets like images (e.g., `logo.png`).
- **🎨 styles/**: Contains global and component-specific styles.

## 🛠 Environment Variables

Make sure you have the necessary environment variables set up. For example, if using API keys or sensitive information, store them in a `.env` file 📂.

## 🛠 Technologies Used

- **⚛️ Next.js**: React framework for building fast and scalable web applications.
- **🔗 Axios**: For making HTTP requests to the backend.
- **🖌 Material-UI**: For UI components and icons.
- **🎨 CSS Modules**: For component-based styling.

## 🚀 Deployment

To deploy the frontend application:

1. Build the application:

   ```bash
   npm run build
   ```

2. Start the server:

   ```bash
   npm start
   ```

### 📝 Additional Notes

- Ensure the backend Flask server is running and accessible at the correct URL.
- Update the frontend code to match any backend URL changes 🔄.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details 📃.
```

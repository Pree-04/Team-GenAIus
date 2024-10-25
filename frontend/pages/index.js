// pages/index.js
import Head from 'next/head';
import Chatbot from '../components/Chatbot';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Gen AIus KT - Chatbot Interface</title>
        <meta name="description" content="Gen AIus KT - A professional chatbot interface" />
        {/* <link rel="icon" href="/favicon.ico" /> */}
      </Head>

      <main style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '1px' }}>
        
        <Chatbot />
      </main>

    </div>
  );
}

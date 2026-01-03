import Post from './components/Post';

function App() {
  return (
    <main>
      <Post author="Maximilian" body="React.js is awesome" />
      <Post author="Manuel"
        body="I love programming" />
    </main>
  );
}

export default App;
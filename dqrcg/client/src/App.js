import NavBar from "./components/Navbar";
import Home from "./components/Home";

function App() {
  return (
    <div className="App">
      <NavBar />
      <Home showForm="true" />
    </div>
  );
}

export default App;

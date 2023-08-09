import './style.css'
import { Browse } from './pages/Browse';
import { Main } from './pages/Main';
import { Resister } from './pages/Resister';
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";
import { Nav } from './Nav';
import 'bootstrap/dist/css/bootstrap.min.css';
function App() {
  return (
    <div className='App'>
      <Router>
        <Nav/>
        <Routes>
          <Route path='/browse' element={<Browse/>}/>
          <Route path='/resister' element={<Resister/>}/>
          <Route path='/' element={<Main/>}/>
          <Route path='*' element={<Browse/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;

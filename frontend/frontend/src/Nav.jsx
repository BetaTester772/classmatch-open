import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

export function Nav() {
  return (
    <Container>
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand href="/browse" id='navbrowse'>조회하기</Navbar.Brand>
          <Navbar.Brand href="/resister" id='navresister'>등록하기</Navbar.Brand>
        </Container>
      </Navbar>
    </Container>
  );
}
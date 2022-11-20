import "./Notification.css";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

export default function Notification(props) {
  const handleClose = () => props.setIsOpen(false);

  return (
    <>
      <Modal show={props.show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title> Done!</Modal.Title>
        </Modal.Header>
        <Modal.Body>{props.msg}</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

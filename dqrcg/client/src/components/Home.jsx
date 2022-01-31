import React ,{useState} from 'react';
import { Form , Button, Alert , Image} from 'react-bootstrap';

import axios from "axios";

const baseURL = "http://127.0.0.1:5000/api/qrcode";

export default function Home(props) {


    
    const [Data, setData] = useState(0);
    const [urlValue, setUrlValue] = useState("");
    const [show, setShow] = useState(false);
    const [errData, seterrData] = useState("");
    const [showForm, setshowForm] = useState(props.showForm);

    const onClickButton = (event) =>{
        event.preventDefault();

        createQR();
        
        // custom form handling here
      }

    const handleOnChange = (e) => {
      setUrlValue(e.target.value);
      setShow(false);
    }
      function createQR() {
        axios
          .post(baseURL, {
            url: urlValue,
          })
          .then((res) => {
            setData(res.data);
            setShow(true);
            seterrData("Your url is "+res.data.dynamicurl);
            setshowForm(false);
            setUrlValue("");
          }).catch((err) =>{
            seterrData(err.response.data.error);
            setShow(true);

          });
      }

  return (
    <>
    <br />
    
    { showForm && ( <div>
      <Alert variant='danger' show={ show } >{errData}</Alert>
    <Form>
    <Form.Group className="mb-3" controlId="formBasicEmail">
    <Form.Control  className="w-25" 
        value={urlValue}
        onChange={handleOnChange}
        type="url" placeholder="Enter url" />

  </Form.Group>
    <Button variant="primary" type="submit"  onClick={onClickButton}>
      Submit
    </Button>
      </Form>
      </div>
    )
}

 { !showForm && ( <div>
 <Alert variant='success' show={ show } >{errData}</Alert>
  
  <Button variant="primary"   onClick={(e) => {setshowForm(true); setShow(false) }}>Home</Button>
  <h3>Below is your generate qr code</h3>
 <Image src= {Data.qrimage} rounded thumbnail={true} />
<br />
 
 </div>
 )}



    </>
  )
}

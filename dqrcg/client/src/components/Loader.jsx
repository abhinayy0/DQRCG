import React from "react";
import loading from "./not_avail.png";
import { Image } from "react-bootstrap";
function ShowDetail() {
  return (
    <div className="text-center mt-5">
      <Image src={loading} rounded />
    </div>
  );
}

export default ShowDetail;

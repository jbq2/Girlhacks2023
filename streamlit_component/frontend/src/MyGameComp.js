import React, { useEffect, useRef } from "react";
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";

const MyGameComponent = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    let circles = []
    Streamlit.setFrameHeight()
    
    function make_base() {
    let base_image = new Image();
    base_image.src = 'https://cdn.discordapp.com/attachments/1153737878099218473/1155511935404617728/Untitled.jpg';
    base_image.onload = function(){
      ctx.drawImage(base_image, 0, 0, canvas.width, canvas.height);
      }
    }

      function getMousePosition(canvas, event) {
          let rect = canvas.getBoundingClientRect();
          let x = event.clientX - rect.left;
          let y = event.clientY - rect.top;
          return {x: x, y: y};
      }

      function drawCircle(x, y, radius) {
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI);
    ctx.stroke(); 
      }

      function addCircle(x, y, radius) {
        circles.push({x: x, y: y, r: radius});
        drawCircle(x, y, radius);
      }

      function circleCheck(circle, point) {
        let dist = Math.sqrt( Math.pow(circle.x - point.x, 2) + Math.pow(circle.y - point.y, 2) );
        if (dist<= circle.r) {
          return true;
        }
      }

      const initialTime = new Date();
      const sI = initialTime.getSeconds();
      const mI = initialTime.getMinutes();
      const hI = initialTime.getHours();
      console.log(`${hI}:${mI}:${sI}`);

      for (let i = 0; i < 1; i++) {
        addCircle(Math.random() *550 + 20, Math.random() * 550 + 20, 100);
      }

    make_base();
    canvas.addEventListener("mousedown", function (e) {
      let point = getMousePosition(canvas, e);
      for (let i = 0; i < circles.length; i++) {
        let circle = circles[i];
        if (circleCheck(circle, point)) {
          circles.splice(i, 1);
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          if (circles.length == 0) {
          const endTime = new Date();
          const sE = endTime.getSeconds();
          const mE = endTime.getMinutes();
          const hE = endTime.getHours();
          let sT;
          let mT;
          let hT;

          if (sE - sI < 10) {
            sT = "0" + (sE - sI).toString();
          }
          else {
            sT = (sE - sI);
          }
          if (mE - mI < 10) {
            mT = "0" + (mE - mI).toString();
          }
          else {
            mT = (mE - mI);
          }
          if (hE - hI < 10) {
            hT = "0" + (hE - hI).toString();
          }
          else {
            hT = (hE - hI);
          }

          const time = `${hT}:${mT}:${sT}`
          Streamlit.setComponentValue(time);
          ctx.fillStyle = '#000000';
          ctx.font = '24px Consolas';
          ctx.textAlign = 'center';
          ctx.fillText('You have found all the aliens!', canvas.width / 2, canvas.height / 4);
          ctx.font = '18px Consolas';
          ctx.fillText(`Time: ${time}`, canvas.width / 2, canvas.height / 3);
          ctx.font = '14px Consolas';
          }
          else {
            make_base()
            for (let k = 0; k < circles.length; k++) {
              let newCircle = circles[k];
              drawCircle(newCircle.x, newCircle.y, newCircle.r);
            }
          }
          break;
        }
      }
    });
      return () => {
      canvas.removeEventListener("mousedown");
    }
  }, []);

  return (
    <canvas
      ref={canvasRef}
      id="canvas"
      width="600"
      height="600"
      style={{ backgroundColor: "green" }}
    ></canvas>
  );
};

export default withStreamlitConnection(MyGameComponent);
import React, { useEffect, useRef } from "react";
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";

const MyComponent = ({ args }) => {
  const canvasRef = useRef(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    canvas.width = 600;
    canvas.height = 600;
    const image = new Image();
    image.src = args.imageSrc;
    Streamlit.setFrameHeight()
    let aliens = [];

    function onRender(event) {
      console.log("render event");
      make_base();
      Streamlit.setFrameHeight()
    }

    function make_base() {
      let base_image = new Image();
      base_image.src = `data:image/png;base64,${args.baseImageSrc}`;
      base_image.onload = function () {
        ctx.drawImage(base_image, 0, 0, canvas.width, canvas.height);
        for (let k = 0; k < aliens.length; k++) {
          let newAlien = aliens[k];
          ctx.drawImage(image, newAlien.x - newAlien.s / 2, newAlien.y - newAlien.s / 2, newAlien.s, newAlien.s);
        }
      };
    }

    make_base();

    function getMousePosition(canvas, event) {
      let rect = canvas.getBoundingClientRect();
      let x = event.clientX - rect.left;
      let y = event.clientY - rect.top;
      return { x: x, y: y };
    }

    function addAlien(x, y, size) {
      aliens.push({ x: x, y: y, s: size });
      ctx.drawImage(image, x - size / 2, y - size / 2, size, size);
    }

    function alienCheck(alien, point) {
      let dist = Math.sqrt(Math.pow(alien.x - point.x, 2) + Math.pow(alien.y - point.y, 2));
      return dist <= alien.s / 2;
    }

    canvas.addEventListener("contextmenu", (event) => {
      event.preventDefault();
    });

    Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)

    canvas.addEventListener("mousedown", (e) => {
      const point = getMousePosition(canvas, e);
      if (e.button === 0) {
        addAlien(point.x, point.y, 50);
        Streamlit.setComponentValue(aliens);
      } else if (e.button === 2) {
        for (let i = 0; i < aliens.length; i++) {
          let alien = aliens[i];
          if (alienCheck(alien, point)) {
            aliens.splice(i, 1);
            Streamlit.setComponentValue(aliens);
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            make_base();
          }
        }
      }
    });

    return () => {
      canvas.removeEventListener("mousedown");
    }
  }, [args.imageSrc, args.baseImageSrc]);

  return (
    <canvas
      ref={canvasRef}
      id="canvas"
      width="600"
      height="600"
      style={{ backgroundColor: "white" }}
    ></canvas>
  );
};

export default withStreamlitConnection(MyComponent);
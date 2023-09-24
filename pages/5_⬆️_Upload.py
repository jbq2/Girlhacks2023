import streamlit as st
import pandas as pd
import sys
from io import StringIO
from pymongo import MongoClient
import base64
sys.path.append('..')
from mongo.dbconfig import ImagesDao
import streamlit.components.v1 as components


# connect to mongodb
users_dao = ImagesDao()

uploaded_file = st.file_uploader("Choose an image", type=["png","jpg"])

if uploaded_file is not None:
    # Display the uploaded image as HTML
    # Read the image file as bytes
    image_bytes = uploaded_file.read()
    # Encode the image bytes as base64
    image_base64 = base64.b64encode(image_bytes).decode()
    # st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="Uploaded Image">', unsafe_allow_html=True)

    html = f"""
    <html>
        <body>
            <canvas id="canvas" width="600" height="600"
                style="background-color: green">
            </canvas>
          
            <script type="text/javascript">
                const canvas = document.getElementById("canvas");
                const ctx = canvas.getContext("2d");
                let circles = []

                function make_base() {{
                  base_image = new Image();
                  base_image.src = 'data:image/png;base64,{image_base64}';
                  base_image.onload = function(){{
                    ctx.drawImage(base_image, 0, 0, canvas.width, canvas.height);
                  }}
                }}

                function getMousePosition(canvas, event) {{
                    let rect = canvas.getBoundingClientRect();
                    let x = event.clientX - rect.left;
                    let y = event.clientY - rect.top;
                    return {{x: x, y: y}};
                }}

                function drawCircle(x, y, radius) {{
                    ctx.beginPath();
                    ctx.arc(x, y, radius, 0, 2 * Math.PI);
                    ctx.stroke(); 
                }}

                function addCircle(x, y, radius) {{
                    circles.push({{x: x, y: y, r: radius}});
                    drawCircle(x, y, radius);
                }}

                function circleCheck(circle, point) {{
                    let dist = Math.sqrt( Math.pow(circle.x - point.x, 2) + Math.pow(circle.y - point.y, 2) );
                    if (dist<= circle.r) {{
                        return true;
                    }}
                }}

                const initialTime = new Date();
                const sI = initialTime.getSeconds();
                const mI = initialTime.getMinutes();
                const hI = initialTime.getHours();
                console.log(`${{hI}}:${{mI}}:${{sI}}`);

                make_base();
                const image = new Image();
                image.src = "https://cdn.discordapp.com/attachments/1153737878099218473/1155351824736456785/alien.png"
                canvas.addEventListener("mousedown", function(e)
                {{
                    point = getMousePosition(canvas, e);
                    ctx.drawImage(image, point.x - 25, point.y - 25, 50, 50);

                }});
            </script>
        </body>
    </html>
    """
    components.html(html, height=600)
submit_button = st.button("Submit")


if submit_button:
    if uploaded_file is not None:
        # convert to Base64
        bytes_data = uploaded_file.getvalue()
        image_base64 = base64.b64encode(bytes_data).decode()

        # insert into mongo
        image_data = {
            "username": "testname",
            "img_bson": image_base64
        }

        try:
            users_dao.insert_one(image_data)
            st.success(f'Successfully Uploaded: {uploaded_file.name}')
        except:
            st.error(f'Failed Upload: {uploaded_file.name}')

    else:
        st.warning("Please upload a file before submitting.")
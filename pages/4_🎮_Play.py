import streamlit as st
import streamlit.components.v1 as components
from st_pages import Page, show_pages, add_page_title

st.markdown("# Where's My Alien?!")

components.html(
    """
    <html>
<body>
    <canvas id="canvas" width="600" height="600"
        style="background-color: green">
    </canvas>
  
    <script type="text/javascript">
    	const canvas = document.getElementById("canvas");
    	const ctx = canvas.getContext("2d");
    	let circles = []

    	function make_base() {
		  base_image = new Image();
		  base_image.src = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFRgVFhUZGBUYGBocGhwaHBgcHBwaGhoaHBoYGhwcIS4lHR4rHxgZJjgmKy8xNTU1HCU7QDs0Py40NTEBDAwMEA8QHhISHjQrJCs0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NP/AABEIAKgBLAMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAACAwABBAUGB//EADYQAAIBAwMCBQMDBAEEAwEAAAERIQACMQNBURJhBHGBkaEiwfAFsdETMuHxFEJSYoIGkrIV/8QAGQEAAwEBAQAAAAAAAAAAAAAAAAECAwQF/8QAIxEAAwEAAwEAAgMAAwAAAAAAAAECEQMhMRJBUQQiYRMUMv/aAAwDAQACEQMRAD8A+PG51DcSZ/FipHlj/Jq0J+P81oJBBIsTCP2zAlucDmlU2w+WDl/beh6cliPnyoAPS6WGCZD3HT5Agv1HpS6i4zV3XFdOwJKWCUD/APkUwDNzySwABvjZ7AB+yoQN+6TmgqwOxnFLQCt5RNoTX87Ops3uYljvhb/FFppGdjBYBwAluGTMfTvilqmBVN07Qbl9RH1GAGgCWQ4wzMB0oCjsifyYNLsCumju1bjBJURt9IVsdhFCbqqqAu0OtVgklATgYHYdqRp4SZJCLxlhbuPam2FVrGEsK7TBNxgboA4crKA7mpcaHVzR2mE4KfdYdWv8Ey7LHLnYKT9gM+2N6htUf486d4e60XDqBNu6yu1abdLqBhrPYYZ4kj3p4C7Rh6cfn5itPh71TDoj2q7dEXXAW9hJGd5hB1NaipR2NAgoXCtd+lZNqRHrQeG0QbXxVf02Qs4VaRLNnJz/AB3h2hbnEoASYBJxu4yfOuNf12nEYjed/wA2r2P9K0iRNBqeFsWAadcdE1xHlrbGCRnikHQJfG/fde4r0f8AQs6kQAe3+KHxX6cQHZIz/utZ4PqdZzU3Lw8pdpTQ3Cutf4K8v6aRf4O5Lpu6pPbpAePeua+PPC02c82hZl4ULlv4VS7/ALgQGT9I6mARydpIy6ffoEB/y9p+fg1nuFYVJSYFoCLbhJLMv0dARWnT1LrS7SQf8LG8Ej1oScwGS3hZgKAC+NhUuR6K6yQAygSQNgSmfge1CRRm2pZebS7SiiPcEH4NTmAaNDxJti5kKOePbNbbLwQ3XJL3bHNCq0XI0JrQwas3Qo5wH75XarO0vH8qoWWe8nuWR7o+xqBgVKsH5ogCVapJHbKWYAoAqw0Wq2yEwNkwk+7Wd6G64kzn0+1USKAKtNMt+pWwJyUM8k/ehuIJgIcZ+aIWfST7jgQj6kkelGgLdGbgSyIYYERuBlUFSgAzewBMPynioaG+8lMtAAeQwKsGhATrKUJvAbxnK7VBQmjRCJcyDMzkHeRQgCsKIhraR+008gkAqIDSEARARKXeazm5lmSck7mnae842mZAQ9JnitY9Ewr5oQSDTBZR3aZNzLJJyZJJ3mtnLI1BWal1xmR1dRBJk7s5nmtOhcq16fhLRaHmqv0gBirS/Y8EXgOCw/L1rVooGsttwwYzifLfmis8UQQOJDRHsYpUt7HNYz0mhrC2yAhdIZZW1Xp61twuKA7bfNcfR8QWAClsTjfPmzWvw2objeXJb8+a34ejX71msfqAwgCO2cye+KZ/yubPauFqa/Sa6X6d4gXRyKp030VF68Nd9tl5BRdbBdZYEbSexgI703wWnZaD1Q/esnj9SwMWmtPtxOfsLhbrNFmroEFheYfyKRreG8PfwewP81yNe4qD6z+f7rEfEl5dZzSr1GVv5/J0PH/pVn/SV51xNb9IvMCRa/nNdXwvjiT0XiPeulZo2ooqlXDL7RP1p5DV8KLROfz2rKbbdxNeh/UvAXZCIkx/PpXndbTuBrmqfl5gjNqihuvPU924QnMAQPStN9qkIkggggwwn5ywqV/RATug5UkHggkcjt3g1zXLTKTBOo5Z6yS7nkETs3lly6SqgowfOsxlmiLDEHnB9u45HeruAQiZZeeI2U0JtSn/ABJCPs/WqwNKXfbv7edToKe2P8+Uj3o287BQAPfnzqul/m/AFGALqyJy/f71KJBAuS2OAEp7z8UgKFu8R3Dl7ZNWh/HnHtDqdIXfhbSy35bURtgS4mMFmO8I+tCGKVXRG38+1QRn5ftFNCZSpl9oDTI2JCK7hle5oeTA7PvgPNG+H+cVSwkWLKho9I3MdL6hIWQgyR5AE1RthsJrPG6yu9HQxYrX4a5kOk6oIuPUEdwhb8AACi0zxV8bxirs6t1g2pugACDkh7BfO+ay+HYB4jbjg+pjHsK0ad4aJQJk8d4ru+k14ZJdmvVvZOJmEg0do7Lb0oNa+FxRaVo5YnHxnZ1m8TLkRtM+VTU6tRf1gi0G4oSSUKaLDcMWgDqMekHJH9wA2+TStGyZxuuKbRMfsimM0NG647k5KZ966f6dY7j0yD/Fc+y2Fua6v6VZ0gnefTauiI7THNNeGTxmgTdjemeE8ObS8TWr+uGjJJroaOiDabhIBR80K3iJb6CvpL6OX43x0m0Hs65Or4u4Ez8v/dM/WLDZeP8AtP59qx2o7485xH5xXm/yFU2zabdSh/8Ay7iIDJhbvtSPDa/XclJNL19S0A+UdpE9+PWsNmoG936Lf7VlHI0ybnTvHDBpvhvG3WjLGMj3Vcr/AJMKqtv3rrrkWdGMy0zsamr9JDnNcy4N4jnedqb4ckjNBqXphVD8TLfbMWqnWbV6Vv1Psl+7pviLiGNiQcDZ753MfxWcCuXkr8FTIBGZ/g1Wr0uGoynifl0ZNS4kqTAQzAGw7Vzs0NH9E8h9yv3qhoE4USTgDzP461aoZxV2aTghQTx/0sZ9POun4M9MACJEHZ+RyKIWgSefWn3adu7HcAH4j96qzStP9xIA4yZEBwI37b4qPkemYbwC+dpBY7x80PTHePaXPt70aRW2z470Y02g0STkgWpRJ9fip+R6KF5ScNrZhgH5PvTLr3aA8MAcDMHzJj+aCy7pIuDYIPGP2qWbBruWh3Kn2pYGgXg0aNpBB2BBjcIwCd2PlCobagto+Q0qyz4/kD7ijvsQwWZey8lzu6G41XUafgihY+MEyQMB779t6lsEEZGKYQIy1Pmzjsl81dtjwvuWzj82o+R6I6a3+HsZ6iZXHAjHlWeyytFjtIJeHBRII52YNaROPWS2a7r9tqBj18oSL9cVntZk02y8b4l9+w/N66F+2R/hp0r8DqAfqs5Hp+1TplH84rJYXn/VaLLbgHkc+qrSWvRNGvT8Mx1f9LAcZLI/Y1ov0rBaD1B4Q6mcnqO3b0xWK3XX9pLGDg5ghYON6AaprZVKIcs0kny396bZ4jprLbeCzuE0FaBhlYlDG9BfqBUnfRULGdHTPUSa7P6MTbf0nF8V53wfinAzW+z9Q6SOxFVw2kzW/wDybv1nwtpfIYkA9sGvJ6+h0xaZnfaFHv717Xx93WBqWSLhI4O7rg+J8LbdiDwa0/kcKvtemXHypenn9fTuEdTBROU1vyQyPegtYBCgqJyMHOZIn/uNdn/+cTg1VvgQDLPKiN5rh/61Ls0rklnI6Cgdj9q06dsI4p1/h1tQHTO1J8TRKpGrwxFoI9oGSsniPx0jxJ3jPrH2n4phsQFBfbBOw8t8RvVVL+UgVLRJtBFI19AZtCHDfyq03WgO1grcSPQ1V16tMD2ftXHXpuvDk3FUp07WE5fv7UtVi0LTv26YTqxeEUglG5e4/N6z/wBQ9J7IPZlofB9qLTsJD/Fz5fwa7f8AEQL1LSTTtHwxPeD8j/yGxP8AGxplqAqv+Vai31sIsJS2E3hTzSxIAL/DEAg2gvciQtwdqwX29JDR5H1bHBxnsfauh/zHvWbW0xcWDUuU/AbMV1mSkGBnnzL2NCBW/U0rRbg9UssLZIKN6x3XYEQFHmSzyZ+BWbnBlghJS8/bP23zUv1CY2iBAYCa579zQXXP0C2/DQj89M0tAu5QnifNnHAS+avrZJgMtCBloDiqNUqWAax0XFogG4npt2GwBLfqNu8dD9F/TzqXi0BplboWmuVpahHHsK9j/wDEP/k13hta022WXO24Em0Y6SUCAC3FWmDPMX6RAAIRnlnz8vvVWWDzz22g10f1T9Sv1LrtS62xXXHFloDyoHBFYL9XAKEydh3j7VtqIaDuswKg0hzSbtRk0I1CMVVUhSh/QB7R58ZimaV9uLvTzf8ADrFdqk0NlxJAGSUJAz3MCs55HLLcpnUv8Mci4I0MgN/UCFD5mfSO9Z7byjKutM2mDwc7spZycA1duoQGVnmY7PEjPHnW/wBy/CFLD6UJT5mE4/OKTdfI3nBaPYragv8AEsgMBnJaHcqVSbNWs65Z3ENSzqaGi3cAiyYwilaBsp9+1Hf1BgS4+Qd+4FZ9LxatXNMu8SbuAOBW8uc6FWnV8L+pHTtVOu/UbLx9Vg9IrgnxApJ8SXJUcdmI7x71q/5GdaZLjPR2alhi1jdeTmOzq7rgQ1HPkn+49689oeNMTgsdjE/A9q3DX6ibjdJZPcmTVTzqgcYbvEaTRtYMEFywcjjFZRoogHc7kD3Jx5mm6Pi7TBDp919t3DVaNRXafZHaMOsImsxPIYHdelO8VeXyKz3kILP7dvzmuey0JFnff186vxF6Co7mvIdhv85rBr6hw4ZOznv6VycqSWnRFCxY2ykCdn2ABIbJAjAZ2pNaLtQI2iR1AghqAQ0Q5Y48qCuXNLNtlnUlnuQPk4osHIKY5HmPeKrQvFHq2AP48+/ITrt+etMd/AF2p9JncRMiWX6D3rH1I/7jv+c1pBqtXScisbXfRaM911afCX54MbcgxxjNJOieK3WeHVoxawd2SQeBjIExBqV0x4Vq3fSVvWC68wNgWAQN03zgVvv0ySAJKwAWJxj1jmsGqE6dC/IF1/YCSYHO3l2qrrR0i4HJII4QtnLlnZR7ENL+7qg2iAWC2AktpYiqt04JiO4foN6y9KK07iCCCiCweCMGivtIkgzudygf2uB9RQgBFvELljPZP1VV1eXGBy8+uaNwQ24AQ2Xsjak31A57L1pmlqIg9j8gisop9oiqlgGAD0uFkyXOSHsCkFiq1BNHpTFEiHKeRypnma2U6tRDYu8B/S1s0D6qhvNMssfycgYD38sb1NUILpLKIMtIwBuDFTXSHPYgM7FDJ2Dw6oqmWWRWa41k3heDLrqK+83IAAYHGAmWez9aVRKlrYgb78gMWkgolyAZPufeq6qK0W7kjGA4cnI29+1S5iCYymx9QBcQ0vbtU+FDbmPpMEfm1LGoarqJnvMbnyxvVdZRDKORsVh81X28FgV1xT2ayNltneqOoSEyspw0n7UuoDU/TYxtlxJE8BlwMbTitnh7wDMgcFE+RX71i005JA7Bn0DD9606AEFyiSDACwi5YraK+SWtNPWQqfb4nD2+fOudr6lXo3HNbRyvcJqVh2Lrxdb3rPZZNBbf9MQXxl8l7Ljc0y27EtiYxOO/PrXT9b6ZYTXsA8/hQvv8Vm1PDC8km4WkngqTP9oj2rfd9TJk5dZ9ezpieoMEcEGouE/SprDnjwZDlfSSP/KUu25nYU6zwJIdabbmUvXH70brFcKG7MOhKABJJ93gAVuvtHTPHltHztXP0blLIISXLHtD+K1X3/NXxv8AqFeiQchD2D9Dkela9DSN0LNZZdafDm7kDOX7RWbnWXLwP+mnJ7IjP8Zo7bDdgY/YZozf3HoqlniAC061nhn8k1yfozHTPU8Csev4e7jD9sk16H/kWXj6rQxuM1zfEX2g/S93P5tVXwznpmrbZyr9C63IIkicsZBGRQhiujqkE3HlnA5e0D0rHqDIYEcZnAKjnbFc1QpNFWme6hdEaK2wb8HBU7bY7Vi5b8LBtpoNWLZDLAUMiMkA7ZNVIlQWAwxhEAkZAI7hg8VSloNCs5o7ixu3xCXPNLBptt0ImM9nzVzX4E1oeie234aXfcqZbrgT/dCmYSCfAxxWW64Ey+3nSoa6DOoNsLc9p/1+9ZbhP5vIp1lu4M1V2l0lHgH0IBGOxFZtNj0l2mg2CIDHJDUzsdtqu5hO0B2g7y5F2c7fapdKgBDvMmSznaFigsJEj7fek1ggNS0gyEaZZb9P/TB5+osYTkRxv3FUQKAUmux6GLdueSAPUml0dw+P8COc0ApMZARvwcRKjbDVX/Uu6upnqbbltt8veiuWAiASikT/AIjHc1RvKThtdyE/gUkgKEmr61UtVUAyoDO+PM9qrwQxgpDaZbLM9oQXatGmUPz8NZ7QBcQCw4OH3W1ar7GGAelpr1AOzW1bcfmkUP07mKLUKFZ7NTpG2DkA589+9VdqXYMdjXR9rCMH6eoaf0EjGfKFSfDBngGfNNdipnua7ehp2rIrbil36TTUmDT0QM1NS2a232C18Hb9kfOsGprB1q0p6IT05Fl1aDIBrni+uhoXQSC0WGBzuDHpXmTZ0/Jdt6qv6hJAtDJIAGZ2C3odS7jNBp2G4rnuAPcxWipvpCawZbeau69GC/RbTD5orrenOxxBnvzis2reGcemPSqb+V2SuzV/WmGnudtp39hQalyJexmeMyP3pWlIZwSQD3CJHyPenanhSA4R4IOwP3FS+RtDUme+88uBz7TxirtIOf2AxAXML8mquJwXEDtvHufemdIRIEmAA0MfU3mDBiT2qO2xi2Q0UwiuDkeVCwO4eMPtTTqE2gFEWggRjq3YyXMus9JgFdqL+1iCCyDlgqAoNV1z1ICWAvp8kdqoiOEc+0EuEn6+0BMBlDHAeVxUd6UGTVXBzsENskE4ycGfLkVV2M+k95/OaC2m/wBCQ4ICppAOTd0mLumDli0sLNoO/viC2iFyQ6ukHdnEgsWzzHB706fQ0hYsPNN1L3bZagrQRADLJJJIDOd2qTZdddFtpPYBn4q7L3j83qFhQQG1Lu6rSQyDNpR9xGRU1DDFw2iXv2Ww/wDsO6AahXovRte9DrehYXfeTJLPcswAB8IelTqewCAEBY3PehM0dtyED6gWGiFLBtIL29sVDGVcepAAQNkHJM8mfYAbUupZayByVJAHqTA86gpaBepeSWc+g/ag6jV3CisvISUFiLTMZYkQIMZ5NICWiDBceQGC/UirJoRkM8SXG3nUu833DnvNUhNBh7cr14p1usQCPwf5oL7t+om52ogwhbAw2EB6Uu67PLbl7v3fx51SpoM0fbdyDIjbyMiRRWkRl7z324hVn/qQBw/P1plhKJRUA8TIB9virmtFhusvJdxLL5llnHv71o0fFdNY7OoMXAg2wi2Oy2l0m7VRNbzy/JLnTuWeIf0t2uP5W1K1NMOsGlqVsv1QCizwUQxsVXSuRNdmXznhxhYNzLG20s+kR37Vq8NuBImee9Zbh5veI2Uud9vfbZ4eAY2jzY/z715knSVeEKAXKmag83tPcZiYfH2pRtQddE9Izr0s3A5anCeIz3VZ9QdgPLyAz6P1NM1GCiJBIIMEEFEEbGr0w8wAmeASA1vmpf8AYF0LNpADQJkf9yQT4BBY8jTrNcigv6Q0j7hTnzQ+azXk1nvyUde/UF9soXAQgmySZG8/irJYUwSPmfKF70vw+rW6zS6hFtpMyW5GMqKpU9BrRWkAcgnOOdvSl6uniB5zPnK9q2W+AvtmKz6uoMGtv60uyGmjGLJp2ieki4JgsOZ2NVfrywSD2Q2W3aobjebrkIDKQCgQPUQKyxJlei7rauyyhZbBRpzLWTO78y96lsaQdxAsU9TZwoaAh7zPpFZV1YEhkljAA2Pr5vtTLrhzS7r9oWMB5eU29+IxU0NCqZdc8gegWAAMRtnJZJdCTR6d19p+lgoXYkAfULgdsNio8GBbazldy/sKpft+P2qgaOwgTBREFzk7bQjO4oAGuh+ifpGt4i/o07Lr7um65AHa0msQ1HBJRT87QRb+69a2fpf6hfo39dl91h6bgwVm0hfNC9Aya+hdYSLrSCMsVBbbcYPTwLieOUpPPPrVa9x6i22W23u3vVahCtA2Elbk47gBeroAsWDqRPSGiSDHLAmOKEEDvRaZY6RaCbrrUUTdDHTauXhbClXXY7dhy55zvQ2BRpx00My0QUCOIbPsFSrbhLDiJwWJ7wx61YG/L84W3r+9Sn2A2y9Ygoj0IRHsaWaqj1CyT9l8bVbYkCFPxOCxmJh8fapbV3AOMRkuVOw3dQiKEDHWapi1pnJwGgyeKWBNAATgE7+gya0eHte2JPlzVx/Zg3iNFoEfn5in1kvzWrTvsUkvtax79VdaaRi0ZNLTp4Q3lpY4RZjf4oDbGZeJfnhVduFuTJKwMI5G75iudQaui02cgPD2/wAB0jxOtdeXcWUB6AAAewAqamuRFpQ/2PufekXX0OpzCUn6Rqi/qlAQRKDwSncgcwMxSTdVOsnX6LSCN1Ql/mKq25SO+wOQt/Ohe3571OjGkI5aOQ0e4c0Y8Qbaz9VHcSSyWTJJkk8mmq/QsNR8XeRL7PilX65uLJZOSd6XddAHG8444Qn3NDYZEOcc9qf2wwYb6g1BxQagRIYK3DR9wKEahAIBKKYcFYY3pO2GDDe6q+8pbf6/gUDC3bMuFChee+4wpsGl9aGB2aqIKEcsi6SfqD9IVVfaijkcEEe4g1QA9WPJS38USFpbtuV2FcrgN9oPEGjRi7jV3FnHoH8VQgg588etH0/UjcLZzm0TkG1x5OpYAm2H3I3hLst/jyqrbCQTsE/UofJoHUdIBhQSeJY37TIq7QymBmTiA/sqUTTAlkvYKO7LjA59KAL07WUwBuTsOe/kJqiX7UzR0uq4DqttYJdxIATKJWSoXIpd9pBIIIIKIMEEZBHNNMBviL7rrjdfN1yJxLEGO1KIIRS3DGZzOQwfapakZUR3LEdoZ9Kol+lN9gVfcyTyXsPgVVtQimHZ7RgDc55/OKSAlq3748o9GqompQGmwQXVR4zv3B/bHlVK2f7jhYHm8+lULscihMAxeQwCQDnv50WneqC0hy12KPbI5o0mCAzaEiIfSXG6YR55FVLx6hNGnU1LYICKxOwTk75qadhIbs/9rgD7GspIBGCNxI/9T/ii6wGAWHBwxyq1/wCTSfk03XjcodpPsw6z3apVSpRdMSAtubgSO8KSROYPvG1AuSoJ55QjDI+XUqVgy0JdGTwF+d6lSpGC6s1KlABWBlD5IHyaPUukDq6gAFneVPBJqVKaAG5bE4GQp33ouh/2goBmXhM4EM1KlAAi1gpsdoAwydpIHrSqlSkMlM07SShn+POpUpoAzDBEiC2CCMhfzQGpUp/gRYuC78vbyX3o7rPqVw6ASNiUCi0SzBeaqpSYCrVu12q7LlsDBE9wQ/MN1KlIYVthJ+kHMDJ7Dv7UNtSpQhF3nsu3HaaXUqUAgh7/AJ2o8k4tyVK8hk9p96lSgCW03ruuJd2QWSePqydyR6k96lSqQAC08HD9E35KaroJZUDJ2Dw6lSgCG2qFxDRIBCPcMFHkMA+gqVKGCDtF1tym24MHII2IPG4q7gAN2/RQo5bq6lUvBMUadZpkhu2ebrR8OpUpDP/Z';
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
        canvas.addEventListener("mousedown", function(e)
        {
            point = getMousePosition(canvas, e);
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
				        console.log(time);

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
    </script>
</body>
  
</html>
    """,
    height=600,
)

st.markdown("## Instructions")
st.markdown("Look for and click on all the aliens!")
st.markdown("Your time will be submitted on the leaderboard once you finish!")

if st.session_state.logged_in:
        st.sidebar.markdown("Logged in as: " + st.session_state.username)
        log_out = st.sidebar.button("Log Out")
        if log_out:
                show_pages(
                    [
                        Page("1_🌌_Home.py", "Home", "🌌"),
                        Page("pages/2_👾_Instructions.py", "Instructions", "👾"),
                        Page("pages/3_👽_Login.py", "Login", "👽"),
                        # Page("pages\4_🎮_Play.py", "Instructions", "🎮"),
                        Page("pages/5_🛸_Register.py", "Register", "🛸"),
                    ]
                )
                switch_page("Home")